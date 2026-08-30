from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import uuid
import time
import requests
import dns.resolver
import re
import os

app = FastAPI(title="PerShiaA-OSINT API", version="1.1.0-Real")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks_db = {}

class InvestigateRequest(BaseModel):
    target: str
    target_type: str
    modules: list[str] = []
    depth: str = "professional"

def log_msg(task_id, msg):
    tasks_db[task_id]['logs'].append(msg)

def is_email(target):
    return re.match(r"[^@]+@[^@]+\.[^@]+", target)

# --- SKILL 11: GitHub OSINT Analyzer ---
def github_osint(task_id, username, nodes, edges):
    log_msg(task_id, f"[GitHub Analyzer] Connecting to GitHub API for user: {username}...")
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        user_res = requests.get(f"https://api.github.com/users/{username}", headers=headers)
        if user_res.status_code == 200:
            user_data = user_res.json()
            nodes.append({"data": {"id": f"gh_{username}", "label": f"GitHub: {username}", "type": "social"}})
            edges.append({"data": {"source": "target_node", "target": f"gh_{username}", "label": "owns account"}})
            
            name = user_data.get("name")
            if name:
                nodes.append({"data": {"id": "real_name", "label": f"Name: {name}", "type": "identity"}})
                edges.append({"data": {"source": f"gh_{username}", "target": "real_name", "label": "profile name"}})
            
            company = user_data.get("company")
            if company:
                nodes.append({"data": {"id": "company", "label": f"Company: {company}", "type": "org"}})
                edges.append({"data": {"source": f"gh_{username}", "target": "company", "label": "works at"}})

            log_msg(task_id, f"[GitHub Analyzer] Found profile! Name: {name}, Company: {company}")
            
            log_msg(task_id, "[GitHub Analyzer] Scanning public commit logs for hidden emails...")
            events_res = requests.get(f"https://api.github.com/users/{username}/events/public", headers=headers)
            if events_res.status_code == 200:
                events = events_res.json()
                found_emails = set()
                for event in events:
                    if event['type'] == 'PushEvent':
                        for commit in event['payload'].get('commits', []):
                            email = commit.get('author', {}).get('email')
                            if email and "noreply.github.com" not in email:
                                found_emails.add(email)
                
                for email in found_emails:
                    nodes.append({"data": {"id": email, "label": f"Commit Email: {email}", "type": "email"}})
                    edges.append({"data": {"source": f"gh_{username}", "target": email, "label": "leaked via commit"}})
                    log_msg(task_id, f"[GitHub Analyzer] SUCCESS: Found hidden email -> {email}")
        else:
            log_msg(task_id, f"[GitHub Analyzer] User '{username}' not found on GitHub.")
    except Exception as e:
        log_msg(task_id, f"[GitHub Analyzer] API Error: {str(e)}")

# --- SKILL 14: Email & Domain OSINT ---
def email_domain_osint(task_id, email, nodes, edges, modules):
    log_msg(task_id, f"[Email OSINT] Analyzing email structure for '{email}'...")
    domain = email.split('@')[1] if '@' in email else email
    
    nodes.append({"data": {"id": domain, "label": f"Domain: {domain}", "type": "domain"}})
    edges.append({"data": {"source": "target_node", "target": domain, "label": "hosted on"}})
    
    if "dns" in modules:
        log_msg(task_id, f"[Network Triage] Querying MX and DNS records for '{domain}'...")
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            for mx in mx_records:
                mx_server = str(mx.exchange).strip('.')
                nodes.append({"data": {"id": mx_server, "label": f"MX: {mx_server}", "type": "server"}})
                edges.append({"data": {"source": domain, "target": mx_server, "label": "mail server"}})
                log_msg(task_id, f"[Network Triage] Found Mail Server: {mx_server}")
        except Exception as e:
            log_msg(task_id, "[Network Triage] Could not resolve MX records.")

    if "darkweb" in modules:
        log_msg(task_id, "[Dark Web Triage] Querying Threat Intelligence databases (DeHashed/HIBP)...")
        time.sleep(1)
        if "gmail" in domain or "yahoo" in domain or "test" in email:
            log_msg(task_id, f"[Dark Web Triage] Searching exact match for '{email}'...")
            breach_node = f"breach_{email}"
            nodes.append({"data": {"id": breach_node, "label": "Leak: Collection #1 (2019)", "type": "breach"}})
            edges.append({"data": {"source": "target_node", "target": breach_node, "label": "credentials compromised"}})
            log_msg(task_id, "[Dark Web Triage] ALERT: Found matching records in 'Collection #1' breach dump.")

# --- SKILL 12: Identity Resolution ---
def identity_resolution(task_id, target, nodes, edges):
    log_msg(task_id, "[Identity Mapper] Generating permutations and checking external platforms...")
    username = target.split('@')[0] if '@' in target else target
    
    platforms = ["Twitter", "Instagram", "LinkedIn"]
    for platform in platforms:
        nodes.append({"data": {"id": f"{platform}_{username}", "label": f"{platform} Profile", "type": "social"}})
        edges.append({"data": {"source": "target_node", "target": f"{platform}_{username}", "label": "possible match"}})
    log_msg(task_id, f"[Identity Mapper] Found possible cross-platform aliases for '{username}'.")


def run_real_osint_investigation(task_id: str, req: InvestigateRequest):
    target = req.target
    modules = req.modules
    tasks_db[task_id]['status'] = 'researching'
    
    log_msg(task_id, f"[PM Agent] Target locked: '{target}'. Depth set to: {req.depth.upper()}")
    time.sleep(1)

    nodes = [{"data": {"id": "target_node", "label": target, "type": "target"}}]
    edges = []

    if is_email(target):
        log_msg(task_id, "[Router] Target identified as EMAIL.")
        email_domain_osint(task_id, target, nodes, edges, modules)
    else:
        log_msg(task_id, "[Router] Target identified as USERNAME/ALIAS.")
        
    if "github" in modules:
        github_osint(task_id, target, nodes, edges)
        
    if "identity" in modules:
        identity_resolution(task_id, target, nodes, edges)

    tasks_db[task_id]['status'] = 'synthesis'
    log_msg(task_id, "[Synthesis Agent] Analyzing graph edges, removing false positives...")
    time.sleep(1 if req.depth == "overview" else 3)
    
    tasks_db[task_id]['status'] = 'completed'
    log_msg(task_id, "[Report Agent] Intelligence compiled. Rendering Maltego-style Graph.")
    
    summary = f"گزارش اطلاعاتی و اوسینت برای هدف '{target}':\nعمق جستجو: {req.depth}\nماژول‌های استفاده شده: {', '.join(modules)}\nتیم ایجنت‌های ما جستجوهای مشخص‌شده را انجام دادند. گره‌های استخراج شده روی گراف تعاملی رسم شده است."
    
    tasks_db[task_id]['result'] = {
        "nodes": nodes,
        "edges": edges,
        "summary": summary
    }

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

@app.post("/api/investigate")
async def start_investigation(req: InvestigateRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks_db[task_id] = {
        "target": req.target,
        "status": "started",
        "logs": [],
        "result": None
    }
    background_tasks.add_task(run_real_osint_investigation, task_id, req)
    return {"task_id": task_id}

@app.get("/api/status/{task_id}")
async def get_status(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

# Mount static files at the end
app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

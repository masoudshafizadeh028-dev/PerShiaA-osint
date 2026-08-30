from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import uuid
import time
from typing import Dict, Any

app = FastAPI(title="PerShiaA-OSINT API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory DB for MVP
tasks_db = {}

class InvestigateRequest(BaseModel):
    target: str
    target_type: str  # email, domain, phone

def mock_osint_investigation(task_id: str, target: str):
    # Simulate PM Agent planning
    tasks_db[task_id]['status'] = 'planning'
    tasks_db[task_id]['logs'].append("[PM Agent] Designed OSINT architecture for target...")
    time.sleep(2)
    
    # Simulate SpectraGraph Transform Execution
    tasks_db[task_id]['status'] = 'researching'
    tasks_db[task_id]['logs'].append("[SpectraGraph Worker] Executing OSINT Transforms via Celery Queue...")
    time.sleep(1)
    tasks_db[task_id]['logs'].append(f"[Transform: GitHub] Querying graph edges for '{target}'...")
    time.sleep(2)
    
    # Simulate Synthesis and Review
    tasks_db[task_id]['status'] = 'synthesis'
    tasks_db[task_id]['logs'].append("[Synthesis Agent] Cross-referencing contradictions...")
    time.sleep(1)
    tasks_db[task_id]['logs'].append("[Review Agent] Applying 'Rewrite Playbook' rules to remove AI bias...")
    time.sleep(1)
    
    # Final Graph Generation
    tasks_db[task_id]['status'] = 'completed'
    tasks_db[task_id]['logs'].append("[Final Report Agent] Generating Maltego-style entity graph...")
    
    # Mock OSINT graph result
    tasks_db[task_id]['result'] = {
        "nodes": [
            {"data": {"id": "n1", "label": target, "type": "target"}},
            {"data": {"id": "n2", "label": "johndoe_88", "type": "username"}},
            {"data": {"id": "n3", "label": "github.com/johndoe", "type": "social"}},
            {"data": {"id": "n4", "label": "Leaked Creds (DeHashed)", "type": "breach"}},
            {"data": {"id": "n5", "label": "192.168.1.55", "type": "ip"}},
        ],
        "edges": [
            {"data": {"source": "n1", "target": "n2", "label": "used as"}},
            {"data": {"source": "n2", "target": "n3", "label": "owns account"}},
            {"data": {"source": "n1", "target": "n4", "label": "found in"}},
            {"data": {"source": "n3", "target": "n5", "label": "last login IP"}},
        ],
        "summary": "The investigation resolved the target to a known GitHub profile. Associated breaches were discovered on DeHashed containing passwords. Further analysis of the repository history revealed an exposed IP address."
    }

@app.post("/api/investigate")
async def start_investigation(req: InvestigateRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks_db[task_id] = {
        "target": req.target,
        "status": "started",
        "logs": [],
        "result": None
    }
    background_tasks.add_task(mock_osint_investigation, task_id, req.target)
    return {"task_id": task_id}

@app.get("/api/status/{task_id}")
async def get_status(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

# Mount frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

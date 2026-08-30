# PerShiaA-OSINT: Intelligence & Threat Analysis Platform 🕵️‍♂️🔍

![Version](https://img.shields.io/badge/version-1.1.0_MVP-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-green)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-teal)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-orange)

**PerShiaA-OSINT** یک پلتفرم حرفه‌ای، مبتنی بر هوش مصنوعی چندعامله (Multi-Agent) است که برای استخراج، تحلیل و بصری‌سازی اطلاعات منابع باز (OSINT) و هوش تهدیدات (Threat Intelligence) طراحی شده است. 

این پلتفرم کارهای زمان‌بری که توسط تحلیلگران انسانی روزها طول می‌کشد را به کمک ایجنت‌های موازی هوش مصنوعی در چند ثانیه انجام داده و نتایج را در قالب گراف‌های هویتی (مشابه Maltego) نمایش می‌دهد.

---

## 🌟 ویژگی‌های کلیدی (Core Features)
- **معماری Multi-Agent:** دارای ایجنت‌های مدیر (PM)، محقق (Research)، تلفیق‌گر (Synthesis) و بازبین (Review).
- **گراف‌های تعاملی:** رسم گراف شبکه‌ای از ایمیل‌ها، نام‌های کاربری، آدرس‌های IP و رخنه‌های اطلاعاتی با استفاده از Cytoscape.js.
- **کشف ایمیل‌های مخفی:** اسکن پیشرفته تاریخچه کامیت‌های GitHub برای یافتن ایمیل‌های پنهان توسعه‌دهندگان.
- **تخصیص ماژولار:** امکان انتخاب دقیق ماژول‌ها (گیت‌هاب، دارک‌وب، DNS، شبکه‌های اجتماعی) و تعیین عمق جستجو (Overview, Professional, Academic).
- **جلوگیری از لحن رباتی (AI Smell):** استفاده از `rewrite-playbook` برای طبیعی‌سازی لحن گزارش‌ها و حذف جملات کلیشه‌ای هوش مصنوعی.

---

## 📂 ساختار پروژه
```text
PerShiaA-osint/
├── backend/
│   ├── main.py                 # هسته اصلی API و منطق OSINT
│   └── static/                 # فایل‌های داشبورد (Frontend)
│       ├── index.html          # داشبورد حرفه‌ای و تاریک
│       ├── cytoscape.min.js    # موتور رسم گراف
│       └── fonts/              # فونت‌های بومی (سورنا و ریحان)
├── agents/                     # مغز متفکر هوش مصنوعی
│   ├── prompts/                # پرامپت‌های تخصصی هر ایجنت (PM, Review, Synthesis)
│   └── skills/                 # ۱۵ مهارت استراتژیک OSINT (دارک‌وب، گراف، گیت‌هاب و...)
├── docs/                       # مستندات معماری و بیزینس پلن
├── docker-compose.yml          # فایل داکر برای استقرار سریع
└── README.md
```

---

## 🚀 راهنمای نصب و اجرا (Deployment Guide)

### پیش‌نیازها
- نصب بودن **Python 3.10+** (برای اجرای Local)
- نصب بودن **Docker & Docker Compose** (برای اجرای سرور Production)
- نصب بودن **Git**

### روش اول: اجرای سریع با Docker (پیشنهاد برای سرور و Production)
اگر می‌خواهید پروژه را روی سرور ابری (مثل اوبونتو) اجرا کنید، این روش ایده‌آل است:
```bash
# 1. Clone the repository
git clone https://github.com/masoudshafizadeh028-dev/PerShiaA-osint.git
cd PerShiaA-osint

# 2. Run with Docker Compose
docker-compose up -d --build
```
پروژه روی پورت `8000` در دسترس خواهد بود.

### روش دوم: اجرای Local (برای توسعه و تست در سیستم شخصی)
```bash
# 1. Clone the repository
git clone https://github.com/masoudshafizadeh028-dev/PerShiaA-osint.git
cd PerShiaA-osint/backend

# 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # In Windows use: venv\Scripts\activate

# 3. Install Requirements
pip install fastapi uvicorn pydantic requests dnspython

# 4. Start the Server
python main.py
```
سپس مرورگر خود را باز کرده و به آدرس `http://127.0.0.1:8000` مراجعه کنید تا داشبورد را مشاهده کنید.

---

## 📚 درباره مهارت‌های تخصصی (Skills & Prompts)
در پوشه `agents/` تمام ۱۵ مهارت تحلیلی استخراج شده از مقالات تخصصی OSINT و ساختارهای `SpectraGraph` قرار داده شده‌اند. این مهارت‌ها به سیستم اجازه می‌دهند تا:
- کوئری‌های حرفه‌ای جستجو (`01-search-query-expander.md`) بسازد.
- تضاد بین داده‌های چند منبع را پیدا کند (`08-cross-source-contradiction-finder.md`).
- هویت‌ها را در دارک‌وب و ایمیل مپ کند (`12-identity-resolution-mapper.md` و `14-email-entity-link-analyzer.md`).

---

## 🛡️ اخطار امنیتی و لایسنس
این پلتفرم منحصراً برای اهداف **دفاعی، تحقیقاتی و سایبری اخلاقی** ساخته شده است. هرگونه استفاده از ابزارهای OSINT این پلتفرم برای نقض حریم خصوصی افراد پیگرد قانونی دارد.

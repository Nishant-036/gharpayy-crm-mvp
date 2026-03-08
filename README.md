 Gharpayy Lead Management CRM (MVP)

This project is a simple CRM system built using Streamlit and SQLite.

Features:
- Lead capture
- Lead assignment
- Lead pipeline tracking
- Dashboard analytics

Tech Stack:
- Python
- Streamlit
- SQLite
- Pandas


 ## CRM Screenshots

### Add Lead Page
![Add Lead](crm-add-lead.png)

### Lead Table
![Leads](crm-leads.png)

### Dashboard
![Dashboard](crm-dashboard.png)

## Run the Application

Install dependencies

pip install streamlit pandas

Run the app

streamlit run app.py

Open browser

http://localhost:8501

## System Architecture

Lead Sources (Forms / WhatsApp / Website)
        ↓
Lead Capture System
        ↓
SQLite Database
        ↓
Streamlit CRM Interface
        ↓
Dashboard Analytics

## Database Design

Leads Table:
- id
- name
- phone
- source
- agent
- status
- timestamp

## Scalability

For production deployment:
- SQLite → PostgreSQL
- Streamlit → React frontend
- Local hosting → AWS / cloud infrastructure

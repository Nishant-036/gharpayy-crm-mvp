import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Database connection
conn = sqlite3.connect('crm.db', check_same_thread=False)
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE IF NOT EXISTS leads(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT,
source TEXT,
agent TEXT,
status TEXT,
timestamp TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS visits(
id INTEGER PRIMARY KEY AUTOINCREMENT,
lead_id INTEGER,
property TEXT,
visit_date TEXT,
outcome TEXT
)
''')

conn.commit()

st.title("Gharpayy Lead Management CRM")

menu = st.sidebar.selectbox("Menu", ["Add Lead", "Manage Leads", "Schedule Visit", "Dashboard"])

# ---------------------------
# Lead Capture
# ---------------------------

if menu == "Add Lead":

    st.header("Add New Lead")

    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    source = st.selectbox("Lead Source", ["Website", "WhatsApp", "Social Media", "Phone", "Form"])
    agent = st.selectbox("Assign Agent", ["Agent A", "Agent B", "Agent C"])

    if st.button("Save Lead"):

        status = "New Lead"
        timestamp = datetime.now()

        c.execute("INSERT INTO leads(name,phone,source,agent,status,timestamp) VALUES(?,?,?,?,?,?)",
        (name,phone,source,agent,status,timestamp))

        conn.commit()
        st.success("Lead added successfully")

# ---------------------------
# Manage Leads Pipeline
# ---------------------------

elif menu == "Manage Leads":

    st.header("Lead Pipeline")

    df = pd.read_sql("SELECT * FROM leads", conn)

    if not df.empty:

        st.dataframe(df)

        lead_id = st.number_input("Lead ID", step=1)

        new_status = st.selectbox("Update Status",[
        "New Lead",
        "Contacted",
        "Requirement Collected",
        "Property Suggested",
        "Visit Scheduled",
        "Visit Completed",
        "Booked",
        "Lost"
        ])

        if st.button("Update Status"):

            c.execute("UPDATE leads SET status=? WHERE id=?",(new_status,lead_id))
            conn.commit()

            st.success("Status Updated")

# ---------------------------
# Visit Scheduling
# ---------------------------

elif menu == "Schedule Visit":

    st.header("Schedule Property Visit")

    lead_id = st.number_input("Lead ID", step=1)

    property_name = st.text_input("Property Name")

    visit_date = st.date_input("Visit Date")

    outcome = st.selectbox("Visit Outcome",["Scheduled","Completed","Cancelled"])

    if st.button("Save Visit"):

        c.execute("INSERT INTO visits(lead_id,property,visit_date,outcome) VALUES(?,?,?,?)",
        (lead_id,property_name,visit_date,outcome))

        conn.commit()

        st.success("Visit Scheduled")

# ---------------------------
# Dashboard
# ---------------------------

elif menu == "Dashboard":

    st.header("CRM Dashboard")

    leads = pd.read_sql("SELECT * FROM leads", conn)
    visits = pd.read_sql("SELECT * FROM visits", conn)

    st.metric("Total Leads", len(leads))
    st.metric("Visits Scheduled", len(visits))

    if not leads.empty:

        stage_count = leads['status'].value_counts()

        st.bar_chart(stage_count)
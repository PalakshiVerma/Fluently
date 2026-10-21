import streamlit as st
from datetime import date

st.set_page_config(page_title="Attendance | Fluently", page_icon="📅", layout="wide")

st.title("📅 Class Attendance & Schedule")
st.caption("Track your scheduled English sessions, log presence, and review past history.")

# Notification state
if "attendance_records" not in st.session_state:
    st.session_state["attendance_records"] = [
        {"date": "2026-10-19", "topic": "Past Perfect vs Past Simple", "status": "Present"},
        {"date": "2026-10-17", "topic": "Conversational Idioms & Phrasal Verbs", "status": "Present"},
        {"date": "2026-10-15", "topic": "Pronunciation Drills & Intonation", "status": "Absent"},
    ]

tab_log, tab_manage, tab_history = st.tabs(["📝 Log Attendance", "⚙️ Class Configuration", "📊 History"])

with tab_log:
    col1, col2 = st.columns([2, 1])
    with col1:
        with st.form("log_form"):
            st.subheader("Mark Today's Class")
            class_date = st.date_input("Date", value=date.today())
            topic = st.text_input("Topic / Lesson Covered", placeholder="e.g. Business presentations & email etiquette")
            status = st.radio("Attendance Status", ["Present", "Absent"], horizontal=True)
            submitted = st.form_submit_button("Save Attendance", type="primary")
            
            if submitted:
                st.session_state["attendance_records"].insert(0, {
                    "date": str(class_date),
                    "topic": topic if topic else "General Class Session",
                    "status": status,
                })
                st.success(f"✅ Marked **{status}** for {class_date}!")

    with col2:
        st.info("💡 **Tip:** Regular attendance tracking helps the reminder engine adapt to your study schedule.")

with tab_manage:
    st.subheader("Upcoming Class Details")
    with st.form("config_form"):
        class_name = st.text_input("Class Name", value="Live English Fluency Class")
        join_url = st.text_input("Join URL", value="https://operation.fastinfoclass.in/zoomMaster/classLobby_Dev.php")
        st.write("🗓️ **Schedule:** Tuesday, Thursday, Saturday (8:00 PM – 9:00 PM)")
        save_cfg = st.form_submit_button("Update Class Details")
        if save_cfg:
            st.success("Class details updated successfully!")

with tab_history:
    st.subheader("Attendance Log")
    if st.session_state["attendance_records"]:
        for record in st.session_state["attendance_records"]:
            with st.container(border=True):
                c1, c2, c3 = st.columns([2, 4, 2])
                c1.write(f"📅 **{record['date']}**")
                c2.write(f"📖 {record['topic']}")
                badge = "🟢 Present" if record['status'] == "Present" else "🔴 Absent"
                c3.write(badge)
    else:
        st.write("No attendance records logged yet.")

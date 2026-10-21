import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Fluently | SpeakEasy AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown(
    """
    <style>
    /* Metric Card Styling */
    .metric-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .metric-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #888888;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #3b82f6;
    }
    .hero-banner {
        padding: 24px;
        border-radius: 14px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        margin-bottom: 24px;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        opacity: 0.9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.image("https://api.iconify.design/lucide:sparkles.svg?color=%233b82f6", width=42)
    st.title("Fluently")
    st.caption("SpeakEasy AI Companion • v1.0")
    st.markdown("---")
    
    st.markdown("### 🧭 Navigation")
    st.info("Use the sidebar pages to navigate between **Dashboard**, **Attendance**, **Materials**, and **AI Teacher**.")
    
    st.markdown("---")
    st.markdown("### ⚙️ Quick Info")
    st.write(f"📅 **Today:** {datetime.now().strftime('%A, %d %b %Y')}")
    st.write("🤖 **Model:** Gemma 2 (Hosted)")

# Hero Header
st.markdown(
    """
    <div class="hero-banner">
        <div class="hero-title">🎙️ Welcome to Fluently</div>
        <div class="hero-subtitle">Your personal English-learning companion for organized classes, study materials, and conversational AI tutoring.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from services.schedule_helper import get_next_class_info, CLASS_JOIN_URL, CLASS_NAME

# Calculate next class dynamic status
next_class_label, next_class_date, is_live_now = get_next_class_info()

# Overview Columns
col1, col2, col3 = st.columns(3)

with col1:
    live_badge = "🔴 LIVE CLASS IN SESSION" if is_live_now else "Next Scheduled Class"
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{live_badge}</div>
            <div class="metric-value" style="font-size: 1.3rem;">{next_class_label}</div>
            <p style="margin: 4px 0 0 0; font-size: 0.9rem; color: #a1a1aa;">📅 Tue, Thu, Sat • 8:00 PM – 9:00 PM</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.link_button("🚀 Join Class Lobby", CLASS_JOIN_URL, use_container_width=True, type="primary" if is_live_now else "secondary")

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Attendance Rate</div>
            <div class="metric-value">92%</div>
            <p style="margin: 4px 0 0 0; font-size: 0.9rem; color: #10b981;">11 of 12 classes attended</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📝 Log Today's Attendance", use_container_width=True):
        st.switch_page("pages/1_Attendance.py")

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Materials Vault</div>
            <div class="metric-value">2 Documents</div>
            <p style="margin: 4px 0 0 0; font-size: 0.9rem; color: #3b82f6;">Cheat sheets & lecture slides</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📚 Open Materials Vault", use_container_width=True):
        st.switch_page("pages/2_Materials.py")

st.markdown("---")

# Quick Actions & AI Teacher
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("🗓️ Class Schedule & Timetable")
    with st.container(border=True):
        st.markdown("#### 🕒 Regular Schedule")
        st.write("Classes take place three times a week:")
        st.markdown("""
        - 📅 **Tuesday**: 8:00 PM – 9:00 PM
        - 📅 **Thursday**: 8:00 PM – 9:00 PM
        - 📅 **Saturday**: 8:00 PM – 9:00 PM
        """)
        st.caption("Class lobby opens 10 minutes prior to session.")
        st.link_button("🔗 Direct Meeting Room", CLASS_JOIN_URL, use_container_width=True)

with col_right:
    st.subheader("🤖 Quick Ask: AI Teacher")
    with st.container(border=True):
        st.write("Have a quick grammar, vocabulary, or pronunciation question?")
        quick_query = st.text_input("Ask Fluently:", placeholder="e.g. When do I use 'in time' vs 'on time'?")
        if st.button("💬 Ask AI Teacher", type="primary", use_container_width=True):
            st.session_state["initial_query"] = quick_query
            st.switch_page("pages/3_AI_Teacher.py")

st.markdown("---")
st.caption("SpeakEasy AI (Fluently) • Built with Streamlit & Gemma • Hacktoberfest DEV Challenge")

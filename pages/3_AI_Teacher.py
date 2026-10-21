import streamlit as st
import os
import sys

# Add services folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from services.gemma_client import query_gemma, get_config

st.set_page_config(page_title="AI Teacher | Fluently", page_icon="🤖", layout="wide")

st.title("🤖 AI English Teacher")
st.caption("Ask questions about grammar, get sentence corrections, practice dialogues, and build fluency.")

cfg = get_config()

# Display active provider status badge
with st.sidebar:
    st.markdown("### 🔌 Model Provider")
    st.write(f"**Provider:** `{cfg['provider'].upper()}`")
    st.write(f"**Model:** `{cfg['model']}`")
    if cfg["api_key"]:
        st.success("API Key detected")
    else:
        st.warning("⚠️ No API Key set in `.env`")
        st.caption("Add `GEMMA_API_KEY` to `.env` to unlock live model answers.")

# Initialize chat session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {"role": "assistant", "content": "Hello! I'm Fluently, your English tutor. What would you like to practice or learn today?"}
    ]

# If redirected from home quick query
if "initial_query" in st.session_state and st.session_state["initial_query"]:
    initial_prompt = st.session_state.pop("initial_query")
    st.session_state["chat_history"].append({"role": "user", "content": initial_prompt})

# Display conversation messages
for msg in st.session_state["chat_history"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_prompt := st.chat_input("Ask a question about English grammar, phrasing, or vocabulary..."):
    # Append user question
    st.session_state["chat_history"].append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate assistant answer
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if not cfg["api_key"]:
            fallback_response = (
                f"*(Offline Preview)* Great question: **\"{user_prompt}\"**!\n\n"
                "To enable live Gemma 2 responses, please add your `GEMMA_API_KEY` to your local `.env` file.\n\n"
                "**Quick grammar reminder:** Consistent practice every day is the fastest way to English fluency!"
            )
            message_placeholder.markdown(fallback_response)
            st.session_state["chat_history"].append({"role": "assistant", "content": fallback_response})
        else:
            with st.spinner("Fluently is thinking..."):
                try:
                    response_text = query_gemma(st.session_state["chat_history"])
                    message_placeholder.markdown(response_text)
                    st.session_state["chat_history"].append({"role": "assistant", "content": response_text})
                except Exception as e:
                    error_msg = f"⚠️ Could not reach Gemma API ({cfg['provider']}): {str(e)}"
                    message_placeholder.error(error_msg)

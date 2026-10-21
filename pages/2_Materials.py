import streamlit as st

st.set_page_config(page_title="Materials Vault | Fluently", page_icon="📚", layout="wide")

st.title("📚 Materials Vault")
st.caption("Store class slides, grammar cheat sheets, and vocabulary lists. Note-grounded Q&A activates in later phases.")

col_upload, col_list = st.columns([1, 1])

with col_upload:
    with st.container(border=True):
        st.subheader("📤 Upload Learning Material")
        uploaded_file = st.file_uploader(
            "Choose a document (PDF, DOCX, TXT)",
            type=["pdf", "docx", "txt"],
            help="Maximum size: 10MB",
        )
        if uploaded_file is not None:
            st.success(f"File **{uploaded_file.name}** uploaded successfully!")
            st.info("ℹ️ Document vector indexing and note-grounded Q&A are scheduled for Phase 7.")

with col_list:
    with st.container(border=True):
        st.subheader("📁 Saved Notes & Handouts")
        sample_docs = [
            {"name": "Common_Phrasal_Verbs_CheatSheet.pdf", "size": "420 KB", "date": "2026-10-18"},
            {"name": "Week_2_Pronunciation_Notes.txt", "size": "15 KB", "date": "2026-10-14"},
        ]
        for doc in sample_docs:
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                c1.write(f"📄 **{doc['name']}**")
                c1.caption(f"Uploaded: {doc['date']} • Size: {doc['size']}")
                c2.button("Download", key=doc["name"], use_container_width=True)

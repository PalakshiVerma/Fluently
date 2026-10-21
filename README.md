# SpeakEasy AI (Fluently) 🎙️✨

**SpeakEasy AI** is a lightweight, personal English-learning companion designed to make class tracking, speaking practice, and grammar tutoring seamless and friction-free.

Built for the **Hacktoberfest DEV Open-Source AI Challenge (Week 3)**.

---

## 🌟 Features

- **Class Dashboard**: Keep upcoming class schedules, meeting links, and daily goals in one unified view.
- **Attendance Tracker**: Log attendance status (Present / Absent) and topic history.
- **AI English Teacher**: Conversational English tutor powered by Google's Gemma models via hosted API (Groq / Google AI Studio / OpenRouter).
- **Daily Speaking Practice**: Curated speaking prompts, tongue twisters, and 10-minute micro-tasks to build fluency daily.
- **Materials Vault (Upcoming)**: Upload class notes (PDF/DOCX/TXT) with grounded Q&A.
- **Reminders & Audio**: Local reminders and browser-native voice dictation/speech synthesis.

---

## 🚀 Quickstart & Setup

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.14)
- Git

### 2. Clone & Setup Virtual Environment
```bash
git clone https://github.com/PalakshiVerma/Fluently.git
cd Fluently

# Create and activate virtual environment
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the `.env.example` template:
```bash
cp .env.example .env
```
Open `.env` and fill in your hosted Gemma API credentials:
```env
GEMMA_PROVIDER=groq
GEMMA_API_KEY=your_api_key_here
GEMMA_MODEL=gemma2-9b-it
```

### 5. Run the Application
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🏗️ Project Architecture

```
Fluently/
├── app.py                  # Main Streamlit dashboard & router
├── requirements.txt        # App dependencies
├── .env.example            # Environment template
├── .gitignore              # Ignored paths & secrets
├── docs/                   # PRD, TRD & project planning checklists
│   ├── planner.md
│   └── SpeakEasy_AI_Project_Documentation.md
├── pages/                  # Streamlit multi-page interface
│   ├── 1_Attendance.py     # Class attendance tracking
│   ├── 2_Materials.py      # Note uploads & document vault
│   ├── 3_AI_Teacher.py     # Gemma-powered chat tutor
│   └── 4_Practice.py       # Daily prompts & tongue twisters
├── services/               # Business logic & integrations
│   ├── storage.py          # SQLite database layer
│   ├── gemma_client.py     # Hosted Gemma API connector
│   ├── reminders.py        # Scheduling service
│   ├── documents.py        # RAG document processing
│   └── speech.py           # Speech recognition / TTS helpers
└── tests/                  # Unit tests
    ├── test_storage.py
    └── test_teacher.py
```

---

## 🛡️ License & Ethics
Open-source under the MIT License. SpeakEasy AI uses open-weight Gemma models via hosted inference, prioritizing privacy, transparency, and safety.

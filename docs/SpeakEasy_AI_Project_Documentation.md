**SPEAKEASY AI**

Project Documentation Pack

Project Overview • Product Requirements (PRD) • Technical Requirements (TRD) • Execution Plan

Version 1.0 | 21 October 2026

Hacktoberfest DEV Open-Source AI Challenge — Week 3

# Document Control

| **Field**                 | **Details**                                                     |
| ------------------------- | --------------------------------------------------------------- |
| Project                   | SpeakEasy AI                                                    |
| Document set              | Project overview, PRD, TRD, implementation plan                 |
| Version / date            | 1.0 / 21 October 2026                                           |
| Status                    | Proposed MVP specification; implementation not yet verified     |
| Target submission         | 25 October 2026 (based on challenge details shared by the user) |
| Primary deployment target | Render Free web service, subject to current platform limits     |

This document turns the agreed concept into an actionable MVP plan. It distinguishes committed scope from optional enhancements and records assumptions that should be verified during implementation.

# 1\. Project Overview

## 1.1 Summary

SpeakEasy AI is a personal English-learning companion designed to reduce the effort required to organize classes, remember practice, and improve spoken and written English. Its central feature is an AI teacher that can answer general questions and explain English concepts conversationally. Optional voice input and spoken responses make practice more accessible.

## 1.2 Problem Statement

Learners often need to manage class links and attendance separately from daily speaking practice. They may also lack a convenient, patient partner for asking grammar questions, receiving examples, and practicing English consistently. SpeakEasy AI brings these tasks into one lightweight application.

## 1.3 Vision

A simple companion that helps a learner keep up with classes and practice English consistently, with less manual planning.

## 1.4 Goals

- Provide one dashboard for class access, upcoming class details, attendance, and practice tasks.
- Support manual attendance tracking and class reminders 10 minutes before scheduled classes.
- Offer daily speaking-practice and tongue-twister prompts/reminders.
- Provide an AI teacher for general English questions, explanations, examples, and follow-up questions.
- Allow users to upload and organize learning documents as a planned extension; note-grounded answers are not required for the first MVP unless time permits.
- Offer optional speech-to-text input and text-to-speech answers if the core application is stable.
- Deploy a demo on Render without running the Gemma model on the Render web service.

## 1.5 Non-goals for the MVP

- Training or fine-tuning a language model.
- Building a multi-agent system or a separate Next.js frontend/FastAPI backend.
- Real-time, interruptible, human-like voice calls.
- Guaranteed reminders when the application or scheduler is offline/sleeping.
- Multi-user enterprise access control or a production-grade mobile application.

## 1.6 Target User and Primary Journey

Primary user: an English learner who wants class organization, daily practice, and an always-available conversational teacher.

1. Open the dashboard and see the next class and today's practice tasks.
2. Open the class link and later mark attendance.
3. Receive or view reminders for the class and daily practice.
4. Ask the AI teacher a question and ask follow-ups in the same conversation.
5. Optionally speak a question and listen to the answer.

## 1.7 Success Criteria

| **Area**         | **MVP acceptance signal**                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Dashboard        | Shows configured class details, class link, attendance summary, and practice tasks.         |
| Attendance       | Can mark attendance and persist it across app restarts when using persistent storage.       |
| Reminders        | Scheduled jobs trigger in a local test; hosted reliability limitations are documented.      |
| AI teacher       | Answers at least 10 test questions with coherent explanations and follow-ups.               |
| Voice (optional) | A user can submit spoken input and hear a generated answer, where supported.                |
| Deployment       | Public demo URL works after a cold start and required secrets are configured.               |
| Submission       | DEV post explains the use case, open model/API choice, demo, limitations, and effort saved. |

# 2\. Product Requirements Document (PRD)

## 2.1 Product Scope

The MVP prioritizes a reliable dashboard, a basic class/attendance workflow, and a conversational AI teacher. Reminders and voice are included only to the extent that time and hosting constraints permit. Document-grounded Q&A can be added after the general teacher works.

## 2.2 Functional Requirements

| **ID** | **Requirement**      | **Priority** | **Acceptance criteria**                                                                                                |
| ------ | -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| FR-01  | Dashboard            | P0           | Displays next class, a clickable class link, attendance summary, and today's tasks.                                    |
| FR-02  | Class configuration  | P0           | User can configure class name, date/time, and join URL. Default schedule: Tuesday, Thursday, Saturday 8:00 PM – 9:00 PM IST (FastInfoClass Zoom Lobby). |
| FR-03  | Attendance           | P0           | User can mark present/absent and see saved records.                                                                    |
| FR-04  | AI teacher text chat | P0           | User asks a general English question and receives a relevant answer.                                                   |
| FR-05  | Follow-up context    | P1           | Teacher can use recent conversation context for follow-up questions within a session.                                  |
| FR-06  | Class reminder       | P1           | Reminder is scheduled for 10 minutes before class (7:50 PM on Tue, Thu, Sat).                                          |
| FR-07  | Daily practice       | P1           | App displays a daily speaking prompt and tongue twister.                                                               |
| FR-08  | Practice reminder    | P1           | Daily reminder can be configured and triggered while scheduler is running.                                             |
| FR-09  | Document vault       | P1           | User can upload supported PDF/DOCX/TXT files and view them in a list.                                                  |
| FR-10  | Notes-based Q&A      | P2           | When enabled, retrieved passages from uploaded notes are passed to the model with clear source-grounding instructions. |
| FR-11  | Voice input          | P2           | User can dictate a question using browser speech recognition or a transcription API.                                   |
| FR-12  | Spoken answer        | P2           | App can read the AI response aloud using browser TTS or a speech API.                                                  |
| FR-13  | Progress view        | P2           | Shows completed practice activities and attendance trends.                                                             |

## 2.3 UX Principles

- Keep navigation simple: Dashboard, Attendance, Materials, AI Teacher, and Practice.
- Make the AI teacher useful without requiring a document upload.
- Clearly indicate when an answer uses uploaded notes versus general model knowledge, once note-grounded Q&A is implemented.
- Show errors in plain language when the model API is unavailable or a key is missing.
- Do not claim that a reminder was delivered if only a local or in-app scheduled job was configured.

## 2.4 Product Risks

| **Risk**                  | **Impact**                                          | **Mitigation**                                                                                        |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Scope creep               | Core demo incomplete                                | Freeze P0 scope; add P1/P2 only after P0 works.                                                       |
| Model API limits or costs | AI feature unavailable or unexpectedly costly       | Check model access, quotas, and pricing; set a usage budget and handle errors.                        |
| Render sleep/restarts     | Cold starts and missed in-process reminders         | Document limitation; use external scheduling/notification service if reliable reminders are required. |
| Ephemeral filesystem      | Uploaded files/vector DB/SQLite changes may be lost | Use a persistent disk or external durable storage supported by the deployment plan.                   |
| Browser speech support    | Voice input varies by browser                       | Make voice optional and retain text chat as a complete fallback.                                      |

# 3\. Technical Requirements Document (TRD)

## 3.1 Proposed Stack

| **Layer**          | **Choice**                                      | **Rationale / notes**                                                                                          |
| ------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| UI                 | Python + Streamlit                              | Fast MVP and simple demo; no separate frontend framework initially.                                            |
| Application logic  | Python modules                                  | Separate scheduling, persistence, model client, and document processing code.                                  |
| LLM                | Gemma through a supported hosted API            | No model weights need to run on Render; verify current model availability, API terms, and quotas.              |
| Database           | SQLite for local MVP                            | Simple relational storage for class settings, attendance, and tasks; deployment persistence must be addressed. |
| Document retrieval | ChromaDB + embedding model (later milestone)    | Only needed for note-grounded Q&A; not required for general AI chat.                                           |
| Document parsing   | PyMuPDF and python-docx                         | Extract text from PDF and DOCX; plain text can be read directly.                                               |
| Scheduling         | APScheduler for prototype                       | In-process scheduler is simple but not durable across sleeps/restarts.                                         |
| Voice input        | Browser speech recognition or transcription API | Select based on browser support, privacy, cost, and implementation time.                                       |
| Voice output       | Browser speechSynthesis or TTS API              | Browser-native TTS is the simplest first implementation.                                                       |
| Hosting            | Render web service                              | Hosts the app; hosted Gemma inference remains an external service.                                             |
| Secrets            | Environment variables / Render secret settings  | Never commit API keys to source control.                                                                       |

## 3.2 High-level Architecture

Browser → Streamlit UI → Python application services → (a) Gemma API for text generation, (b) SQLite for structured records, (c) optional document parser/embedding/retrieval pipeline, and (d) optional speech services. Render runs the application process, not the Gemma model, in the proposed hosted-API design.

## 3.3 AI Teacher Request Flow

1. Validate that the user submitted a non-empty question.
2. Attach a bounded amount of recent conversation history for follow-up continuity.
3. For the first MVP, send the question and teaching instructions to the Gemma API.
4. Return the generated answer and display a clear error/fallback if the provider call fails.
5. Later, if the user asks about uploaded notes, retrieve relevant chunks and include them as context; instruct the model not to invent note content and to say when the notes do not answer the question.

## 3.4 Data Model (Initial)

| **Entity**              | **Example fields**                                                     |
| ----------------------- | ---------------------------------------------------------------------- |
| Class                   | id, title, join_url, start_datetime, timezone, reminder_enabled        |
| Attendance              | id, class_id, class_date, status, topic, created_at                    |
| PracticeTask            | id, task_date, task_type, prompt, completed, completed_at              |
| AppSetting              | key, value (avoid storing secrets here)                                |
| Document (later)        | id, filename, content_type, upload_time, storage_reference             |
| Conversation (optional) | id, created_at, role, message_text; define retention before persisting |

## 3.5 Security and Privacy

- Keep API keys in environment variables or the host's secret manager; never expose them to browser code.
- Add file type and file size validation before parsing uploads.
- Do not log API keys, full private documents, or sensitive user content.
- Use only documents the user is entitled to upload; explain if content is sent to an external model provider.
- For a public demo, consider access controls or demo data so other visitors cannot view or overwrite personal records.
- Set explicit retention behavior for uploaded files, extracted text, and conversation history.

## 3.6 Deployment and Operational Constraints

- Pin dependencies in requirements.txt and test the same start command locally.
- Configure the Gemma provider key in Render environment settings.
- Test cold starts and API errors; free services may sleep after inactivity.
- Do not rely on the ephemeral filesystem for durable records or uploads.
- Do not rely on an in-process APScheduler job for guaranteed reminders on a sleeping/restarting free web service.
- Use a separate scheduled worker or external notification/scheduling service if reliable delivery is a must; check current pricing and free-tier limits first.
- Browser TTS may be simpler than an external TTS service and avoids extra API calls, but voice quality/support varies by device.

## 3.7 Testing Requirements

| **Test**               | **Expected result**                                                             |
| ---------------------- | ------------------------------------------------------------------------------- |
| AI happy path          | A general grammar question returns a relevant explanation and example.          |
| Follow-up              | A follow-up such as "give me two more examples" uses prior turn context.        |
| Missing API key        | App shows a configuration message without exposing secrets.                     |
| API failure/rate limit | App handles provider errors without crashing.                                   |
| Attendance persistence | Saved attendance remains after app restart when durable storage is configured.  |
| Reminder timing        | Local scheduler fires at the configured time and timezone in a controlled test. |
| Invalid upload (later) | Unsupported/oversized files are rejected with a useful message.                 |
| Voice unsupported      | Text chat still works and the UI explains the voice fallback.                   |
| Hosted cold start      | Deployed app recovers after sleeping and successfully makes a model request.    |

# 4\. Implementation Plan

## 4.1 Priority Rule

Build the smallest end-to-end vertical slice first. A working text AI teacher and stable dashboard are more valuable than many incomplete features. The timeline below follows the October 21–25, 2026 challenge window provided in the source context; adjust based on actual progress.

## 4.2 Four-day execution plan

| **Date** | **Focus**                 | **Deliverables**                                                                                     | **Exit criteria**                                                |
| -------- | ------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Oct 21   | Foundation                | Project structure, Streamlit navigation, dashboard, class settings, SQLite schema                    | App launches; class link and records render.                     |
| Oct 22   | AI teacher                | Gemma API client, prompt, chat UI, bounded conversation history, error handling                      | 10 test questions work; follow-up context works.                 |
| Oct 23   | Automation and polish     | Attendance UI, practice prompt/tongue twister, reminder prototype; optional document upload or voice | P0 works; at least one automation is demonstrable.               |
| Oct 24   | Deployment and submission | Render deployment, secrets, smoke tests, screenshots/demo, DEV article draft and publish             | Public demo works; limitations and open-AI rationale documented. |
| Oct 25   | Buffer / submit           | Final regression test, confirm post URL and required challenge tags/template                         | Submission completed before deadline.                            |

## 4.3 Suggested Repository Structure

```
speakeasy-ai/
├── app.py                  # Streamlit entry point
├── requirements.txt
├── .env.example            # Placeholder variable names only
├── .gitignore
├── README.md
├── services/
│   ├── gemma_client.py     # Hosted model API calls
│   ├── reminders.py        # Scheduling prototype
│   ├── storage.py          # SQLite operations
│   ├── documents.py        # Parsing/retrieval (later)
│   └── speech.py            # Optional voice helpers
├── pages/
│   ├── 1_Attendance.py
│   ├── 2_Materials.py
│   ├── 3_AI_Teacher.py
│   └── 4_Practice.py
└── tests/
    ├── test_storage.py
    └── test_teacher.py
```

## 4.4 Definition of Done

- The app starts locally from documented instructions.
- A user can view the dashboard and class link.
- Attendance can be recorded and retrieved.
- The AI teacher answers general questions using the configured Gemma API.
- Missing credentials and API failures are handled gracefully.
- The README explains setup, environment variables, architecture, limitations, and deployment.
- The deployed demo is smoke-tested and no secrets are committed.
- The DEV post explains the effort saved, the role of open-weight AI, what was actually implemented, and known limitations.

# 5\. Decisions and Open Questions

| **Decision / question** | **Current position**                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Model access            | Use a supported hosted Gemma API if the chosen model is available to the account and within quota; verify provider/model and current terms. |
| Notes-based teaching    | Not required for the first vertical slice; planned as an extension using retrieval.                                                         |
| Voice                   | Optional MVP enhancement: browser speech input and browser text-to-speech; full real-time voice is out of scope.                            |
| Reminder delivery       | Prototype with APScheduler locally; hosted reliable delivery requires a durable external/scheduled mechanism.                               |
| Data persistence        | SQLite locally; choose persistent disk or managed database before relying on hosted data.                                                   |
| Public access           | Decide whether the demo needs authentication before storing personal data.                                                                  |
| Submission proof        | Capture genuine screenshots/demo and describe only features that actually work.                                                             |

# 6\. Submission Story (Draft Outline)

- The problem: English practice and class organization are easy to postpone when tools are fragmented.
- The solution: a single companion for class tracking, practice prompts, and an AI English teacher.
- The lazy payoff: fewer things to remember and less setup before practicing.
- The AI approach: Gemma via a hosted API, with a clear explanation of what is open-weight and what remains provider-hosted.
- The demo: show a general grammar question, a follow-up, class/attendance workflow, and any reminder/voice feature that truly works.
- Limitations: model API availability/cost, Render cold starts and ephemeral storage, reminder reliability, and optional voice support.

Important: do not claim the app works offline if it relies on a hosted model API. Do not claim that all data stays local. State the exact model/provider and what runs on Render in the final article.
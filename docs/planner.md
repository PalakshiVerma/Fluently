# SpeakEasy AI — Project Planner

> **Purpose:** A practical, phase-by-phase implementation checklist for SpeakEasy AI.  
> **Target:** Hacktoberfest DEV Open-Source AI Challenge — Week 3  
> **Planning window:** 21–25 October 2026  
> **Stack direction:** Python, Streamlit, hosted Gemma API, SQLite, Render. Add document retrieval and voice only after the core app works.

## How to use this planner

- Work through phases in order.
- Finish and test a phase before starting the next one.
- Keep the MVP small; mark optional work as deferred if the deadline is at risk.
- Check tasks off only when they are implemented and tested.
- Never commit API keys, private notes, or `.env` files.

## Phase 0 — Scope and setup

**Goal:** Prepare a clean project and confirm the model/API path.

- [x] Create the project folder and initialize Git.
- [x] Create and activate a Python virtual environment.
- [x] Create `requirements.txt`.
- [x] Create `.gitignore` for `.env`, virtual environments, caches, local databases, uploads, and generated files.
- [x] Create `.env.example` with placeholder variable names only.
- [x] Choose and verify the exact hosted Gemma API/provider and model ID.
- [ ] Create an API key and store it in `.env` locally.
- [ ] Make one minimal Python API request and confirm a response.
- [x] Add a README with setup instructions and the project goal.

**Exit criteria:** A clean Python project can call the selected Gemma API without exposing the key.

## Phase 1 — Streamlit app skeleton

**Goal:** Make the application run and provide clear navigation.

- [ ] Create `app.py` as the Streamlit entry point.
- [ ] Add page/navigation structure for Dashboard, Attendance, AI Teacher, Materials, and Practice.
- [ ] Add a consistent page title and short project description.
- [ ] Add friendly loading and error states.
- [ ] Run the app locally and test each page.

**Exit criteria:** The app launches locally and navigation works, even if some pages are placeholders.

## Phase 2 — Data and persistence

**Goal:** Store class and practice information.

- [ ] Create `services/storage.py`.
- [ ] Initialize SQLite tables for class settings, attendance, practice tasks, and app settings.
- [ ] Add functions to create/read/update class details.
- [ ] Add functions to save and retrieve attendance.
- [ ] Add functions to save and retrieve practice-task completion.
- [ ] Handle empty database and first-run initialization.
- [ ] Test that records persist after restarting the app locally.

**Exit criteria:** Class settings, attendance, and task completion survive a local app restart.

## Phase 3 — Dashboard and attendance

**Goal:** Make the app useful before adding advanced AI features.

- [ ] Show the next configured class on the dashboard.
- [ ] Show the class date/time and a working class-link button.
- [ ] Show attendance summary and recent attendance records.
- [ ] Build a form to add/edit class details and join URL.
- [ ] Add Present/Absent attendance controls.
- [ ] Show today's practice checklist.
- [ ] Test normal and empty-data states.

**Exit criteria:** A user can configure a class, open its link, record attendance, and see the saved result.

## Phase 4 — AI Teacher (core AI feature)

**Goal:** Answer general English-learning questions conversationally using Gemma.

- [ ] Create `services/gemma_client.py`.
- [ ] Read the API key from an environment variable; never hard-code it.
- [ ] Add a clear system instruction: teach patiently, explain simply, provide examples, and correct misconceptions.
- [ ] Build a chat interface in Streamlit.
- [ ] Send user questions to the Gemma API.
- [ ] Display the answer with readable formatting.
- [ ] Preserve a bounded amount of recent conversation history for follow-up questions.
- [ ] Handle missing API key, API errors, rate limits, and timeouts.
- [ ] Test at least 10 questions: grammar, vocabulary, sentence correction, examples, and follow-ups.
- [ ] Check responses for usefulness and avoid claiming the model is always correct.

**Exit criteria:** The AI Teacher answers general questions and supports sensible follow-up turns.

## Phase 5 — Daily English Practice

**Goal:** Make it easy to practise every day.

- [ ] Create a Practice page.
- [ ] Display a daily speaking prompt.
- [ ] Display a tongue twister.
- [ ] Add a 10-minute speaking task.
- [ ] Allow the user to mark each task complete.
- [ ] Save completion status in SQLite.
- [ ] Add a simple progress summary.
- [ ] Test that tasks and completion status behave correctly across restarts.

**Exit criteria:** The user can see daily practice tasks, complete them, and review progress.

## Phase 6 — Reminders

**Goal:** Add scheduled reminders while being honest about hosting limitations.

- [ ] Confirm the user's preferred timezone and reminder times.
- [ ] Build a local APScheduler prototype.
- [ ] Schedule class reminders for 10 minutes before class.
- [ ] Schedule a daily speaking-practice reminder.
- [ ] Schedule a daily tongue-twister reminder, or combine both practice reminders if simpler.
- [ ] Test scheduling locally with a near-future test time.
- [ ] Decide how notifications reach the user; a scheduler alone does not send a notification.
- [ ] For hosted reminders, choose a durable external scheduler/notification service or a continuously running worker.
- [ ] Verify current Render free-tier and third-party service limits before relying on hosted delivery.
- [ ] Document that a sleeping/restarting free web service may miss in-process scheduled jobs.

**Exit criteria:** Local scheduling is tested and the hosted reminder strategy is explicitly chosen. Do not describe reminders as delivered until the notification channel is implemented and tested.

## Phase 7 — Materials Vault and notes-based Q&A (optional extension)

**Goal:** Upload learning documents and optionally ask questions grounded in their content.

- [ ] Add file upload for PDF, DOCX, and TXT.
- [ ] Validate allowed file types and file size.
- [ ] Extract text using PyMuPDF, python-docx, or a plain-text reader.
- [ ] Split extracted text into overlapping chunks.
- [ ] Select an embedding model and generate embeddings.
- [ ] Store chunks and metadata in ChromaDB.
- [ ] Retrieve relevant chunks for a question.
- [ ] Pass retrieved context to Gemma with instructions to stay grounded in the notes.
- [ ] Tell the user when the notes do not contain enough information.
- [ ] Display source filename or relevant passage where feasible.
- [ ] Test questions answered by the notes and questions not covered by the notes.
- [ ] Decide how uploaded files and vector data persist in deployment.

**Exit criteria:** A question about uploaded notes receives an answer grounded in retrieved passages. If time is short, defer this phase; the general AI Teacher does not depend on it.

## Phase 8 — Voice assistance (optional extension)

**Goal:** Add simple voice input/output, not a full real-time voice agent.

- [ ] Keep text chat fully usable without microphone permissions.
- [ ] Choose browser speech recognition or a speech-to-text API for voice input.
- [ ] Add a microphone/dictation control and display the recognized text before submission when practical.
- [ ] Choose browser `speechSynthesis` or a text-to-speech API for spoken answers.
- [ ] Add a play/stop control for reading the AI answer aloud.
- [ ] Handle unsupported browsers, denied microphone access, and transcription errors.
- [ ] Test on the target browser and at least one fallback path.
- [ ] Check external speech API quotas, costs, and privacy implications if used.

**Exit criteria:** A user can speak a question, submit the recognized text, and hear the answer, while text-only use still works.

## Phase 9 — Render deployment

**Goal:** Publish a working demo without running Gemma on Render.

- [ ] Confirm the app starts using the intended production command.
- [ ] Pin dependencies in `requirements.txt`.
- [ ] Push the project to a GitHub repository.
- [ ] Create a Render web service connected to the repository.
- [ ] Configure the start command (for example, `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`).
- [ ] Add the Gemma API key through Render environment settings.
- [ ] Confirm no secret is committed to Git.
- [ ] Test deployment from a cold start.
- [ ] Check logs for errors without printing secrets or user content.
- [ ] Choose durable storage for data that must survive restarts; Render's default filesystem is not durable.
- [ ] Verify free-tier limits, sleeping behavior, and any external service costs.
- [ ] Test the app from a second browser/session if it is public.

**Exit criteria:** The public URL loads and the core demo works after startup. Data persistence and reminder limitations are documented.

## Phase 10 — QA, demo, and submission

**Goal:** Make the project understandable, reproducible, and ready to show.

- [ ] Run through the full primary user journey.
- [ ] Test missing API key, model failure, empty data, and slow responses.
- [ ] Verify attendance persistence in the chosen deployment configuration.
- [ ] Verify that optional voice and reminders work before mentioning them in the article.
- [ ] Capture genuine screenshots of the running app.
- [ ] Record a short demo if time permits.
- [ ] Finish README: features, setup, environment variables, architecture, limitations, and demo link.
- [ ] Write the DEV article in your own words.
- [ ] Explain what open-weight AI contributes and what runs on an external API.
- [ ] Do not claim offline operation if the app depends on hosted APIs.
- [ ] Include the challenge's required tags/template, including `#devchallenge` and `#hf26challenge`, as applicable.
- [ ] Confirm the submission is published before the challenge deadline.

**Exit criteria:** The demo, repository, README, and published submission describe the features that actually work.

## Deadline-first MVP

If time becomes tight, complete these in order:

1. [ ] Streamlit app launches.
2. [ ] Dashboard shows the class link and basic task list.
3. [ ] Attendance can be saved.
4. [ ] Gemma-powered text AI Teacher works.
5. [ ] README and Render deployment work.
6. [ ] Add daily practice prompts.
7. [ ] Add reminders only if the delivery mechanism is reliable.
8. [ ] Add document retrieval and voice only after the above are stable.

## Definition of done

- [ ] A new developer can run the project using the README.
- [ ] Secrets are not in the repository.
- [ ] The AI Teacher can answer general English questions and follow-ups.
- [ ] Dashboard and attendance work.
- [ ] Any advertised reminders, document Q&A, or voice features have been tested.
- [ ] The hosted demo's storage, cold-start, and reminder limitations are documented.
- [ ] The submission accurately describes the model provider and the open-weight components used.

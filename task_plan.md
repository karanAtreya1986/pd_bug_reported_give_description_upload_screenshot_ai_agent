# 🗺️ Jira Ticket Pilot: Task Plan (task_plan.md)

## 🏁 Phase 0: Initialization (Current)
- [x] Create project memory files (`gemini.md`, `task_plan.md`, `findings.md`, `progress.md`)
- [x] Create directory structure (`architecture/`, `tools/`, `.tmp/`)
- [ ] Present Phase 1 Discovery Questions to user

---

## 🏗️ Phase 1: Blueprint (Vision & Logic)
- [x] Define North Star & Integrations
- [x] Finalize JSON Data Schema in `gemini.md`
- [ ] Research Jira API for attachment uploads
- [ ] Design UI High-Fidelity Mockup (Premium Aesthetics)
- [ ] Approve official "Blueprint" (Data Flow)

---

## ⚡ Phase 2: Link (Connectivity)
- [x] Set up `.env` with `JIRA_API_TOKEN`, `JIRA_EMAIL`, `JIRA_BASE_URL`, and `GROQ_API_KEY`
- [x] Build `tools/verify_groq.py` to test LLM connectivity
- [x] Build `tools/verify_jira.py` to test Jira API connectivity



---

## ⚙️ Phase 3: Architect (The 3-Layer Build)
- [ ] **Layer 1: Architecture**
    - [ ] Prompt Engineering SOP (Groq gpt-oss-120b)
    - [ ] Jira Payload Format SOP
- [ ] **Layer 2: Navigation**
    - [ ] Develop HTML/JS Frontend for Bug Reporting
    - [ ] Implement Image-to-Base64 handler
- [ ] **Layer 3: Tools**
    - [ ] `tools/process_bug_ai.py` (Groq Engine)
    - [ ] `tools/submit_jira_ticket.py` (Jira Engine)


---

## ✨ Phase 4: Stylize (Payload Refinement)
- [ ] Format Jira descriptions with Rich Text/Markdown
- [ ] Implement confirmation preview for the user

---

## 🛰️ Phase 5: Trigger (Deployment)
- [ ] Set up automation triggers (e.g., Slack to Jira or CLI)
- [ ] Final documentation hand-off

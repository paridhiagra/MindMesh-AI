<div align="center">

# 🧠 MindMesh AI

### *A self-healing, dual-agent AI system*

Hermes orchestrates. OpenClaw builds. Slack watches. Together, they heal what breaks.

![Status](https://img.shields.io/badge/status-in--development-orange?style=for-the-badge)
![CI](https://img.shields.io/github/actions/workflow/status/paridhiagra/MindMesh-AI/ci.yml?style=for-the-badge&label=CI)
![Python](https://img.shields.io/badge/python-3.11-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

</div>

---

## 🌌 Overview

**MindMesh AI** is an experimental self-healing multi-agent system that automates the full development loop — detect a broken build, diagnose the issue, fix it, and verify — with minimal human intervention.

Two agents work in tandem:

| Agent | Role | Responsibility |
|:--|:--|:--|
| 🧭 **Hermes** | Orchestrator | Monitors CI/CD, reads failure logs, issues fix instructions |
| 🛠️ **OpenClaw** | Builder | Executes fixes, writes/patches code, reports back |

Every decision and status update flows through **Slack**, making the entire loop observable in real time.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    CI["🔄 GitHub Actions CI"] -- "status" --> H["🧭 Hermes<br/>(Orchestrator)"]
    H -- "instructions" --> OC["🛠️ OpenClaw<br/>(Builder)"]
    OC -- "results" --> H
    OC --> SLACK["💬 Slack<br/>(#agent-main)"]

    style CI fill:#1f2937,stroke:#60a5fa,stroke-width:2px,color:#fff
    style H fill:#1f2937,stroke:#f59e0b,stroke-width:2px,color:#fff
    style OC fill:#1f2937,stroke:#34d399,stroke-width:2px,color:#fff
    style SLACK fill:#1f2937,stroke:#a78bfa,stroke-width:2px,color:#fff
```

</div>

---

## ✨ Features

- 🔍 **CI Monitoring** — polls GitHub Actions, detects pass/fail in real time
- 🩹 **Self-Healing Loop** — reads error logs and delegates fixes automatically
- 💬 **Slack Integration** — live updates, escalations, human-in-the-loop mentions
- ♻️ **Retry Policy** — configurable auto-retries before escalating to a human
- 📝 **Decision Logging** — every agent decision logged to `docs/decisions.md`

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|:--|:--|
| Language | Python |
| CI/CD | GitHub Actions |
| Messaging | Slack SDK |
| AI Engine | Groq (GPT-OSS 120B) + Ollama (Qwen2.5-Coder 7B) |
| Config | JSON + `.env` |
| Testing | Pytest |

</div>

## 🧠 Model Routing

Following the "expensive brain, cheap hands" pattern — a strong model plans, a fast/cheap model executes.

| Task | Agent | Model | Provider | Why |
|:--|:--|:--|:--|:--|
| Planning & task decomposition | Hermes (Orchestrator) | GPT-OSS 120B | Groq (cloud API) | Strong reasoning for breaking down tasks correctly the first time |
| Code execution & writing | OpenClaw (Builder) | Qwen2.5-Coder 7B | Ollama (local) | Runs fully offline, unlimited free usage, ideal for high-volume coding tasks |

This keeps cost at zero while maximizing plan quality: Groq's cloud model handles the rare, high-stakes orchestration calls, while the local Ollama model handles the repetitive execution work with no API limits.

---

## ♻️ Self-Improvement Loop

MindMesh AI doesn't just execute tasks once and stop — it closes the loop:

1. **Detect** — CI run fails or OpenClaw reports an error
2. **Diagnose** — Hermes reads the failure log and classifies the error type
3. **Fix** — Hermes issues a targeted instruction to OpenClaw based on the diagnosis
4. **Learn** — if the same error pattern reappears, Hermes reuses the fix instead of re-diagnosing from scratch, and logs it to `docs/decisions.md`

This means the system gets faster and more reliable across a session — the second time it hits a known failure, it doesn't need a human in the loop.

---

---

## 📁 Project Structure

```
MindMesh-AI/
├── .github/workflows/    # CI pipeline (ci.yml)
├── config/                # Agent configs (Hermes, OpenClaw)
├── scripts/                # Agent logic scripts
├── tests/                   # Test suite
├── docs/                     # Documentation & decision logs
├── requirements.txt
└── .env                      # Secrets (not committed)
```

---

## ⚙️ Setup & Installation

**1. Clone the repo**
```bash
git clone https://github.com/paridhiagra/MindMesh-AI.git
cd MindMesh-AI
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the root:

```
SLACK_BOT_TOKEN=xoxb-your-token
GITHUB_TOKEN=github_pat-your-token
SLACK_CHANNEL_AGENT_MAIN=#agent-main
SLACK_CHANNEL_AGENT_CODE=#agent-code
SLACK_CHANNEL_AGENT_MONITOR=#agent-monitor
```

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🚧 Roadmap

- [x] Project scaffolding & config
- [x] GitHub Actions CI pipeline
- [x] Hermes → GitHub API connection
- [ ] Hermes → Failure log analysis
- [ ] OpenClaw → Automated fix generation
- [ ] Full self-healing loop (detect → diagnose → fix → verify)
- [ ] Slack bi-directional control

---

<div align="center">

**Made with 🧩 by [paridhiagra](https://github.com/paridhiagra)**

</div>
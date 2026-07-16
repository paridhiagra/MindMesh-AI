# 🧠 MindMesh AI

A self-healing, dual-agent AI system where **Hermes** orchestrates and **OpenClaw** builds — connected through Slack, healing itself when things break.

![Status](https://img.shields.io/badge/status-in--development-yellow)
![CI](https://github.com/paridhiagra/MindMesh-AI/actions/workflows/ci.yml/badge.svg)

---

## 🌌 Overview

MindMesh AI is an experimental **self-healing multi-agent system** built to automate the full development loop — from detecting a broken build to diagnosing the issue and fixing it, with minimal human intervention.

Two agents work together:

| Agent | Role |
|-------|------|
| **Hermes** | The orchestrator — monitors CI/CD, detects failures, reads logs, and issues instructions |
| **OpenClaw** | The builder — receives instructions from Hermes and writes/fixes code accordingly |

All activity is streamed to **Slack**, so the whole loop is observable in real time.

---

## 🏗️ Architecture

GitHub Actions (CI)
│
▼
┌─────────┐      instructions      ┌───────────┐
│ Hermes  │ ───────────────────►   │ OpenClaw  │
│(orchestr│                        │ (builder) │
│  -ator) │ ◄───────────────────   │           │
└────┬────┘      results/status    └───────────┘
│
▼
Slack (#agent-main / #agent-monitor)

---

## ✨ Features

- 🔍 **CI Monitoring** — Hermes polls GitHub Actions and detects pass/fail status
- 🩹 **Self-Healing Loop** — On failure, Hermes reads error logs and delegates a fix to OpenClaw
- 💬 **Slack Integration** — Live updates, escalations, and human-in-the-loop mentions
- ♻️ **Retry Policy** — Configurable auto-retry attempts before escalating to a human
- 📝 **Decision Logging** — All agent decisions logged to `docs/decisions.md`

---

## 🛠️ Tech Stack

- **Language:** Python
- **CI/CD:** GitHub Actions
- **Messaging:** Slack SDK
- **AI:** Anthropic API
- **Config:** JSON + `.env`
- **Testing:** Pytest

---

## 📁 Project Structure

MindMesh-AI/
├── .github/workflows/     # CI pipeline (ci.yml)
├── config/                 # Agent configs (Hermes, OpenClaw)
├── scripts/                 # Agent logic scripts
├── tests/                   # Test suite
├── docs/                    # Documentation & decision logs
├── requirements.txt
└── .env                     # Secrets (not committed)

---

## ⚙️ Setup & Installation

1. **Clone the repo**
```bash
   git clone https://github.com/paridhiagra/MindMesh-AI.git
   cd MindMesh-AI
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Configure environment variables**
   Create a `.env` file in the root with:

    SLACK_BOT_TOKEN=xoxb-your-token
    GITHUB_TOKEN=github_pat-your-token
    SLACK_CHANNEL_AGENT_MAIN=#agent-main
    SLACK_CHANNEL_AGENT_CODE=#agent-code
    SLACK_CHANNEL_AGENT_MONITOR=#agent-monitor

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🚧 Roadmap

- [x] Project scaffolding & config
- [x] GitHub Actions CI pipeline
- [x] Hermes: GitHub API connection
- [ ] Hermes: Failure log analysis
- [ ] OpenClaw: Automated fix generation
- [ ] Full self-healing loop (detect → diagnose → fix → verify)
- [ ] Slack bi-directional control

---

## 📄 License

MIT
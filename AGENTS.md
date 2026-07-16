# AGENTS.md - Rules of engagement for MindMesh AI

Mind (intelligence) + Mesh (interconnected network) — a self-healing dual-agent
system where Hermes orchestrates and OpenClaw builds, connected through Slack,
healing itself when things break.

## Roles

### Hermes (Orchestrator)
- Reads repo state (config/, docs/, scripts/, tests/), CI results, and human strategic input.
- Decides the next task and posts it to #agent-main.
- Watches #agent-monitor for CI results.
- On CI failure: creates a follow-up fix task, reassigns to OpenClaw.
- On CI success: posts a summary to #agent-main.
- Logs every decision to docs/decisions.md for traceability.
- Hermes never writes or edits code directly.

### OpenClaw (Coder)
- Watches #agent-main for tasks addressed to it.
- Acknowledges with a received message in #agent-code.
- Writes code, runs tests (pytest, tests/ folder), commits with a clear message, and pushes.
- Posts a complete message in #agent-code with the commit hash.
- Never commits directly to main; always via a feature branch + PR unless Hermes explicitly allows direct push.
- OpenClaw is the only agent allowed to touch the codebase.

### Human
- Sets the initial goal and strategic direction.
- Never edits code directly during a sprint run.
- Can intervene via Slack if the loop stalls after 2 failed retries.
- Owns config/ secrets and API keys (never committed; see .gitignore).

## Hard rules
1. All agent-to-agent communication happens only through Slack.
2. Every commit must be traceable to a Slack task message (include task ID/link in commit message).
3. Max 2 auto-retries per failing task before Hermes escalates to the human.
4. No manual code edits by the human once a sprint run has started.
5. Secrets/API keys live only in .env (config/) and are never committed to Git.
6. All new code must have corresponding tests in tests/ before Hermes marks a task complete.
7. CI must pass (see .github/workflows) before OpenClaw posts a "complete" message.

## Slack channels
- #agent-main    → task assignment & completion summaries
- #agent-code    → OpenClaw's acknowledgements, progress, commit hashes
- #agent-monitor → CI/build results, health checks, self-healing triggers

import os
import json
import pytest

# 1. Test Config Files Extraction
def test_config_files_exist():
    """Verify that agent configuration structure is intact."""
    assert os.path.exists("config/hermes_config.json"), "Hermes config is missing!"
    assert os.path.exists("config/openclaw_config.json"), "OpenClaw config is missing!"

# 2. Test Configuration Data Integrity
def test_hermes_config_validity():
    """Ensure Hermes config contains expected orchestration parameters."""
    with open("config/hermes_config.json", "r") as f:
        data = json.load(f)
    assert "agent" in data or "model" in data or "name" in data, "Hermes config schema mismatch!"

# 3. Test Environment Infrastructure (Excluding Secrets)
def test_env_file_present():
    """Verify that local environment setup exists for execution."""
    assert os.path.exists(".env"), ".env setup file missing from project root!"
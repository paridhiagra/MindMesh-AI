import os
import requests
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

if github_token:
    print("✅ GitHub token loaded successfully!")
else:
    print("❌ GitHub token NOT found. Check your .env file.")


repo_owner = "paridhiagra"
repo_name = "MindMesh-AI"

url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"
headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    latest_run = response.json()["workflow_runs"][0]
    print(f"Latest run status: {latest_run['status']}")
    print(f"Conclusion: {latest_run['conclusion']}")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
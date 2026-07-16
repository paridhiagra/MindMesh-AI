import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

try:
    response = client.chat_postMessage(
        channel=os.environ["SLACK_CHANNEL_AGENT_MAIN"],
        text="✅ MindMesh AI bot connected successfully!"
    )
    print("Message sent:", response["ts"])
except SlackApiError as e:
    print("Error:", e.response["error"])
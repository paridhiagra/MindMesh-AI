import os
import json
from http.server import BaseHTTPRequestHandler

# Import your existing logic or rewrite a quick handler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Ek sample live response test framework ke liye
        response = {
            "status": "online",
            "message": "MindMesh AI Core Infrastructure is Live on Vercel!",
            "agents": ["Hermes", "OpenClaw"]
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
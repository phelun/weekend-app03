import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict, Tuple


def payload(path: str) -> Tuple[int, Dict[str, Any]]:
    if path == "/healthz":
        return 200, {"status": "healthy"}
    return 200, {
        "service": "app03",
        "secret_loaded": bool(os.getenv("API_KEY")),
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, response = payload(self.path)
        body = json.dumps(response).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

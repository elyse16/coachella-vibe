#!/usr/bin/env python3
"""
Coachella Vibe Code — Local Server
Run this script, then open http://127.0.0.1:8888 in your browser.
Press Ctrl+C to stop.
"""
import http.server
import os
import sys

PORT = 8888
HOST = "127.0.0.1"
APP_FILE = "coachella-vibe-code.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the main app for root and callback paths
        if self.path == "/" or self.path.startswith("/callback"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            
            # Read the HTML file
            app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), APP_FILE)
            with open(app_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()
    
    def log_message(self, format, *args):
        # Quieter logging
        if "/callback" in str(args[0]) or args[0] == "GET / ":
            print(f"  → {args[0]}")

if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════╗
║       🌴  COACHELLA VIBE CODE 2026  🌴       ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Server running at:                          ║
║  → http://127.0.0.1:{PORT}                     ║
║                                              ║
║  Open that URL in your browser.              ║
║  Make sure Spotify is open on any device.    ║
║  Press Ctrl+C to stop the server.            ║
║                                              ║
╚══════════════════════════════════════════════╝
""")
    
    try:
        with http.server.HTTPServer((HOST, PORT), Handler) as server:
            server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped. See you at Coachella! 🌵")
        sys.exit(0)

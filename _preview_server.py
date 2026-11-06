import http.server, os

ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def send_head(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path):
            self.path = "/index.html"   # SPA fallback, same as Netlify _redirects
        return super().send_head()
    def log_message(self, *a):
        pass

print("Preview running at  http://localhost:8080")
print("Press Ctrl+C to stop.")
http.server.ThreadingHTTPServer(("127.0.0.1", 8080), Handler).serve_forever()

from CCU_credentials import Server_Port

from http.server import BaseHTTPRequestHandler, HTTPServer
from jsonrpcserver import method, dispatch

@method
def ping():
    return "pong"

class TestHttpServer(BaseHTTPRequestHandler):
    def do_POST(self):
        # Process request
        request = self.rfile.read(int(self.headers["Content-Length"])).decode()
        response = dispatch(request.json())
        # Return response
        self.send_response(response.http_status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(str(response).encode())


if __name__ == "__main__":
    HTTPServer(("localhost", Server_Port), TestHttpServer).serve_forever()
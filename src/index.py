from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from calculator import calculate

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        query = urlparse(self.path)
        if (query.path.startswith("/calculate")):
            query_components = dict(qc.split("=") for qc in query.query.split("&"))
            req = query_components["req"]

            self.wfile.write(bytes("result: %s" % calculate(req), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
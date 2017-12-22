from http.server import BaseHTTPRequestHandler,HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        page_html = open("RestTestSum.html", "r").read()            
        s.wfile.write(page_html.encode())

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class(("127.0.0.1", 80), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    
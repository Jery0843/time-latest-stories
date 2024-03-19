import re
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request

class SimpleWebServer(BaseHTTPRequestHandler):

    def get_html_content(self):
        req = urllib.request.Request('https://time.com', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')

    def parse_stories(self, html_content):
        pattern = re.compile(r'<li class="latest-stories__item">\s*<a href="([^"]+)">\s*<h3 class="latest-stories__item-headline">([^<]+)</h3>', re.DOTALL)
        return pattern.findall(html_content)

    def do_GET(self):
        if self.path == '/latest-stories':
            html_content = self.get_html_content()
            matches = self.parse_stories(html_content)

            if matches:
                stories = [{"title": match[1].strip(), "link": f'https://time.com{match[0]}'} for match in matches[:6]]

                self.send_response(200)
                
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                self.wfile.write(json.dumps(stories, indent=4).encode('utf-8'))
            else:
                self.send_error(500, "Internal Server Error: Could not parse the stories")
        else:
            self.send_error(404)

port = 8000
httpd = HTTPServer(('', port), SimpleWebServer)
print(f"Server started on port {port}...")
httpd.serve_forever()

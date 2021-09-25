from http.server import BaseHTTPRequestHandler
from PIL import Image
import requests
from io import BytesIO

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'image/jpeg'
    self.end_headers()
    response = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/SOME_LIKE_IT_HOT_TITLE.jpg/800px-SOME_LIKE_IT_HOT_TITLE.jpg")
    img = Image.open(BytesIO(response.content))
    self.wfile.write(img)
    return

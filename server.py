from http.server import HTTPServer, SimpleHTTPRequestHandler, test, socketserver
import sys
from urllib.parse import urlparse
from urllib.parse import unquote
from pypresence import Presence # The simple rich presence client in pypresence
import time

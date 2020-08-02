"""Serve."""

from waitress import serve
from engine import wsgi


open('/tmp/app-initialized', 'w').close()

serve(wsgi.application, unix_socket='/tmp/nginx.socket')
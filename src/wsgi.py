from spyne.server.wsgi import WsgiApplication
from .app import application

# entrypoint for gunicorn
app = WsgiApplication(application)

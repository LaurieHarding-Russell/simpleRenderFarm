from flask import Flask
from render import renderApi
from client import clientPages
import subprocess

app = Flask(__name__)
app.register_blueprint(renderApi)
app.register_blueprint(clientPages)

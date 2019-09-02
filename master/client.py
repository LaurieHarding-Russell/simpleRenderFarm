from flask import Flask, Blueprint, render_template, send_from_directory
import subprocess

clientPages = Blueprint('', __name__,  template_folder='client')

@clientPages.route('/')
def client():
    return render_template("dist/client/index.html")

@clientPages.route('/<path:path>')
def serveFiles(path):
    print("********************************\n")
    print(path)
    print("********************************\n")
    return send_from_directory('client/dist/client/', path)

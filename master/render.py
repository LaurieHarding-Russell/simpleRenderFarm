from flask import Flask, Blueprint
import subprocess

renderApi = Blueprint('render', __name__)

@renderApi.route('/init', methods = ['POST'])
def initialize(frame):
    f = request.files['file']
    f.save(f.filename)

@renderApi.route('/render-frame/<filename>/<int:frame>')
def hello(filename, frame):
    f = request.files['file']
    f.save(filename)

    successful = returnderFrame(filename)
    if successful == 0:
        try:
            return send_file("test_" + frame)
        except Exception as e:
            abort(500, "failed to get file")
    abort(500, "the magic stuff didn't work")

def renderFrame(name, frame):
    return subprocess.call("blender", ["--background", name, "--render-output //test_" "--engine CYCLES", "--render-format PNG", "--use-extension 1", "--render-frame " + frame])

import subprocess
import glob
from flask import Blueprint, jsonify
import zipfile

renderApi = Blueprint('render', __name__)

@renderApi.route('/init', methods = ['POST'])
def initialize(frame):
    f = request.files['file']
    f.save(f.filename)

@renderApi.route('/scenes')
def getFiles():
    return jsonify(glob.glob("*.blend"))

@renderApi.route('/render-frame/<scene>/<int:start>/<int:end>')
def renderFrames(filename, frame):
    # TODO add support for splitting up process to slaves.
    for i in range(start, end):
        successful = renderFrame(scene, i)
        # assuming no problems :)
    return ":)"


# TODO, will save by scene at some point
@renderApi.route('/download/rendered')
def getRendered(filename, frame):
    zipFile = zipfile.ZipFile('rendered.zip', 'w', zipfile.ZIP_DEFLATED)
    zipDirectory('rendered', zipFile)
    zipf.close()
    try:
        return send_file("rendered.zip")
    except Exception as e:
        abort(500, "failed to get file")


def renderFrame(name, frame):
    return subprocess.call("blender", ["--background", name, "--render-output //render/render" "--engine CYCLES", "--render-format PNG", "--use-extension 1", "--render-frame " + frame])

def zipDirectory(path, zipFile):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            zipFile.write(os.path.join(root, file))

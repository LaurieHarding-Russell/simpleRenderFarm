import os
import tempfile
import pytest
import flask
from flaskr import flaskr'

from zipfile import ZipFile

@pytest.fixture
def client():
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()

    with flaskr.app.app_context():
        flaskr.init_db()

    yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])


def initAndRender(client):
    client.post('/init', test.blend)
    client.get('/render-frame/test.blend/1/1', test.blend)
    zip = client.get('/download/rendered')

    with ZipFile('sampleDir.zip', 'r') as zipObj:
        listOfFileNames = zipObj.namelist()
        print(listOfFileNames)

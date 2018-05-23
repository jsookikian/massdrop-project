import json
import unittest

from src.server import app

TEST_DB = 'test.db'


class FlaskTestClient(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['REMOTE_ADDR'] = environ.get('REMOTE_ADDR', '127.0.0.1')
        environ['HTTP_USER_AGENT'] = environ.get('HTTP_USER_AGENT', 'Chrome')
        return self.app(environ, start_response)


app.wsgi_app = FlaskTestClient(app.wsgi_app)
client = app.test_client()
client.post('/newJob',
            data=json.dumps({
                'url':"google.com"
            }))


if __name__ == "__main__":
    unittest.main()
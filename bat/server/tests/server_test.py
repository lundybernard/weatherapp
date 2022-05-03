from unittest import TestCase
from unittest.mock import patch

from ..server import (
    app,
    start_server,
    start_api_server,
)


SRC = 'bat.server.server'


class TestFlaskApp(TestCase):

    def setUp(t):
        t.client = app.test_client()

    def test_get_root(t):
        res = t.client.get('/')
        t.assertEqual(res.status_code, 200)
        t.assertEqual(
            res.get_data(as_text=True),
            'Hello World!'
        )

    def test_get_temperature(t):
        res = t.client.get('/temperature')
        t.assertEqual(
            res.get_data(as_text=True),
            '+ VALID +'
        )

    def test_get_presure(t):
        res = t.client.get('/presure')
        t.assertEqual(
            res.get_data(as_text=True),
            '+ VALID +'
        )

    def test_get_wind(t):
        res = t.client.get('/wind')
        t.assertEqual(
            res.get_data(as_text=True),
            '+ VALID +'
        )


class TestServer(TestCase):

    @patch(f'{SRC}.app', autospec=True)
    def test_start_server(t, app):
        start_server()
        app.run.assert_called_with(host='0.0.0.0', port='5000', debug=True)

    @patch(f'{SRC}.connexion')
    def test_start_api_server(t, connexion):
        start_api_server()
        connexion.FlaskApp.assert_called_with(
            'bat.server.server', specification_dir='../api/'
        )
        app = connexion.FlaskApp.return_value
        app.run.assert_called_with(host='0.0.0.0', port='5000', debug=True)

from unittest import TestCase
from unittest.mock import patch, Mock

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

    @patch(f'{SRC}.get_temperature', autospec=True)
    def test_get_temperature(t, get_temperature: Mock) -> None:
        location_id = 'loc1'
        get_temperature.return_value = 'temperature value'

        res = t.client.get(f'/temperature/{location_id}')

        get_temperature.assert_called_with(location_id)
        t.assertEqual(
            res.get_data(as_text=True),
            get_temperature.return_value
        )

    @patch(f'{SRC}.get_presure', autospec=True)
    def test_get_presure(t, get_presure: Mock) -> None:
        location_id = 'loc1'
        get_presure.return_value = 'presure value'

        res = t.client.get('/presure/loc1')

        get_presure.assert_called_with(location_id)
        t.assertEqual(
            res.get_data(as_text=True),
            get_presure.return_value
        )

    @patch(f'{SRC}.get_wind', autospec=True)
    def test_get_wind(t, get_wind: Mock) -> None:
        location_id = 'loc1'
        get_wind.return_value = 'wind value'

        res = t.client.get('/wind/loc1')

        get_wind.assert_called_with(location_id)
        t.assertEqual(
            res.get_data(as_text=True),
            get_wind.return_value
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

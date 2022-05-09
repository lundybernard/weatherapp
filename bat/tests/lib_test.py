from unittest import TestCase
from unittest.mock import patch

from bat.lib import (
    get_temperature,
    get_presure,
    get_wind,
    hello_world,
)


SRC = 'bat.lib'


class LibTests(TestCase):

    def setUp(t):
        patches = ['NOAAClient', ]
        for target in patches:
            patcher = patch(f'{SRC}.{target}', autospec=True)
            setattr(t, target, patcher.start())
            t.addCleanup(patcher.stop)

        t.noaa_client = t.NOAAClient.from_config.return_value

    def test_hello_world(t):
        ret = hello_world()
        t.assertEqual(ret, 'Hello World!')

    def test_get_temperature(t):
        t.noaa_client.temperature = 'temperature value'
        ret = get_temperature(location='location-id')
        t.assertEqual(ret, t.noaa_client.temperature)

    def test_get_presure(t):
        t.noaa_client.presure = 'presure value'
        ret = get_presure(location='location-id')
        t.assertEqual(ret, t.noaa_client.presure)

    def test_get_wind(t):
        t.noaa_client.wind = 'wind value'
        ret = get_wind(location='location-id')
        t.assertEqual(ret, t.noaa_client.wind)

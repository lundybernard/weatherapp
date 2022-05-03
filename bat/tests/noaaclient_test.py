from unittest import TestCase
from unittest.mock import patch, Mock

from ..noaaclient import (
    Config,
    NOAAClient,
)

from ._data import RECORD_AABP


SRC = 'bat.noaaclient'


class ConfigTests(TestCase):

    def test_config(t) -> None:
        location = 'location-key'
        source = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded/'

        conf = Config(
            location=location,
            source=source,
        )

        t.assertEqual(location, conf.location)
        t.assertEqual(source, conf.source)


class NOAAClientTests(TestCase):
    requests: Mock

    def setUp(t) -> None:
        patches = ['requests', ]
        for target in patches:
            patcher = patch(f'{SRC}.{target}', autospec=True)
            setattr(t, target, patcher.start())
            t.addCleanup(patcher.stop)

        t.response = t.requests.get.return_value
        t.response.text = RECORD_AABP

        t.location = 'location-key'
        t.source = 'https://unittest.nws.noaa.gov/tests/'
        t.config = Config(
            location=t.location,
            source=t.source,
        )

        t.noaa = NOAAClient.from_config(t.config)

    # Public Interface

    def test___init__(t) -> None:
        noaa = NOAAClient(t.location, t.source)
        t.assertEqual(noaa.location, t.location)
        t.assertEqual(noaa.source, t.source)
        t.assertIsInstance(noaa, NOAAClient)

    def test_from_config(t) -> None:
        noaa = NOAAClient.from_config(t.config)
        t.assertEqual(noaa.location, t.config.location)
        t.assertEqual(noaa.source, t.config.source)
        t.assertIsInstance(noaa, NOAAClient)

    def test_temperature(t) -> None:
        ret = t.noaa.temperature
        t.assertEqual(ret, '75 F (24 C)')

    def test_presure(t) -> None:
        ret = t.noaa.presure
        t.assertEqual(ret, '29.77 in. Hg (1008 hPa)')

    def test_wind(t) -> None:
        ret = t.noaa.wind
        t.assertEqual(ret, 'from the W (270 degrees) at 10 MPH (9 KT):0')

    # Private Properties

    def test__record(t) -> None:
        t.noaa.location = 'AABP'

        ret = t.noaa._record

        t.requests.get.assert_called_with(
            f'{t.noaa.source}{t.noaa.location}.TXT'
        )
        t.assertEqual(ret, RECORD_AABP)

    def test__record_url(t) -> None:
        location = 'AABP'
        t.noaa.location = location
        ret = t.noaa._record_url
        t.assertEqual(ret, f'{t.noaa.source}{location}.TXT')

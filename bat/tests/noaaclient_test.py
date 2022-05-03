from unittest import TestCase
from unittest.mock import patch, Mock, sentinel

from ..noaaclient import (
    Config,
    NOAAClient,
)


SRC = 'bat.noaaclient'


class ConfigTests(TestCase):

    def test_config(t) -> None:
        location = 'location-key'

        conf = Config(
            location=location,
        )

        t.assertEqual(location, conf.location)


class NOAAClientTests(TestCase):
    storage: Mock
    storage_client: Mock
    Credentials: Mock
    auth: Mock

    def setUp(t) -> None:
        patches = []
        for target in patches:
            patcher = patch(f'{SRC}.{target}', autospec=True)
            setattr(t, target, patcher.start())
            t.addCleanup(patcher.stop)

        t.location = 'location-key'
        t.config = Config(
            location=t.location,
        )

        t.noaa = NOAAClient.from_config(t.config)

    # Public Interface

    def test___init__(t) -> None:
        c = NOAAClient(t.location)
        t.assertEqual(c.location, t.location)
        t.assertIsInstance(c, NOAAClient)

    def test_from_config(t) -> None:
        c = NOAAClient.from_config(t.config)
        t.assertEqual(c.location, t.config.location)
        t.assertIsInstance(c, NOAAClient)

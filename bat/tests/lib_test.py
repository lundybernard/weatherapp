from unittest import TestCase

from bat.lib import (
    get_temperature,
    get_presure,
    get_wind,
    hello_world,
)


class LibTests(TestCase):

    def test_hello_world(t):
        ret = hello_world()
        t.assertEqual(ret, 'Hello World!')

    def test_get_temperature(t):
        ret = get_temperature()
        t.assertEqual(ret, '+ VALID OUTPUT +')

    def test_get_presure(t):
        ret = get_presure()
        t.assertEqual(ret, '+ VALID OUTPUT +')

    def test_get_wind(t):
        ret = get_wind()
        t.assertEqual(ret, '+ VALID OUTPUT +')

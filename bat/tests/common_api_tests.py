import requests

PT_SVC_ADDR = 'http://0.0.0.0:5000/'


class CommonAPITest(object):
    '''Define the API tests in their own inheritable class
    so they may be reused in multiple test cases.
    This was done to allow testing of the api in a container
    and as local service.
    '''

    def setUp(t):
        t.location = 'AABP'

    def test_api_hello_world(t):
        print('test_api_hello_world')
        url = f'{t.service_address}'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(out.text, 'Hello World!')

    def test_api_temperature(t):
        print('test_api_temperature')
        url = f'{t.service_address}temperature/{t.location}'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(
            out.text,
            '75 F (24 C)',  # these values may need to be regex matches
        )

    def test_api_presure(t):
        print('test_api_presure')
        url = f'{t.service_address}presure/{t.location}'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(
            out.text,
            '29.77 in. Hg (1008 hPa)',
        )

    def test_api_wind(t):
        print('test_api_wind')
        url = f'{t.service_address}wind/{t.location}'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(
            out.text,
            'from the W (270 degrees) at 10 MPH (9 KT):0',
        )

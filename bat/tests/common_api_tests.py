import requests

PT_SVC_ADDR = 'http://0.0.0.0:5000/'


class CommonAPITest(object):
    '''Define the API tests in their own inheritable class
    so they may be reused in multiple test cases.
    This was done to allow testing of the api in a container
    and as local service.
    '''

    def test_api_hello_world(t):
        print('test_api_hello_world')
        url = f'{t.service_address}hello_world'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(out.text, '"Hello World!"\n')

    def test_api_temperature(t):
        print('test_api_temperature')
        url = f'{t.service_address}temperature'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(out.text, '"+ VALID OUTPUT +"\n')

    def test_api_presure(t):
        print('test_api_presure')
        url = f'{t.service_address}presure'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(out.text, '"+ VALID OUTPUT +"\n')

    def test_api_wind(t):
        print('test_api_wind')
        url = f'{t.service_address}wind'
        print(f'connect to service at {url}')
        out = requests.get(url, verify=False)
        t.assertEqual(out.text, '"+ VALID OUTPUT +"\n')

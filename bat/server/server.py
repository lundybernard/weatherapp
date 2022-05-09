from flask import Flask
import connexion

from bat.lib import (
    get_temperature,
    get_presure,
    get_wind,
    hello_world,
)

app = Flask(__name__)


@app.route('/')
def hello_api():
    return hello_world()


# TODO: Refactor into a single route that accepts location and value parameters
@app.route('/temperature/<location>')
def temperature_api(location: str = None) -> str:
    return get_temperature(location)


@app.route('/presure/<location>')
def presure_api(location: str = None) -> str:
    return get_presure(location)


@app.route('/wind/<location>')
def wind_api(location: str = None) -> str:
    return get_wind(location)


def start_server(host='0.0.0.0', port='5000', debug=True):
    app.run(host=host, port=port, debug=debug)


def start_api_server(host='0.0.0.0', port='5000', debug=True):
    '''Start a Swagger API server using connexion to generate the routes from
    the api.yaml file
    '''
    app = connexion.FlaskApp(__name__, specification_dir='../api/')
    app.add_api('api.yaml')
    app.run(host=host, port=port, debug=debug)

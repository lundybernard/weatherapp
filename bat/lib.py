from .noaaclient import NOAAClient

from .conf import get_config


def hello_world():
    return 'Hello World!'


def get_temperature():
    return "dummy temperature value"


def get_presure(location: str):
    '''WIP: config bug causing default noaaclient.source to return None
    '''
    cfg = get_config()
    noaa = NOAAClient(cfg.noaaclient)

    noaa.location = location
    return noaa.presure


def get_wind():
    raise NotImplementedError

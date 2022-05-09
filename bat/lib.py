from .noaaclient import NOAAClient

from .conf import get_config


def hello_world():
    return 'Hello World!'


def get_temperature(location: str):
    cfg = get_config()
    cfg.noaaclient.location = location
    noaa = NOAAClient.from_config(cfg.noaaclient)
    return noaa.temperature


def get_presure(location: str):
    '''WIP: config bug causing default noaaclient.source to return None
    '''
    cfg = get_config()
    cfg.noaaclient.location = location
    noaa = NOAAClient.from_config(cfg.noaaclient)
    return noaa.presure


def get_wind(location: str):
    cfg = get_config()
    cfg.noaaclient.location = location
    noaa = NOAAClient.from_config(cfg.noaaclient)
    return noaa.wind

from dataclasses import dataclass

import requests
import re


@dataclass
class Config:
    location: str = None
    source: str = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded/'


class NOAAClient:
    location: str
    source: str
    __record: str

    def __init__(self, location: str = None, source: str = None):
        self.location = location
        self.source = source

    @classmethod
    def from_config(cls, conf: Config) -> 'NOAAClient':
        return cls(conf.location, conf.source)

    @property
    def temperature(self) -> str:
        # TODO: Refactor, Room for improvement
        return re.findall(r'Temperature: ([^\n]+)', self._record)[0]

    @property
    def presure(self) -> str:
        # TODO: Refactor, Room for improvement
        return re.findall(r'Pressure \(altimeter\): ([^\n]+)', self._record)[0]

    @property
    def wind(self) -> str:
        # TODO: Refactor, Room for improvement
        return re.findall(r'Wind: ([^\n]+)', self._record)[0]

    @property
    def _record(self) -> str:
        '''This may need some cashing logic to update only when needed
        '''
        try:
            return self.__record
        except AttributeError:
            ret = requests.get(self._record_url)
            # TODO: we should validate the response here
            self.__record = ret.text
            return self.__record

    @property
    def _record_url(self) -> str:
        return f'{self.source}{self.location}.TXT'

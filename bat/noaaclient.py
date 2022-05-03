from dataclasses import dataclass


@dataclass
class Config:
    location: str = None


class NOAAClient:
    location: str

    def __init__(self, location: str = None):
        self.location = location

    @classmethod
    def from_config(cls, conf: Config) -> 'NOAAClient':
        return cls(conf.location)

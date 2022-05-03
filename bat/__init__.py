from dataclasses import dataclass

from .example import Config
from .noaaclient import Config as noaaclient_config


@dataclass
class GlobalConfig:
    # example module with configuration dataclass
    example: Config
    noaaclient: noaaclient_config

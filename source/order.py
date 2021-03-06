from typing import NamedTuple

from source.metadata import Metadata
from source.protocols import BaseProtocol


class Order(NamedTuple):
    data: str
    metadata: Metadata = None

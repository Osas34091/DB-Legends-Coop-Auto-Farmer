from typing import NamedTuple, Union

class ImageMatch(NamedTuple):
    found: bool
    x: Union[int, None]
    y: Union[int, None]

class DualImageMatch(NamedTuple):
    which_found: int
    x: Union[int, None]
    y: Union[int, None]
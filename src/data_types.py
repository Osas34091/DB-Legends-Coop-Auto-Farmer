# ==========================================================
# Proyecto: DB Legends Co-Op Auto Farmer
# Autor: Osas34091
# Repositorio: https://github.com/Osas34091/DB-Legends-Coop-Auto-Farmer
# ==========================================================

from typing import NamedTuple, Union

class ImageMatch(NamedTuple):
    found: bool
    x: Union[int, None]
    y: Union[int, None]

class DualImageMatch(NamedTuple):
    which_found: int
    x: Union[int, None]
    y: Union[int, None]

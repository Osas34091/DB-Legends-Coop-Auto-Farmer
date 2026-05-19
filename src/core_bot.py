from adbutils._device import AdbDevice
import time
import numpy as np
from .vision import VisionScanner
from .helpers import log_activity

class AndroidController:
    def __init__(self, device: AdbDevice, debug_mode: bool = False):
        self.device = device
        self.debug_mode = debug_mode
        self.scanner = VisionScanner()

    def capture_screen_to_ram(self):
        """Toma captura directo a memoria sin guardar en disco."""
        return np.array(self.device.screenshot().convert("RGB"), dtype=np.uint8)

    def tap_screen(self, x: int, y: int):
        self.device.click(x, y)
# ==========================================================
# Proyecto: DB Legends Co-Op Auto Farmer
# Autor: Osas34091
# Repositorio: https://github.com/Osas34091/DB-Legends-Coop-Auto-Farmer
# ==========================================================

import cv2
import numpy as np
import pytesseract
from .data_types import ImageMatch, DualImageMatch

class VisionScanner:
    def __init__(self):
        self.cached_scale = 1.0

    def read_text_from_image(self, image, cords: tuple, ocr_config="--psm 7") -> str | None:
        cropped = image.crop(cords)
        gray = cropped.convert("L")
        thresh = cv2.threshold(
            np.array(gray), 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV
        )[1]
        try:
            return pytesseract.image_to_string(thresh, config=ocr_config).strip()
        except Exception as e:
            print(f"Error de OCR: {e}")
            return None

    def locate_image_multiscale(self, template_path: str, screenshot, threshold=0.8) -> ImageMatch:
        """Busca una imagen adaptándose al tamaño de la pantalla del celular."""
        target_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path)
        
        if template is None:
            print(f"[-] No se encontró la imagen en ruta: {template_path}")
            return ImageMatch(False, None, None)
            
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        found, x, y = self._evaluate_scale(template_gray, target_gray, self.cached_scale, threshold)
        if found:
            return ImageMatch(True, x, y)

        scales = np.linspace(0.7, 1.4, 8)
        for scale in scales:
            if scale == self.cached_scale:
                continue
            found, x, y = self._evaluate_scale(template_gray, target_gray, scale, threshold)
            if found:
                self.cached_scale = scale
                return ImageMatch(True, x, y)
                
        return ImageMatch(False, None, None)

    def _evaluate_scale(self, template_gray, target_gray, scale, threshold):
        width = int(template_gray.shape[1] * scale)
        height = int(template_gray.shape[0] * scale)

        if width > target_gray.shape[1] or height > target_gray.shape[0] or width < 10 or height < 10:
            return False, None, None

        resized = cv2.resize(template_gray, (width, height))
        result = cv2.matchTemplate(target_gray, resized, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            center_x = max_loc[0] + width // 2
            center_y = max_loc[1] + height // 2
            return True, center_x, center_y
            
        return False, None, None

    def locate_all_cards(self, template_path: str, screenshot, threshold=0.55):
        """Busca TODAS las cartas en pantalla a su tamaño original (escala 1.0)."""
        target_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path)
        
        if template is None:
            return []
            
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        
        result = cv2.matchTemplate(target_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        
        locations = np.where(result >= threshold)
        
        points = []
        h, w = template_gray.shape
        
        for pt in zip(*locations[::-1]):
            center_x = pt[0] + w // 2
            center_y = pt[1] + h // 2
            
            too_close = False
            for p in points:
                if abs(p[0] - center_x) < 50 and abs(p[1] - center_y) < 50:
                    too_close = True
                    break
            
            if not too_close:
                points.append((center_x, center_y))
                
        return points

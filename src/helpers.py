# ==========================================================
# Proyecto: DB Legends Co-Op Auto Farmer
# Autor: Osas34091
# Repositorio: https://github.com/Osas34091/DB-Legends-Coop-Auto-Farmer
# ==========================================================

from datetime import datetime
from functools import wraps
import time

def log_activity(message: str):
    """Guarda un registro de la actividad o errores del bot."""
    with open("bot_log.txt", "a") as log_file:
        log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def auto_retry(retries=3, wait_time=2):
    """Decorador para reintentar acciones en caso de fallos temporales."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = retries
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    log_activity(f"Fallo en {func.__name__}: {str(e)}. Reintentando...")
                    time.sleep(wait_time)
                    attempts -= 1
            return False
        return wrapper
    return decorator

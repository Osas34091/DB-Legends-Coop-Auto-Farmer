import sys
from adbutils import adb
from src.legends_coop import LegendsCoopBot

def print_banner():
    print("""
    =============================================
           DRAGON BALL LEGENDS - AUTO CO-OP
    =============================================
         Desarrollado por: Osas34091
           Versión 1.0 | GitHub: Osas34091
    =============================================
    """)
 

if __name__ == "__main__":
    print_banner()
    
    if "farm" in sys.argv:
        debug_active = "--debug" in sys.argv
        
        try:
            device = adb.device()
            bot = LegendsCoopBot(device, debug_mode=debug_active)
            bot.start_farming_loop()
        except Exception as e:
            print(f"[-] Error crítico al iniciar: {e}")
            print("[!] Verifica que tu celular esté conectado con Depuración USB activa.")
    else:
        print("Uso correcto: python main.py farm")
        print("Argumentos extra: --debug (muestra logs en consola)")

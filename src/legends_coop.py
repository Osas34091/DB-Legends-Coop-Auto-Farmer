import os
import time
import random
from .core_bot import AndroidController

class LegendsCoopBot(AndroidController):
    def __init__(self, device, debug_mode=False):
        super().__init__(device, debug_mode)
        print("[+] Conexión ADB exitosa. Iniciando motor de DB Legends...")
        self.cards = [
            "./Images/Strike_Card_Image.png",
            "./Images/Blast_Card_Image.png",
            "./Images/Green_Card_Image.png",
            "./Images/Special_Card_Image.png"
        ]
        self.in_combat = False 

    def humanized_tap(self, center_x, center_y, radius=15):
        """Simula toques humanos con variación de posición y clics múltiples."""
        target_x = int(center_x + random.randint(-radius, radius))
        target_y = int(center_y + random.randint(-radius, radius))

        taps = 1
        
        if self.debug_mode:
            print(f"[*] Clic Humano -> ({target_x}, {target_y})")
            
        for i in range(taps):
            self.tap_screen(target_x, target_y)
            if taps > 1 and i == 0:
                time.sleep(random.uniform(0.02, 0.08)) 

    def play_random_arts_card(self, screenshot) -> bool:
        """Escanea TODAS las cartas y presiona aleatoriamente sin clics fantasma."""
        found_cards = []

        for card_path in self.cards:
            matches = self.scanner.locate_all_cards(card_path, screenshot, threshold=0.55)
            for match in matches:
                found_cards.append(match)

        if found_cards:
            random.shuffle(found_cards)
            
            min_x_clicked = float('inf') 
            
            for (x, y) in found_cards:
                if x < min_x_clicked:
                    self.humanized_tap(x, y, radius=20)
                    min_x_clicked = x  
                    time.sleep(random.uniform(0.05, 0.15)) 
            
            return True
            
        return False

    def start_farming_loop(self):
        """Máquina de estados principal para farmear Co-op de forma infinita."""
        print("\n[*] Bot activo. Esperando en el Lobby de Co-op...")
        
        while True:
            screen = self.capture_screen_to_ram()

            if self.in_combat:
                match = self.scanner.locate_image_multiscale("./Images/Victory_Coop_Screen_Text.png", screen, 0.75)
                if match.found:
                    print("-> Pantalla detectada: ¡VICTORIA! Saliendo de fase de combate...")
                    self.in_combat = False 
                    w, h = self.device.window_size()
                    time.sleep(0.5) 
                    continue
                
                card_played = self.play_random_arts_card(screen)
                
                if not card_played:
                    time.sleep(0.05) 
                
                continue 

            
            match = self.scanner.locate_image_multiscale("./Images/Retry_Coop_Again_Screen_Text.png", screen, 0.8)
            if match.found:
                print("-> Pantalla detectada: Solicitando 'Volver a desafiar'...")
                self.humanized_tap(match.x, match.y, radius=80)
                time.sleep(0.8) 
                continue

            match = self.scanner.locate_image_multiscale("./Images/Confirm_Retry_Coop_Again_Screen_Text.png", screen, 0.8)
            if match.found:
                print("-> Pantalla detectada: Confirmando revancha (Sí)...")
                self.humanized_tap(match.x, match.y, radius=60)
                os.system("cls" if os.name == "nt" else "clear")
                print("=============================================")
                print("[+] Ciclo finalizado. Buscando nueva partida.")
                print("=============================================")
                time.sleep(1.0) 
                continue

            match = self.scanner.locate_image_multiscale("./Images/Ready_Friend_Screen_Button.png", screen, 0.8)
            if match.found:
                print("-> Pantalla detectada: Confirmando preparación (Listo)...")
                self.humanized_tap(match.x, match.y, radius=80)
                time.sleep(0.8) 
                continue

            match = self.scanner.locate_image_multiscale("./Images/Waiting_Loading_Coop_Screen_Text.png", screen, 0.8)
            if match.found:
                print("-> Pantalla detectada: Buscando/Esperando (Espera...)\r", end="")
                time.sleep(0.2) 
                continue

            match = self.scanner.locate_image_multiscale("./Images/Ready_Loading_Coop_Screen_Text.png", screen, 0.8)
            if match.found:
                print("\n-> Pantalla detectada: Partida encontrada. Cargando arena (Listo)...")
                self.in_combat = True 
                time.sleep(0.2) 
                continue
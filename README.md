# 🐉 DB Legends Co-op Farming Bot

Script de automatización inteligente y universal para farmear de manera infinita el modo Hyperdimensional Co-op en Dragon Ball Legends mediante Python y ADB.

## ⚙️ Requisitos e Instalación

1. **Activar Depuración USB:** En tu teléfono Android, ve a Ajustes > Opciones de Desarrollador y activa la "Depuración USB".
2. **Conexión:** Conecta el dispositivo a la PC mediante cable USB (Asegúrate de aceptar el mensaje de permiso que saldrá en la pantalla del celular al conectarlo).
3. **Instalar Dependencias:** Abre una terminal o consola de comandos dentro de la carpeta de este proyecto y ejecuta:
   pip install -r requirements.txt

---

## 🎮 Instrucciones de Uso

1. Abre **Dragon Ball Legends** en tu dispositivo.
2. Entra al modo de **Hyperdimensional Co-op** y selecciona la dificultad que deseas farmear.
3. Quédate dentro de la pantalla del Lobby de espera (donde aparece el botón amarillo para buscar miembros o donde ya estás listo con tu compañero).
4. Abre la terminal de tu PC y ejecuta el siguiente comando:
   
   python main.py farm

## 🛡️ Características de Seguridad Humana
* El bot no usa clics en coordenadas fijas fijadas en código; calcula zonas dinámicas usando OpenCV.
* Incorpora variaciones de toque en ubicaciones píxel por píxel aleatorias para evitar detecciones de patrones repetitivos en los servidores de Bandai.
* Alterna tiempos de respuesta aleatorios entre toques emulando retrasos de impaciencia humana.
* Cuenta con detección inteligente multiescala, lo que significa que tus amigos lo pueden usar sin importar la marca, modelo o resolución de pantalla de sus celulares.

"""
Módulo de automatización de tareas
"""
import os
from datetime import datetime

class Automatizador:
    @staticmethod
    def crear_carpeta(ruta):
        """Crea una carpeta si no existe"""
        if not os.path.exists(ruta):
            os.makedirs(ruta)
            return f"Carpeta {ruta} creada ✅"
        return f"Carpeta {ruta} ya existe"

    @staticmethod
    def registrar_actividad(mensaje):
        """Registra actividad con fecha y hora"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{fecha}] {mensaje}\n"
        with open("actividad.log", "a", encoding="utf-8") as f:
            f.write(linea)
        return linea
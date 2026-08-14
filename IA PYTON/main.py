"""
IA-Automation-Scripts
Lectura, limpieza y BÚSQUEDA en base de datos CSV
"""
from config import PROYECTO_NOMBRE, VERSION
from modules.text_processor import ProcesadorTexto
from modules.automation import Automatizador
import pandas as pd

def main():
    print(f"🚀 {PROYECTO_NOMBRE} - Versión {VERSION}")
    print("=" * 70)

    auto = Automatizador()
    print(auto.crear_carpeta("resultados"))
    print(auto.registrar_actividad("Inicio del programa"))

    # --- 1. LEER BASE DE DATOS ---
    archivo_csv = "ai_companion_dependency_dataset.csv"
    print(f"\n📂 Leyendo: {archivo_csv}")
    
    try:
        datos = pd.read_csv(archivo_csv)
        filas, cols = datos.shape
        print(f"✅ Datos cargados: {filas} registros y {cols} columnas")

        # --- 2. LIMPIAR ---
        datos_limpios = datos.dropna()
        print(f"✅ Datos limpios: {datos_limpios.shape[0]} registros listos")

        # --- 3. MOSTRAR COLUMNAS DISPONIBLES ---
        print("\n📋 Columnas encontradas:")
        for i, nombre in enumerate(datos.columns):
            print(f"   {i+1}. {nombre}")

        # --- 4. 🔍 BUSCADOR ---
        print("\n" + "="*70)
        print("🔍 BUSCADOR INTELIGENTE")
        print("="*70)

        # ✅ EJEMPLO: Buscar por plataforma de IA
        busqueda = "ChatGPT"  # 🔄 CAMBIA AQUÍ LO QUE QUIERES BUSCAR
        print(f"\n🔍 Buscando: '{busqueda}'...")

        # Busca en TODA la base de datos
        coincidencias = datos_limpios[datos_limpios.apply(
            lambda fila: fila.astype(str).str.contains(busqueda, case=False).any(),
            axis=1
        )]

        if len(coincidencias) > 0:
            print(f"✅ Encontrados: {len(coincidencias)} registros")
            print("\n📋 Resultados:")
            print("-" * 70)
            # Muestra información importante de cada coincidencia
            for idx, fila in coincidencias.head(5).iterrows():
                print(f"👤 Registro {fila['user_id']} | Edad: {fila['age']} | País: {fila['country_region']}")
                print(f"   Plataforma: {fila['ai_chatbot_platform']} | Productividad: {fila['productivity']}")
                print("-" * 70)
        else:
            print("⚠️ No se encontraron coincidencias")

        # --- 5. GUARDAR RESULTADOS ---
        ruta_salida = "resultados/datos_procesados.csv"
        datos_limpios.to_csv(ruta_salida, index=False)
        print(f"\n💾 Base limpia guardada en: {ruta_salida}")
        print(auto.registrar_actividad(f"Búsqueda: {busqueda} | Resultados: {len(coincidencias)}"))

    except FileNotFoundError:
        print(f"❌ No se encontró: {archivo_csv}")

    print("\n✅ Ejecución finalizada")

if __name__ == "__main__":
    main()
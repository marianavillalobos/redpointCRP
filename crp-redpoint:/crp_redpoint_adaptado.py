
import pandas as pd

def cargar_datos_desde_csv(ruta_maquinas, demanda_unidades=1000):
    df = pd.read_csv(ruta_maquinas)
    df['demanda_unidades'] = demanda_unidades  # Asignación de demanda por SKU
    return df

def generar_resultado_crp(df):
    df['T. Real (seg/unidad)'] = df['tiempo_real_promedio_min_unidad'] * 60
    df['Utilización'] = df['utilizacion_percent']
    df['Eficiencia'] = df['eficiencia_percent']
    df['Scrap'] = df['scrap_directo_percent']
    df['1-di'] = 1 - (df['scrap_directo_percent'] / 100.0)
    df['Vi'] = df['yield_inicial_percent'] / 100.0
    df['Tci (seg/unidad)'] = df['T. Real (seg/unidad)'] / df['Vi']

    df['Segundos necesarios'] = df['demanda_unidades'] * df['Tci (seg/unidad)']
    df['Tiempo en minutos'] = df['Segundos necesarios'] / 60
    df['Tiempo en horas'] = df['Tiempo en minutos'] / 60

    df['Personal asignado'] = 1  # Valor predeterminado, puede ser parametrizado
    df['Horas por persona'] = df['Tiempo en horas'] / df['Personal asignado']
    df['Horas extra necesarias'] = df['Horas por persona'] - 40
    df['Horas extra necesarias'] = df['Horas extra necesarias'].clip(lower=0)

    df_resultado = df[[
        'ID_maquina',
        'T. Real (seg/unidad)',
        'Utilización',
        'Eficiencia',
        'Scrap',
        '1-di',
        'Vi',
        'Tci (seg/unidad)',
        'Segundos necesarios',
        'Tiempo en minutos',
        'Tiempo en horas',
        'Personal asignado',
        'Horas por persona',
        'Horas extra necesarias'
    ]].rename(columns={'ID_maquina': 'Proceso'})

    return df_resultado

if __name__ == "__main__":
    ruta_csv = "maquinas_estilos_tallas_redpoint.csv"
    df_maquinas = cargar_datos_desde_csv(ruta_csv)
    df_resultados = generar_resultado_crp(df_maquinas)
    df_resultados.to_csv("resultados_crp_redpoint_formato_final.csv", index=False)
    print("Archivo de resultados generado: resultados_crp_redpoint_formato_final.csv")

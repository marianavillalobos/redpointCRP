
# Sistema CRP para Red Point – Línea de Calcetines

Este proyecto implementa un sistema de **Planeación de Requerimientos de Capacidad (CRP)** en Python, enfocado en la etapa de **tejeduría** de la empresa Red Point, donde se ha identificado un cuello de botella operativo crítico.

## 🎯 Objetivo

Analizar la capacidad de las máquinas de tejeduría considerando:
- Tiempos de ciclo reales
- Scrap y eficiencia
- Disponibilidad por turno
- SKU específicos por máquina (estilo + talla)

Y calcular:

- Carga de trabajo real
- Tiempo necesario en segundos, minutos y horas
- Utilización
- Horas extra requeridas por máquina

## 📁 Estructura del Proyecto

```
crp-redpoint/
│
├── data/
│   ├── maquinas_estilos_tallas_redpoint.csv   # Datos de entrada por máquina/SKU
│
├── results/
│   └── resultados_crp_redpoint_formato_final.csv  # Resultados de ejecución
│
├── crp_redpoint_adaptado.py       # Script principal
├── README.md                      # Este archivo
├── requirements.txt               # Dependencias
└── .gitignore                     # Exclusiones del control de versiones
```

## ▶️ Cómo ejecutar

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el script principal:
```bash
python crp_redpoint_adaptado.py
```

3. El resultado se guardará en `results/resultados_crp_redpoint_formato_final.csv`.

## 📥 Datos esperados

El archivo `maquinas_estilos_tallas_redpoint.csv` debe contener:

- `ID_maquina`: identificador único
- `sku`: combinación de estilo y talla
- `tiempo_real_promedio_min_unidad`: tiempo real en minutos
- `yield_inicial_percent`: rendimiento inicial
- `scrap_directo_percent`: porcentaje de scrap
- `horas_disponibles_turno`
- `turnos_por_dia`
- `eficiencia_percent`
- `utilizacion_percent`

## 📤 Resultados generados

El sistema CRP calcula:

- Tiempo por unidad (segundos)
- Tiempo total requerido
- Carga total en minutos y horas
- Personal necesario y horas por persona
- Horas extra requeridas si se supera la jornada estándar

---

Desarrollado como parte del análisis operativo en Red Point para mitigar cuellos de botella y mejorar la toma de decisiones basada en capacidad real.

# Taller Databricks – Ingeniería de Datos

**Autor:** Dylan Mejía
**Curso:** Ingeniería de Datos · Universidad EIA · 2026-2

Taller práctico en **Databricks** para una tienda que necesita almacenar sus ventas, corregir errores y automatizar la preparación de reportes.

## Conjunto de datos

16 registros de ventas (`id_venta`, `fecha`, `producto`, `categoria`, `cantidad`, `precio_unitario`) con tres errores intencionales:

- Venta 3 duplicada
- Venta 8 sin producto
- Venta 12 con cantidad negativa

## Estructura del repositorio

```
.
├── README.md
├── docs/
│   └── Taller_Databricks.pdf        # Informe con respuestas, capturas y explicaciones
├── Ejercicio_1/                     # Almacenar y consultar datos en Unity Catalog
│   ├── 01_cargar_ventas.py
│   └── 01b_consultar_ventas.py
├── Ejercicio_2/                     # Transformación y reglas de calidad
│   └── 02_transformar_ventas.py
├── Ejercicio_3/                     # Automatización con un job
│   ├── configuracion_job.txt
│   └── error_controlado.py
└── Ejercicio_4/                     # Pipeline declarativo (Lakeflow SDP)
    ├── pipeline_ventas.sql
    └── consultas_prueba.sql
```

## Resumen de ejercicios

| # | Tema | Resultado principal |
|---|------|--------------------|
| 1 | Unity Catalog y tablas Delta | Tabla `workspace.ingenieria_datos_dylan.ventas_bronze` (16 registros) |
| 2 | Limpieza y calidad | `ventas_silver` (13 registros) y `ventas_por_categoria`; proceso idempotente con `overwrite` |
| 3 | Lakeflow Jobs | `job_ventas_dylan` con dos tareas dependientes (*All succeeded*), prueba de fallo controlado |
| 4 | Lakeflow Spark Declarative Pipelines | Vistas materializadas `pipeline_ventas_limpias` y `pipeline_ventas_por_categoria`, actualización incremental |

## Cómo usar los notebooks

Los archivos `.py` están en formato de notebook de Databricks. Para importarlos: **Workspace → Import → File**.
El código usa el catálogo `workspace` y el esquema `ingenieria_datos_dylan`.

# Ejercicio 3 - Error controlado
# Celda agregada temporalmente en 01_cargar_ventas (entre la celda del esquema y la de los datos)
# para provocar el fallo de la tarea cargar_ventas. Se eliminó después para la ejecución final exitosa.

spark.table("workspace.ingenieria_datos_dylan.ventas_bronze").select("columna_inexistente").show()

# Error obtenido:
# [UNRESOLVED_COLUMN.WITH_SUGGESTION] A column, variable, or function parameter with name
# `columna_inexistente` cannot be resolved. Did you mean one of the following?
# [`cantidad`, `id_venta`, `precio_unitario`, `categoria`, `fecha`]. SQLSTATE: 42703

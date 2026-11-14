# Databricks notebook source
# Ejercicio 1 - Notebook 01b_consultar_ventas
# Lee la tabla desde otro notebook usando su nombre completo catalogo.esquema.tabla

# COMMAND ----------

ventas = spark.table("workspace.ingenieria_datos_dylan.ventas_bronze")
print("Total registros:", ventas.count())   # Resultado: 16

# COMMAND ----------

display(ventas.filter("categoria = 'Tecnología'"))   # Resultado: 5 ventas

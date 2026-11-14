# Databricks notebook source
# Ejercicio 2 - Notebook 02_transformar_ventas
# Limpieza de datos, cálculo de total_venta y resumen por categoría

# COMMAND ----------

from pyspark.sql import functions as F
BASE = "workspace.ingenieria_datos_dylan"

bronze = spark.table(f"{BASE}.ventas_bronze")
print("Antes de limpiar:", bronze.count())      # 16

sin_dup = bronze.dropDuplicates()               # elimina registros idénticos
print("Sin duplicados:", sin_dup.count())       # 15

# COMMAND ----------

silver = (sin_dup
    .filter(F.col("producto").isNotNull() & (F.trim("producto") != ""))
    .filter(F.col("cantidad") > 0)
    .filter(F.col("precio_unitario") > 0)
    .withColumn("total_venta", F.col("cantidad") * F.col("precio_unitario")))

print("Después de limpiar:", silver.count())    # 13

(silver.write.mode("overwrite")
   .option("overwriteSchema", "true")
   .saveAsTable(f"{BASE}.ventas_silver"))

display(silver)

# COMMAND ----------

por_categoria = (silver.groupBy("categoria")
    .agg(F.sum("total_venta").alias("total_vendido"),
         F.count("*").alias("num_ventas"))
    .orderBy(F.desc("total_vendido")))

(por_categoria.write.mode("overwrite")
   .option("overwriteSchema", "true")
   .saveAsTable(f"{BASE}.ventas_por_categoria"))

display(por_categoria)

# COMMAND ----------

# Verificación después de re-ejecutar el notebook (no deben acumularse registros)
print("Silver:", spark.table(f"{BASE}.ventas_silver").count())                  # 13
print("Por categoría:", spark.table(f"{BASE}.ventas_por_categoria").count())    # 3

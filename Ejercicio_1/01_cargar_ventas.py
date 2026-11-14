# Databricks notebook source
# Ejercicio 1 - Notebook 01_cargar_ventas
# Crea el esquema y guarda las ventas como tabla Delta ventas_bronze

# COMMAND ----------

CATALOGO = "workspace"
ESQUEMA  = "ingenieria_datos_dylan"
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOGO}.{ESQUEMA}")

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

schema = StructType([
    StructField("id_venta", IntegerType()),
    StructField("fecha", StringType()),
    StructField("producto", StringType()),
    StructField("categoria", StringType()),
    StructField("cantidad", IntegerType()),
    StructField("precio_unitario", DoubleType()),
])

datos = [
    (1,  "2026-11-01", "Mouse inalámbrico", "Tecnología", 2,  45000.0),
    (2,  "2026-11-01", "Teclado",           "Tecnología", 1, 120000.0),
    (3,  "2026-11-02", "Camiseta",          "Ropa",       3,  35000.0),
    (3,  "2026-11-02", "Camiseta",          "Ropa",       3,  35000.0),  # duplicada
    (4,  "2026-11-02", "Sartén",            "Hogar",      1,  80000.0),
    (5,  "2026-11-03", "Audífonos",         "Tecnología", 1, 150000.0),
    (6,  "2026-11-03", "Jean",              "Ropa",       2, 110000.0),
    (7,  "2026-11-04", "Lámpara",           "Hogar",      2,  60000.0),
    (8,  "2026-11-04", None,                "Hogar",      1,  25000.0),  # sin producto
    (9,  "2026-11-05", "Chaqueta",          "Ropa",       1, 200000.0),
    (10, "2026-11-05", "Monitor",           "Tecnología", 1, 650000.0),
    (11, "2026-11-06", "Juego de vasos",    "Hogar",      1,  40000.0),
    (12, "2026-11-06", "Gorra",             "Ropa",      -2,  30000.0),  # cantidad negativa
    (13, "2026-11-07", "Cable HDMI",        "Tecnología", 3,  20000.0),
    (14, "2026-11-07", "Cojín",             "Hogar",      4,  25000.0),
    (15, "2026-11-08", "Medias",            "Ropa",       5,   8000.0),
]

df = (spark.createDataFrame(datos, schema)
        .withColumn("fecha", F.to_date("fecha")))

(df.write.format("delta")
   .mode("overwrite")                 # evita acumular filas si se re-ejecuta
   .option("overwriteSchema", "true")
   .saveAsTable(f"{CATALOGO}.{ESQUEMA}.ventas_bronze"))

display(df)

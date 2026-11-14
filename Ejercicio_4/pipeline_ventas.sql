-- Ejercicio 4 - Pipeline declarativo (Lakeflow Spark Declarative Pipelines)
-- Pipeline: pipeline_ventas_dylan | Catálogo: workspace | Esquema: ingenieria_datos_dylan | Cómputo: Serverless
-- Archivo: my_transformation.sql

CREATE OR REFRESH MATERIALIZED VIEW pipeline_ventas_limpias AS
SELECT DISTINCT
  id_venta, fecha, producto, categoria, cantidad, precio_unitario,
  cantidad * precio_unitario AS total_venta
FROM workspace.ingenieria_datos_dylan.ventas_bronze
WHERE producto IS NOT NULL AND trim(producto) <> ''
  AND cantidad > 0
  AND precio_unitario > 0;

CREATE OR REFRESH MATERIALIZED VIEW pipeline_ventas_por_categoria AS
SELECT categoria,
       SUM(total_venta) AS total_vendido,
       COUNT(*)         AS num_ventas
FROM pipeline_ventas_limpias
GROUP BY categoria;

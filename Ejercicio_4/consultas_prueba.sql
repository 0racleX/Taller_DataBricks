-- Ejercicio 4 - Consultas de prueba (ejecutadas en el SQL Editor)

-- 1. Resumen ANTES de agregar la venta
SELECT * FROM workspace.ingenieria_datos_dylan.pipeline_ventas_por_categoria
ORDER BY total_vendido DESC;

-- 2. Agregar una venta válida a ventas_bronze (sin ejecutar el notebook de carga)
INSERT INTO workspace.ingenieria_datos_dylan.ventas_bronze
VALUES (16, DATE'2026-11-10', 'Mouse inalámbrico', 'Tecnología', 2, 45000.0);

-- 3. Volver a ejecutar el pipeline (botón "Run pipeline") y consultar el resumen DESPUÉS
SELECT * FROM workspace.ingenieria_datos_dylan.pipeline_ventas_por_categoria
ORDER BY total_vendido DESC;

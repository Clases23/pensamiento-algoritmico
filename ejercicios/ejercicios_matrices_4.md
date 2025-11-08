## Ejercicio: Control de Inventario en Bodegas

Cada fila corresponde a una **bodega** y las columnas representan: **StockInicial**, **Entradas**, **Salidas** y **StockFinal**. La regla de consistencia por fila es:
`StockInicial + Entradas − Salidas == StockFinal`.

> Nota: hay una bodega intencionalmente **inconsistente** para probar validaciones.

```python
bodegas = ["Bodega Centro", "Bodega Norte", "Bodega Sur", "Bodega Oriente", "Bodega Occidente"]
# Columnas: [StockInicial, Entradas, Salidas, StockFinal]
inventario = [
    [500, 200, 150, 550],  # Centro       -> 500+200-150 = 550 ✅
    [400, 150, 120, 430],  # Norte        -> 400+150-120 = 430 ✅
    [350, 100, 180, 270],  # Sur          -> 350+100-180 = 270 ✅
    [300,  80,  90, 280],  # Oriente      -> 300+80-90   = 290 ❌ (inconsistente a propósito)
    [450, 120, 160, 410]   # Occidente    -> 450+120-160 = 410 ✅
]
```

* Cree una función llamada `stock_final_de(bodega)` que retorne el **StockFinal** de la bodega dada.
* Cree una función llamada `bodegas_bajo_stock(umbral)` que retorne una **lista de bodegas** con `StockFinal < umbral`.
* Cree una función llamada `total_por_columna(nombre_columna)` que retorne el **total** de la columna indicada (`"StockInicial"`, `"Entradas"`, `"Salidas"` o `"StockFinal"`).
* Cree una función llamada `es_consistente(bodega)` que retorne `True` si la **bodega cumple** la regla de consistencia y `False` en caso contrario.
* Cree una función llamada `bodegas_inconsistentes()` que retorne una **lista con los nombres** de las bodegas **inconsistentes**.

---

## Ejercicio : Tickets de Soporte Técnico por Categoría y Semana

Cada fila es una **categoría** de ticket y cada columna una **semana**.

```python
categorias = ["Autenticación", "Red/Conectividad", "Hardware", "Software", "Cuenta/Facturación"]
semanas = ["S1", "S2", "S3", "S4"]

tickets = [
    [85,  90,  110, 95],  # Autenticación
    [70,  75,   80, 85],  # Red/Conectividad
    [55,  60,   58, 62],  # Hardware
    [95, 105,  115, 98],  # Software
    [40,  45,   50, 48]   # Cuenta/Facturación
]
```

* Cree la función `total_tickets_categoria(categoria)` que retorne el **total mensual** de tickets de la categoría dada.
* Cree la función `total_tickets_semana(numero_semana)` que retorne el **total** de tickets de la semana indicada (1 a 4).
* Cree la función `categoria_mayor_demanda()` que retorne la **categoría** con mayor total de tickets.
* Cree la función `semana_menor_demanda()` que retorne el **número de semana** con menor total de tickets.
* Cree la función `tickets_mayores_a(umbral)` que retorne **cuántas celdas** de `tickets` son **mayores** que `umbral`.

---

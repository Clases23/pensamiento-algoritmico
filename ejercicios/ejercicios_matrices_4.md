# Taller de Práctica en Python (Manejo de Matrices)

> Sugerencia general: cada subpunto **debe** resolverse creando la función con el **nombre indicado**. Puedes usar ciclos `for`, acumuladores y comparaciones simples.

---

## Ejercicio 1: Producción de Cacao en Colombia

En varios departamentos productores se registró la producción **trimestral** de cacao (en toneladas) durante un año. Cada fila representa un **departamento** y cada columna un **trimestre**:

```python
departamentos = ["Chocó", "Nariño", "Arauca", "Santander", "Meta"]
trimestres = ["T1 (Ene-Mar)", "T2 (Abr-Jun)", "T3 (Jul-Sep)", "T4 (Oct-Dic)"]

produccion_cacao = [
    [70,  85,  90,  95],   # Chocó
    [60,  65,  80,  85],   # Nariño
    [55,  60,  70,  75],   # Arauca
    [95, 100, 110, 120],   # Santander
    [50,  55,  60,  70]    # Meta
]
```

* Cree una función llamada `total_cacao_departamento(departamento)` que retorne la **producción total anual** del departamento dado.
* Cree una función llamada `total_cacao_trimestre(numero_trimestre)` que retorne la **producción total** del trimestre indicado (1 a 4).
* Cree una función llamada `departamento_mas_cacao()` que retorne el **nombre del departamento** con **mayor producción anual**.
* Cree una función llamada `trimestre_menos_cacao()` que retorne el **número de trimestre** con **menor producción total**.
* Cree una función llamada `porcentaje_cacao_por_departamento()` que retorne una **lista de porcentajes** de contribución anual por departamento (en el mismo orden de `departamentos`).

---

## Ejercicio 2: Usuarios en la Red WiFi del Campus

Se midieron los usuarios conectados a la red WiFi en distintos **edificios** del campus y en diferentes **franjas horarias**:

```python
edificios = ["Biblioteca", "Laboratorios", "Bloque A", "Bloque B", "Gimnasio"]
franjas = ["Mañana", "Mediodía", "Tarde", "Noche"]

usuarios_wifi = [
    [800,  900, 1100, 500],  # Biblioteca
    [700,  650,  900, 400],  # Laboratorios
    [600,  500,  750, 350],  # Bloque A
    [550,  520,  700, 300],  # Bloque B
    [400,  380,  450, 200]   # Gimnasio
]
```

* Cree una función llamada `total_usuarios_edificio(edificio)` que retorne el **total diario** de usuarios del edificio dado.
* Cree una función llamada `total_usuarios_franja(nombre_franja)` que retorne el **total de usuarios** en **todas** las sedes para la franja dada.
* Cree una función llamada `edificio_mayor_afluencia()` que retorne el **nombre del edificio** con mayor total diario.
* Cree una función llamada `franja_menor_afluencia()` que retorne el **nombre de la franja** con menor total de usuarios sumando todos los edificios.
* Cree una función llamada `conteo_mediciones_mayores(umbral)` que retorne **cuántas celdas** de `usuarios_wifi` son **mayores** que `umbral`.

---

## Ejercicio 3: Desempeño Académico por Componentes

Se registraron las calificaciones (0.0 a 5.0) de varios **estudiantes** en cuatro **componentes** de evaluación:

```python
estudiantes = ["Andrés", "Brenda", "Carlos", "Diana", "Esteban"]
componentes = ["Parcial 1", "Parcial 2", "Proyecto", "Final"]

notas = [
    [3.8, 4.1, 4.5, 4.0],  # Andrés
    [2.7, 3.0, 3.5, 3.2],  # Brenda
    [4.5, 4.7, 4.6, 4.8],  # Carlos
    [3.0, 3.2, 2.9, 3.1],  # Diana
    [3.8, 3.9, 4.0, 4.2]   # Esteban
]
```

* Cree una función llamada `promedio_estudiante(nombre)` que retorne el **promedio** del estudiante indicado.
* Cree una función llamada `promedio_por_componente()` que retorne una **lista con el promedio** de cada componente (en el orden de `componentes`).
* Cree una función llamada `mejor_estudiante()` que retorne el **nombre del estudiante** con el **mejor promedio general**.
* Cree una función llamada `estudiantes_con_bajo_en_alguno(umbral)` que retorne una **lista de nombres** con **alguna nota < umbral**.
* Cree una función llamada `maxima_nota_en_componente(nombre_componente)` que retorne la **nota máxima** alcanzada en ese componente.

---

## Ejercicio 4: Generación de Energía Solar (kWh)

Cinco plantas solares reportaron su generación semanal (kWh) durante cuatro semanas:

```python
plantas = ["Guajira", "Cesar", "Córdoba", "Valle", "Cundinamarca"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

kwh_solar = [
    [1200, 1300, 1250, 1400],  # Guajira
    [900,   950,  980, 1000],  # Cesar
    [800,   820,  790,  850],  # Córdoba
    [1000, 1100, 1080, 1150],  # Valle
    [700,   720,  750,  780]   # Cundinamarca
]
```

* Cree una función llamada `total_kwh_planta(planta)` que retorne la **generación total** anual (cuatro semanas) de la planta indicada.
* Cree una función llamada `total_kwh_semana(numero_semana)` que retorne la **generación total** de la semana indicada (1 a 4) sumando todas las plantas.
* Cree una función llamada `planta_mayor_generacion()` que retorne el **nombre de la planta** con **mayor generación total**.
* Cree una función llamada `semana_menor_generacion()` que retorne el **número de semana** con **menor generación total**.
* Cree una función llamada `plantas_sobre_umbral(umbral: int)` que retorne una **lista de plantas** cuya **generación total** supera `umbral`.

---

## Ejercicio 5: Control de Inventario en Bodegas

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

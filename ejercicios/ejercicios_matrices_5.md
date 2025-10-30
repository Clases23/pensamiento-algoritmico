# Taller de Práctica en Python (Manejo de Matrices)

> Indicaciones: en **cada subpunto** debes crear **exactamente** la función con el **nombre indicado**.

---

## Ejercicio 1: Producción de Flores (miles de tallos) por Región y Trimestre

Cada fila es una **región** y cada columna un **trimestre**.

```python
regiones = ["Sabana Cundinamarca", "Rionegro", "La Ceja", "Cajicá", "Madrid (Cund.)"]
trimestres = ["T1", "T2", "T3", "T4"]

flores = [
    [420, 450, 480, 520],  # Sabana Cundinamarca
    [300, 320, 350, 370],  # Rionegro
    [260, 280, 290, 310],  # La Ceja
    [220, 230, 240, 260],  # Cajicá
    [200, 210, 230, 240]   # Madrid (Cund.)
]
```

* Cree la función `total_flores_region(region)` que retorne la **producción anual** de la región dada.
* Cree la función `total_flores_trimestre(numero_trimestre)` que retorne la **producción total del trimestre** indicado (1 a 4).
* Cree la función `region_top_flores()` que retorne el **nombre de la región** con mayor producción anual.
* Cree la función `trimestre_min_flores()` que retorne el **número de trimestre** con menor producción total.
* Cree la función `porcentaje_flores_por_region()` que retorne una **lista de porcentajes** de contribución anual por región (mismo orden que `regiones`).

---

## Ejercicio 2: Asistencia al Cine por Sala y Franja Horaria

Cada fila es una **sala** y cada columna una **franja**.

```python
salas = ["Sala 1", "Sala 2", "Sala 3", "Sala 4", "Sala 5"]
franjas = ["Matutina", "Tarde", "Noche", "Trasnoche"]

asistencia = [
    [180, 320, 420, 110],  # Sala 1
    [150, 290, 380,  95],  # Sala 2
    [170, 310, 410, 105],  # Sala 3
    [140, 260, 350,  90],  # Sala 4
    [160, 280, 360, 100]   # Sala 5
]
```

* Cree la función `total_asistentes_sala(sala)` que retorne el **total diario** de asistentes de la sala dada.
* Cree la función `total_asistentes_franja(nombre_franja)` que retorne el **total** en **todas** las salas para la franja dada.
* Cree la función `sala_mayor_asistencia()` que retorne la **sala** con mayor asistencia total.
* Cree la función `franja_menor_asistencia()` que retorne el **nombre de la franja** con menor asistencia total.
* Cree la función `funciones_sobre_umbral(umbral)` que retorne **cuántas celdas** de `asistencia` son **mayores** que `umbral`.

---

## Ejercicio 3: Vuelos Domésticos por Aeropuerto y Trimestre

Cada fila es un **aeropuerto** y cada columna un **trimestre**. Los valores son **número de vuelos**.

```python
aeropuertos = ["BOG (El Dorado)", "MDE (JMC)", "CLO (Alfonso Bonilla)", "CTG (Rafael Núñez)", "SMR (Simón Bolívar)"]
trimestres = ["T1", "T2", "T3", "T4"]

vuelos = [
    [12500, 13200, 13800, 14500],  # BOG
    [ 5200,  5600,  5900,  6200],  # MDE
    [ 3400,  3700,  3900,  4100],  # CLO
    [ 4100,  4300,  4500,  4700],  # CTG
    [ 2800,  3000,  3200,  3400]   # SMR
]
```

* Cree la función `total_vuelos_aeropuerto(aeropuerto)` que retorne el **total anual** de vuelos del aeropuerto dado.
* Cree la función `total_vuelos_trimestre(numero_trimestre)` que retorne el **total** de vuelos del trimestre indicado (1 a 4).
* Cree la función `aeropuerto_con_mas_vuelos()` que retorne el **aeropuerto** con mayor total anual.
* Cree la función `trimestre_con_menos_vuelos()` que retorne el **número de trimestre** con menor total de vuelos.
* Cree la función `aeropuertos_sobre_umbral(umbral)` que retorne una **lista** de aeropuertos cuyo **total anual** supera `umbral`.

---

## Ejercicio 4: Taquilla de Conciertos por Ciudad y Mes (miles de asistentes)

Cada fila es una **ciudad** y cada columna un **mes**.

```python
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Bucaramanga"]
meses = ["M1", "M2", "M3", "M4"]

taquilla = [
    [45, 50, 55, 60],  # Bogotá
    [30, 35, 38, 42],  # Medellín
    [25, 28, 30, 34],  # Cali
    [22, 24, 27, 29],  # Barranquilla
    [18, 20, 22, 25]   # Bucaramanga
]
```

* Cree la función `total_taquilla_ciudad(ciudad)` que retorne la **asistencia total** en la ciudad dada.
* Cree la función `total_taquilla_mes(numero_mes)` que retorne la **asistencia total** del mes indicado (1 a 4) sumando todas las ciudades.
* Cree la función `ciudad_con_mayor_taquilla()` que retorne la **ciudad** con mayor asistencia total.
* Cree la función `mes_con_menor_taquilla()` que retorne el **número de mes** con la menor asistencia total.
* Cree la función `ciudades_sobre_asistencia(umbral)` que retorne una **lista** de ciudades cuya **asistencia total** supera `umbral`.

---

## Ejercicio 5: Tickets de Soporte Técnico por Categoría y Semana

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

# Ejercicios de Programación en Python (Manejo de Matrices)

## Ejercicio 1: Producción de Café en Colombia

En varias regiones cafeteras de Colombia se registró la producción trimestral de café (en toneladas) durante un año. Cada fila de la matriz representa un departamento productor y cada columna corresponde a un trimestre del año (Trimestre 1 = enero-marzo, Trimestre 2 = abril-junio, etc.). A continuación se muestra la matriz `produccion_cafe` con los datos recolectados, junto con las listas auxiliares `departamentos` y `trimestres`:

```python
departamentos = ["Antioquia", "Huila", "Tolima", "Caldas", "Santander"]
trimestres = ["T1 (Ene-Mar)", "T2 (Abr-Jun)", "T3 (Jul-Sep)", "T4 (Oct-Dic)"]

produccion_cafe = [
    [120, 135, 150, 160],  # Antioquia
    [100, 110, 115, 130],  # Huila
    [80,  85,  90,  100],  # Tolima
    [90,  95,  100, 105],  # Caldas
    [60,  70,  80,  75]    # Santander
]
```

* Cree una función que reciba el nombre de un departamento y retorne la producción total de café de ese departamento en el año.
* Cree una función que reciba el número de un trimestre (1 a 4) y retorne la producción total de café de todos los departamentos en ese trimestre.
* Cree una función que retorne el nombre del departamento con mayor producción total de café en todo el año.
* Cree una función que retorne el número del trimestre en el cual se produjo la menor cantidad de café en total (considerando la suma de todos los departamentos por trimestre).
* Cree una función que retorne una lista con el porcentaje del total anual de producción que aportó cada departamento. (Por ejemplo, un resultado posible podría ser `[30.5, 25.0, 15.2, 18.3, 11.0]` indicando porcentajes de contribución de cada departamento en orden.)

## Ejercicio 2: Pasajeros en el TransMilenio de Bogotá

En un día típico se registró el número de pasajeros que utilizaron varias estaciones principales de TransMilenio en Bogotá, distribuidos en diferentes franjas horarias. La siguiente matriz `pasajeros` indica la cantidad de pasajeros en cada combinación de **estación** y **franja del día**. Cada fila corresponde a una estación de TransMilenio y cada columna a una franja horaria (mañana, medio día, tarde, noche), según las listas auxiliares `estaciones` y `franjas`:

```python
estaciones = ["Portal Norte", "Portal Sur", "Estación Jiménez", "Estación Calle 100"]
franjas = ["Mañana", "Medio día", "Tarde", "Noche"]

pasajeros = [
    [5000, 3000, 4000, 2000],  # Portal Norte
    [4500, 2500, 3500, 1500],  # Portal Sur
    [3000, 2000, 2500, 1000],  # Estación Jiménez
    [3200, 2100, 2800,  900]   # Estación Calle 100
]
```

* Cree una función que reciba el nombre de una estación y retorne el total de pasajeros que pasaron por dicha estación durante todo el día.
* Cree una función que reciba el nombre de una franja horaria (`"Mañana"`, `"Medio día"`, `"Tarde"` o `"Noche"`) y retorne la cantidad total de pasajeros que se movilizaron en **todas** las estaciones durante esa franja.
* Cree una función que retorne el nombre de la estación que tuvo la mayor cantidad total de pasajeros en el día.
* Cree una función que retorne el nombre de la franja horaria en la cual se registró la menor cantidad total de pasajeros (sumando todas las estaciones).
* Cree una función que reciba un número (umbral) y retorne cuántas mediciones **estación-franja** tuvieron un número de pasajeros superior a ese umbral. *(Por ejemplo, si el umbral es 3000, la función debe contar cuántos elementos de la matriz `pasajeros` son mayores a 3000.)*

## Ejercicio 3: Notas de Estudiantes Universitarios

En una universidad colombiana se registran las calificaciones finales de un grupo de estudiantes en varias asignaturas. La escala de notas va de 0.0 a 5.0, siendo 3.0 la calificación mínima aprobatoria. A continuación se presenta la matriz `notas` con las calificaciones de 5 estudiantes en 4 materias diferentes. Cada fila corresponde a un **estudiante** (mapeado en la lista `estudiantes`) y cada columna corresponde a una **materia** (mapeada en la lista `materias`):

```python
estudiantes = ["Ana", "Benjamín", "Camila", "David", "Luisa"]
materias = ["Programación", "Cálculo", "Física", "Inglés"]

notas = [
    [4.5, 3.8, 4.2, 5.0],  # Ana
    [2.9, 3.5, 2.7, 4.0],  # Benjamín
    [3.2, 2.9, 4.8, 4.1],  # Camila
    [4.0, 4.2, 3.0, 3.5],  # David
    [3.8, 4.5, 4.0, 2.5]   # Luisa
]
```

* Cree una función que calcule y retorne el promedio de notas de **cada estudiante**. (El resultado puede ser una lista de promedios en el mismo orden de la lista `estudiantes`.)
* Cree una función que calcule y retorne el promedio de **cada materia**. (El resultado puede ser una lista de promedios en el mismo orden de la lista `materias`.)
* Cree una función que retorne el **nombre del estudiante** con el mejor promedio general en el semestre.
* Cree una función que retorne una lista con los **nombres de los estudiantes** que reprobaron al menos una materia (nota < 3.0 en alguna de sus calificaciones).
* Cree una función que reciba el nombre de una materia y retorne la **nota más alta** obtenida en esa materia entre todos los estudiantes.

## Ejercicio 4: Turistas Extranjeros en Ciudades Colombianas

El Ministerio de Turismo registró la cantidad de turistas extranjeros que visitaron varias ciudades de Colombia durante cada trimestre de un año. Los valores (en la matriz `turistas`) están expresados en **miles de turistas**. Cada fila corresponde a una **ciudad** turística y cada columna a un **trimestre** del año. A continuación se proporcionan los datos recopilados, junto con las listas auxiliares `ciudades` y `trimestres`:

```python
ciudades = ["Cartagena", "Bogotá", "Medellín", "San Andrés", "Santa Marta"]
trimestres = ["T1", "T2", "T3", "T4"]

turistas = [
    [80,  90,  120, 150],  # Cartagena
    [60,  75,   80, 100],  # Bogotá
    [40,  55,   70,  80],  # Medellín
    [30,  50,   60,  70],  # San Andrés
    [20,  30,   50,  60]   # Santa Marta
]
```

* Cree una función que reciba el nombre de una ciudad y retorne la cantidad **total de turistas** (en miles) que visitaron esa ciudad en todo el año.
* Cree una función que reciba el número de un trimestre (1 a 4) y retorne la cantidad total de turistas (en miles) que visitaron **todas** las ciudades en ese trimestre.
* Cree una función que retorne el **nombre de la ciudad** que recibió la mayor cantidad total de turistas en el año.
* Cree una función que retorne el **número de trimestre** que registró el mayor volumen de turistas sumando todas las ciudades.
* Cree una función que reciba un número (cantidad de turistas en miles) y retorne una lista con los nombres de las ciudades que recibieron más de esa cantidad de turistas en total durante el año. *(Por ejemplo, si se ingresa 200, la función retornaría `["Cartagena"]` considerando los datos dados, ya que Cartagena tuvo 440 mil turistas en el año, superando ese umbral.)*

## Ejercicio 5: Tabla de Posiciones de Liga de Fútbol

En un torneo local de fútbol en Colombia, conformado por 5 equipos, se lleva la siguiente tabla de posiciones parcial. Para cada equipo se registran: **partidos jugados (PJ)**, **partidos ganados (PG)**, **partidos empatados (PE)**, **partidos perdidos (PP)**, **goles a favor (GF)** y **goles en contra (GC)**. La matriz `tabla_posiciones` presenta estos datos por equipo, en el mismo orden que la lista `equipos`:

```python
equipos = ["Atlético Nacional", "Millonarios", "Deportivo Cali", "Junior", "Santa Fe"]

# Formato de cada fila: [PJ, PG, PE, PP, GF, GC]
tabla_posiciones = [
    [8, 5, 3, 0, 13,  5],  # Atlético Nacional
    [8, 4, 3, 1,  9,  6],  # Millonarios
    [8, 3, 2, 3,  8,  9],  # Deportivo Cali
    [8, 2, 3, 3,  7, 10],  # Junior
    [7, 1, 4, 3,  4, 12]   # Santa Fe  (PJ debería ser 8 aquí, hay un partido no contabilizado)
]
```

* Cree una función que reciba el nombre de un equipo y retorne su **puntaje total** en la tabla, considerando 3 puntos por victoria, 1 punto por empate y 0 por derrota.
* Cree una función que retorne el nombre del **equipo con mejor diferencia de gol** (diferencia = GF − GC) del torneo.
* Cree una función que retorne una lista con los nombres de los equipos que **no han perdido ningún partido** en lo que va del torneo.
* Cree una función que verifique si, para todos los equipos, el número de **partidos jugados (PJ)** coincide con la suma de sus partidos ganados, empatados y perdidos. La función debe retornar `True` si **todos** los equipos están consistentes en sus datos, o `False` en caso contrario.
* Cree una función que retorne el nombre del equipo que tiene la **mayor cantidad de goles en contra** (es decir, la peor defensa del torneo).

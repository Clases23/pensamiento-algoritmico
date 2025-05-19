## Ejercicios de matrices (listas de listas)

---

### Ejercicio 1: Plan de asientos de auditorio - Contexto: Una estacion con un auditorio de 10 filas y 15 columnas usa una matriz booleana `asientos` (True=ocupado, False=libre).  
- Cuenta cuantos asientos libres hay en cada fila.  
- Determina la primera fila que tiene menos de 5 asientos libres.  
- Muestra las coordenadas (fila, columna) de todos los asientos ocupados en la ultima fila.  
- Permite al usuario intercambiar el estado de dos asientos indicados por sus coordenadas.  

---

### Ejercicio 2: Mapa de deteccion de movimiento - Contexto: Un sensor de movimiento genera una matriz 8x8 de valores 0 (sin movimiento) y 1 (movimiento).  
- Identifica todas las posiciones donde hay deteccion (valor 1).  
- Cuenta el numero total de detecciones registradas.  
- Lista las filas que no registraron ninguna deteccion.  
- Presenta una lista de tuplas con fila y columna de cada deteccion.  

---

### Ejercicio 3: Tablero de juego Truiqui - Contexto: Un juego de tres en raya usa una matriz 3x3 con 'X', 'O' o '' (vacio).  
- Muestra el tablero formateado en pantalla.  
- Pide al usuario ficha y coordenadas, y marca el movimiento si la casilla esta vacia.  
- Verifica antes de marcar si la posicion escogida esta libre o ya ocupada.  
- Lista todas las posiciones vacias disponibles para la siguiente jugada.  

---

### Ejercicio 4: Agenda semanal - Contexto: Una agenda organiza actividades en una matriz 7x24 (filas=dias, columnas=horas), con cadenas vacias o el nombre de la actividad.  
- Solicita un dia (0-6) y una hora (0-23) y devuelve la actividad programada o indica "Libre".  
- Lista todas las horas libres del dia martes (fila 1).  
- Cuenta cuantas horas ocupadas hay en cada dia.  
- Crea una lista de dias que no tienen ninguna actividad.  

---

### Ejercicio 5: Cuestionario de verdadero/falso - Contexto: Un cuestionario de 5 alumnos y 3 preguntas usa una matriz 5x3 con True/False. Se tiene otra lista `clave` con la respuesta correcta de cada pregunta.  
- Compara matriz y lista `clave` y construye una matriz de resultados (True=acierto, False=error).  
- Para cada alumno, cuenta cuantas respuestas acertadas obtuvo.  
- Identifica cuales alumnos acertaron todas las preguntas.  
- Muestra una lista de tuplas (indice_alumno, aciertos) para cada alumno.  

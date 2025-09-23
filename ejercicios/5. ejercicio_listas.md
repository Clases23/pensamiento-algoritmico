

**Instrucción:** puedes usar bucles (`for`, `while`), bucles anidados, condicionales y funciones; **solo listas**, sin estructuras más complejas.

1. ## Lista de compras filtrada  
   Dado un `list` con nombres de productos (p. ej. `["leche", "pan", "huevos", "queso", "aceite"]`), escribe una función que:
   - Reciba la lista y una letra inicial.
   - Devuelva otra lista solo con los productos que comiencen por esa letra.
   - Muestre cuántos ítems cumplen ese criterio.

2. ## Análisis de temperaturas semanales  
   Dada una lista con 7 valores numéricos (temperaturas diarias):
   - Calcula el promedio de todas las temperaturas.
   - Genera una lista con los índices de los días en los que la temperatura superó el promedio.
   - Crea otra lista con las temperaturas ordenadas de menor a mayor.

3. ## Control de gastos mensuales  
   Tienes una lista de transacciones (positivas para ingresos, negativas para gastos):
   - Calcula el balance final.
   - Separa en dos listas: `ingresos` y `gastos`.
   - Indica si el mes cerró en superávit o déficit.

4. ## Gestión de tareas pendientes  
   Mantén una lista de strings con tareas. Crea funciones para:
   - **Agregar** una tarea al final de la lista.
   - **Eliminar** una tarea por su nombre.
   - **Marcar** una tarea como completada (por ejemplo, modificando `"tarea"` a `"[OK] tarea"`).
   - **Mostrar** todas las tareas indicando cuáles están pendientes y cuáles completadas.

5. ## Inventario de tienda  
   Usa dos listas paralelas:  
   ```python
   productos = ["Camisa", "Pantalón", "Zapatos", …]
   stock     = [10, 5, 2, …]
   ```
   - Dada el nombre de un producto, devuelve su stock.
   - Procesa una venta (nombre + cantidad): resta del stock y avisa si no hay suficiente.
   - Lista los productos cuyo `stock == 0`.

6. ## Notas de estudiantes  
   Representa a 5 estudiantes con una lista de listas (cada sublista contiene sus 3 notas):
   ```python
   notas = [
     [75, 82, 90],
     [60, 58, 65],
     …
   ]
   ```
   - Recorre con bucles anidados y calcula el promedio de cada alumno.
   - Crea una lista `aprobados` con los promedios ≥ 60 y otra `reprobados` con los < 60.
   - Muestra cuántos alumnos aprobaron y cuántos reprobaron.

7. ## Agenda de contactos  
   Usa una lista de listas donde cada contacto es `[nombre, teléfono]`:
   - Busca contactos por subcadena en el nombre (devuelve lista de coincidencias).
   - Actualiza el teléfono de un contacto dado su nombre exacto.
   - Elimina un contacto por nombre.

8. ## Asignación de asientos en un cine  
   Modela la sala como una lista de listas (filas × asientos), e.g.:
   ```python
   sala = [
     ["L", "L", "O", "L", "L"],  # L = libre, O = ocupado
     ["O", "L", "L", "O", "L"],
     …
   ]
   ```
   - Cuenta cuántos asientos libres quedan.
   - Encuentra el primer asiento libre (devuelve fila y columna).
   - Marca un asiento como ocupado (cambia `"L"` → `"O"`) y avisa si ya estaba reservado.
```

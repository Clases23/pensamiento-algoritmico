---

# **Ciclos en Programación: Enunciados del "Mundo Real" 🚀**  

Cada problema está diseñado para incluir al **menos un ciclo** (`for`, `while`, `while True`) y, en algunos casos, **ciclos anidados**.

---

### **Ejercicio 1: Control de temperatura en un invernadero 🌱** *(Uso de `WHILE TRUE`, ciclo anidado para mediciones múltiples)*  
📌 **Enunciado:**  
Un invernadero mide la temperatura **cada 10 segundos durante 1 minuto** antes de registrar la media de temperatura. Si la temperatura media baja de `15°C`, se enciende la calefacción, y si sube de `30°C`, se activa la ventilación.  
El programa debe repetirse **hasta que el usuario decida finalizar**.  

🔹 **Debe utilizar:**  
- `WHILE TRUE` para mantener el monitoreo continuo.  
- `FOR` anidado para tomar **6 mediciones de temperatura en 1 minuto**.  

---

### **Ejercicio 2: Cajero automático 🏦** *(Uso de `WHILE` y `WHILE TRUE`, anidado en el menú de opciones)*  
📌 **Enunciado:**  
Un cajero automático solicita al usuario ingresar su clave.  
- Si la clave es incorrecta **más de 3 veces**, la cuenta se bloquea.  
- Si la clave es correcta, el usuario puede **consultar saldo, retirar dinero o salir**.  
- Si el usuario elige retirar dinero, el sistema debe solicitar la cantidad y verificar que sea múltiplo de 10.  

🔹 **Debe utilizar:**  
- `WHILE` para controlar los intentos de clave.  
- `WHILE TRUE` dentro del menú para mantener el sistema activo.  
- `WHILE` anidado dentro de la opción de retiro para validar que la cantidad ingresada sea correcta.  

---

### **Ejercicio 3: Registro de asistencia en una escuela 📚** *(Uso de `FOR` anidado para varias clases)*  
📌 **Enunciado:**  
El director de una escuela necesita un registro de asistencia para varias clases.  
- El programa debe solicitar cuántas clases se registrarán.  
- Luego, para cada clase, se ingresará la asistencia de `N` estudiantes (`"P"` para presente, `"A"` para ausente).  
- Al final, se muestra cuántos estudiantes asistieron en cada clase y el total general.  

🔹 **Debe utilizar:**  
- `FOR` para iterar sobre cada clase.  
- `FOR` anidado para recorrer a los estudiantes de cada clase.  

---

### **Ejercicio 4: Sistema de peaje 🚗** *(Uso de `WHILE TRUE`, anidado para turnos de cobro)*  
📌 **Enunciado:**  
Un peaje cobra a los conductores según el tipo de vehículo:  
- **Moto:** $2,000  
- **Carro:** $5,000  
- **Camión:** $10,000  

El sistema debe operar **por turnos de 5 vehículos**.  
- Se solicita el tipo de cada vehículo.  
- Al final de cada turno, se muestra el total recaudado.  
- El sistema debe repetirse hasta que el usuario decida salir.  

🔹 **Debe utilizar:**  
- `WHILE TRUE` para mantener el sistema activo.  
- `FOR` anidado dentro del `WHILE` para procesar cada turno de 5 vehículos.  

---

### **Ejercicio 5: Control de acceso a un edificio 🏢** *(Uso de `WHILE`, anidado para múltiples empleados)*  
📌 **Enunciado:**  
El acceso a un edificio es controlado mediante identificaciones.  
- Para **cada empleado**, el programa solicita su número de ID y clave.  
- Si la clave es incorrecta **más de 3 veces**, se bloquea el acceso.  
- Si es correcta, el programa registra la hora de ingreso y permite que otro empleado intente ingresar.  
- El sistema se ejecuta hasta que el usuario decida finalizar.  

🔹 **Debe utilizar:**  
- `WHILE` para verificar la clave con intentos limitados.  
- `WHILE TRUE` anidado para permitir que múltiples empleados intenten ingresar.  

---

### **Ejercicio 6: Máquina de boletos para el metro 🚆** *(Uso de `WHILE TRUE`, anidado para múltiples pasajeros)*  
📌 **Enunciado:**  
Una máquina de boletos vende tres tipos de pasajes:  
- **Normal:** $2,500  
- **Estudiante:** $1,500  
- **Tercera edad:** $1,000  

El programa debe permitir vender boletos a **varios pasajeros**, donde cada pasajero puede comprar varios boletos.  
- Se calcula el total para cada pasajero.  
- Luego, el sistema solicita el pago exacto antes de continuar con otro pasajero.  
- Se repite hasta que el operador decida finalizar.  

🔹 **Debe utilizar:**  
- `WHILE TRUE` para mantener el programa en ejecución.  
- `WHILE` anidado para manejar múltiples boletos por pasajero.  

---

### **Ejercicio 7: Tienda en línea con carrito de compras 🛒** *(Uso de `WHILE` anidado para validar compras)*  
📌 **Enunciado:**  
Un usuario agrega productos a un carrito de compras ingresando su precio.  
- Si el usuario ingresa un precio **negativo**, debe reingresar el valor.  
- Cuando finaliza la compra (`0` para terminar), el programa muestra el total y solicita confirmación.  
- Si el usuario rechaza la compra, se repite el proceso hasta que acepte.  

🔹 **Debe utilizar:**  
- `WHILE` para agregar productos.  
- `WHILE` anidado para validar valores correctos.  
- `WHILE` adicional para repetir la compra si es rechazada.  

---

### **Ejercicio 8: Evaluación de alumnos en un curso 🎓** *(Uso de `FOR` anidado para varias materias)*  
📌 **Enunciado:**  
Un profesor evalúa `N` estudiantes en `M` materias.  
- Se ingresa la nota de cada estudiante en cada materia.  
- Se calcula el promedio de cada estudiante.  
- Si el promedio es **menor a 60**, el estudiante reprueba.  
- Se muestra cuántos aprobaron y cuántos reprobaron.  

🔹 **Debe utilizar:**  
- `FOR` para recorrer a los estudiantes.  
- `FOR` anidado para ingresar notas en cada materia.  

---

### **Ejercicio 9: Parqueadero con espacios limitados 🚘** *(Uso de `WHILE`, anidado para validar entradas/salidas)*  
📌 **Enunciado:**  
Un parqueadero tiene `20` espacios disponibles.  
- Cuando un vehículo **entra**, los espacios disponibles disminuyen.  
- Si un vehículo **sale**, los espacios aumentan.  
- **Si el parqueadero está lleno, no se permiten más entradas.**  
- El sistema debe preguntar por cada acción (`E` para entrar, `S` para salir) y validar si es posible.  

🔹 **Debe utilizar:**  
- `WHILE` para gestionar las entradas y salidas.  
- `WHILE` anidado para validar cada acción antes de ejecutarla.  

---

### **Ejercicio 10: Sistema de votación electrónica 🗳️** *(Uso de `FOR` y `WHILE` anidado para validar votos)*  
📌 **Enunciado:**  
Un programa permite que `N` personas voten por **tres candidatos** (`A`, `B` y `C`).  
- Cada persona **debe ingresar su voto válido** (`A`, `B` o `C`).  
- Si el voto es inválido, se le pedirá al usuario que vuelva a intentarlo hasta ingresar una opción válida.  
- Al final, el sistema muestra los resultados y el candidato ganador.  

🔹 **Debe utilizar:**  
- `FOR` para recorrer cada votante.  
- `WHILE` anidado dentro del `FOR` para validar cada voto.  

---

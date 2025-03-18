# **Ciclos en Programación: "Enunciados del Mundo Real" 🚀**

- **FOR**: Cuando sabemos cuántas iteraciones deben realizarse.  
- **WHILE**: Cuando la repetición depende de una condición.  
- **WHILE TRUE**: Cuando queremos asegurarnos de que el código se ejecute al menos una vez y controlamos la salida con `break`.  

---

### **Ejercicio 1: Control de temperatura en un invernadero 🌱** *(Uso de `WHILE TRUE`)*  
📌 **Enunciado:**  
Un invernadero tiene un sensor que mide la temperatura cada minuto. Si la temperatura baja de `15°C`, se enciende la calefacción, y si sube de `30°C`, se activa la ventilación.  
El programa debe repetirse hasta que el usuario decida finalizar ingresando `"N"`.  

🔹 **Debe utilizar** `WHILE TRUE` para ejecutar continuamente el monitoreo y salir con `break`.

---

### **Ejercicio 2: Cajero automático 🏦** *(Uso de `WHILE` y `WHILE TRUE`)*  
📌 **Enunciado:**  
Diseña un programa que simule un cajero automático. El usuario debe ingresar su clave.  
- Si la clave es incorrecta más de **3 veces**, la cuenta se bloquea.  
- Si es correcta, el usuario podrá elegir entre **consultar saldo, retirar dinero o salir**.  

🔹 **Debe utilizar:**  
- `WHILE` para controlar los intentos de ingreso de clave.  
- `WHILE TRUE` dentro del menú de opciones para que se ejecute hasta que el usuario elija salir.

---

### **Ejercicio 3: Registro de asistencia en una escuela 📚** *(Uso de `FOR`)*  
📌 **Enunciado:**  
Crea un programa que registre la asistencia de `N` estudiantes en una clase.  
- Por cada estudiante, el usuario debe ingresar `"P"` (presente) o `"A"` (ausente).  
- Al final, el programa muestra cuántos estudiantes asistieron y cuántos faltaron.  

🔹 **Debe utilizar** `FOR`, ya que sabemos exactamente cuántos estudiantes hay y necesitamos recorrerlos.

---

### **Ejercicio 4: Sistema de peaje 🚗** *(Uso de `WHILE TRUE`)*  
📌 **Enunciado:**  
Un peaje cobra a los conductores según el tipo de vehículo:  
- **Moto:** $2,000  
- **Carro:** $5,000  
- **Camión:** $10,000  

El programa debe repetirse hasta que el usuario ingrese `"Salir"`.

🔹 **Debe utilizar** `WHILE TRUE` porque el número de vehículos que pasan es **indeterminado** y el ciclo debe ejecutarse hasta que el usuario decida salir.

---

### **Ejercicio 5: Control de acceso a un edificio 🏢** *(Uso de `WHILE`)*  
📌 **Enunciado:**  
Un sistema de seguridad controla el acceso a un edificio. Los empleados deben ingresar su número de identificación y una clave.  
- Si la clave es incorrecta **más de 3 veces**, el acceso se bloquea.  
- Si es correcta, el programa muestra un mensaje de bienvenida y finaliza.  

🔹 **Debe utilizar** `WHILE`, ya que el número de intentos es **limitado**.

---

### **Ejercicio 6: Máquina de boletos para el metro 🚆** *(Uso de `WHILE TRUE`)*  
📌 **Enunciado:**  
Una máquina de boletos vende tres tipos de pasajes:  
- **Normal:** $2,500  
- **Estudiante:** $1,500  
- **Tercera edad:** $1,000  

El usuario puede comprar varios boletos hasta que ingrese `"Finalizar"`.  
El programa debe calcular el total y solicitar el pago exacto antes de cerrar la compra.

🔹 **Debe utilizar** `WHILE TRUE` porque la cantidad de boletos comprados es **indeterminada** y el usuario decide cuándo detenerse.

---

### **Ejercicio 7: Tienda en línea con carrito de compras 🛒** *(Uso de `WHILE`)*  
📌 **Enunciado:**  
Un usuario puede agregar productos a un carrito de compras ingresando su precio.  
Cuando el usuario finalice la compra (ingresando `0`), el programa debe mostrar el total y pedir confirmación antes de proceder con el pago.

🔹 **Debe utilizar** `WHILE` porque no sabemos cuántos productos comprará, pero el ciclo debe **terminar cuando el usuario ingrese `0`**.

---

### **Ejercicio 8: Evaluación de alumnos en un curso 🎓** *(Uso de `FOR`)*  
📌 **Enunciado:**  
Un profesor registra las calificaciones de `N` estudiantes.  
- Para aprobar, un estudiante debe obtener una calificación **mayor o igual a 60**.  
- Al final, el programa muestra cuántos estudiantes aprobaron y cuántos reprobaron.  

🔹 **Debe utilizar** `FOR` porque la cantidad de estudiantes es **determinada** y se necesita procesar cada nota.

---

### **Ejercicio 9: Parqueadero con espacios limitados 🚘** *(Uso de `WHILE`)*  
📌 **Enunciado:**  
Un parqueadero tiene `20` espacios disponibles.  
- Cada vez que un vehículo **entra**, los espacios disponibles disminuyen.  
- Si un vehículo **sale**, los espacios aumentan.  
- **No puede permitir más autos si el parqueadero está lleno**.  
- El programa debe ejecutarse hasta que el usuario ingrese `"Salir"`.  

🔹 **Debe utilizar** `WHILE` porque la cantidad de autos que entran y salen **es variable**, pero hay una condición de **límite de espacios**.

---

### **Ejercicio 10: Sistema de votación electrónica 🗳️** *(Uso de `FOR` y `WHILE`)*  
📌 **Enunciado:**  
Un programa permite que `N` personas voten por **tres candidatos** (`A`, `B` y `C`).  
- Cada persona **debe ingresar su voto válido** (`A`, `B` o `C`).  
- Si el voto es inválido, se le pedirá al usuario que vuelva a intentarlo hasta ingresar una opción válida.  
- Al final, el sistema muestra la cantidad de votos obtenidos por cada candidato y el nombre del ganador.  
- **Si hay empate, debe indicarlo.**  

🔹 **Debe utilizar:**  
- `FOR` para recorrer cada votante (sabemos cuántos hay).  
- `WHILE` dentro del `FOR` para validar que cada persona vote correctamente.  

---

## **📌 Resumen del uso de ciclos en cada ejercicio:**  

| **Ejercicio** | **Ciclo utilizado** |
|--------------|----------------|
| Control de temperatura 🌱 | `WHILE TRUE` |
| Cajero automático 🏦 | `WHILE` + `WHILE TRUE` |
| Registro de asistencia 📚 | `FOR` |
| Sistema de peaje 🚗 | `WHILE TRUE` |
| Control de acceso 🏢 | `WHILE` |
| Máquina de boletos 🚆 | `WHILE TRUE` |
| Tienda en línea 🛒 | `WHILE` |
| Evaluación de alumnos 🎓 | `FOR` |
| Parqueadero 🚘 | `WHILE` |
| Sistema de votación 🗳️ | `FOR` + `WHILE` |

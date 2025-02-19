---
# 📌 Introducción a Python

## 🐍 ¿Qué es Python?

Python es un **lenguaje de programación interpretado, de alto nivel y multiparadigma**, diseñado para ser fácil de leer y escribir. Es ampliamente utilizado en diversas áreas como desarrollo web, análisis de datos, inteligencia artificial y automatización.

### 📜 Características de Python:
✅ **Sintaxis sencilla y clara**: Su código es fácil de leer y escribir.  
✅ **Interpretado**: No requiere compilación, se ejecuta directamente.  
✅ **Multiparadigma**: Soporta programación **imperativa, orientada a objetos y funcional**.  
✅ **Extensible y embebible**: Puede integrarse con otros lenguajes como C y Java.  
✅ **Gran comunidad y librerías**: Existen muchas bibliotecas disponibles para diversas tareas.

---

## 🔧 ¿Cómo funciona Python?

Python es un lenguaje **interpretado**, lo que significa que su código se ejecuta línea por línea en un **intérprete** en lugar de ser compilado a código máquina previamente.

### 🔹 Proceso de ejecución de un programa en Python:
1. **Escribimos el código fuente** en un archivo `.py`.
2. **El intérprete de Python lee el código** y lo traduce a un formato intermedio llamado **bytecode**.
3. **El bytecode es ejecutado por la máquina virtual de Python (PVM)**, que interpreta cada instrucción y la ejecuta en el sistema operativo.

📌 Ejemplo de código básico en Python:
```python
print("¡Hola, mundo!")
```

Al ejecutar este código, el intérprete mostrará:
```
¡Hola, mundo!
```

---

## ⚙️ Generalidades de Python

### 🔹 **Tipado Dinámico**
Python no requiere declarar el tipo de una variable, ya que lo asigna automáticamente en tiempo de ejecución.
```python
x = 10  # Entero
x = "Python"  # Ahora es una cadena
```

### 🔹 **Indentación Obligatoria**
Python usa **indentación** en lugar de llaves `{}` para definir bloques de código, lo que mejora la legibilidad.
```python
if True:
    print("Esto está indentado correctamente")
```
❌ Si la indentación es incorrecta, Python generará un error.

### 🔹 **Multiparadigma**
Python permite programar en distintos estilos:
- **Imperativo** (estructurado con variables y control de flujo).
- **Orientado a objetos** (usando clases y objetos).
- **Funcional** (usando funciones como elementos de primera clase).

### 🔹 **Interpretado e Interactivo**
Puedes ejecutar Python línea por línea en un **entorno interactivo (REPL)** simplemente escribiendo `python` en la terminal.
```python
>>> 2 + 2
4
```

---

## 🚀 Aplicaciones de Python
Python se usa en muchas áreas de la informática, como:

🔹 **Desarrollo Web** → Django, Flask.  
🔹 **Ciencia de Datos** → Pandas, NumPy, Matplotlib.  
🔹 **Inteligencia Artificial y Machine Learning** → TensorFlow, Scikit-Learn.  
🔹 **Automatización y Scripting** → Manipulación de archivos, procesos repetitivos.  
🔹 **Ciberseguridad** → Análisis de seguridad, pruebas de penetración.  
🔹 **Desarrollo de Juegos** → Pygame, Panda3D.  

---

## 🛠 Instalación y Primeros Pasos

### 🔹 **Instalar Python**
1. Descarga la última versión desde [python.org](https://www.python.org/).
2. Asegúrate de marcar la opción **"Add Python to PATH"** al instalar.
3. Verifica la instalación ejecutando:
   ```bash
   python --version
   ```

### 🔹 **Ejecutar un Script en Python**
Guarda un archivo con extensión `.py` y ejecútalo desde la terminal:
```bash
python mi_programa.py
```

### 🔹 **Usar el intérprete interactivo (REPL)**
Para probar código rápidamente, abre la terminal y escribe:
```bash
python
```
Luego, puedes escribir código directamente:
```python
>>> print("Hola, Python")
Hola, Python
```

---

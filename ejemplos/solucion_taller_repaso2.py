# =========================================================
# SOLUCIONES — Taller de Repaso (Primer Semestre)
# =========================================================
# Reglas seguidas:
# - Sin librerías externas.
# - Solo estructuras básicas: if/elif/else, for/while, listas y matrices.
# - En general, se retornan resultados en lugar de imprimir para facilitar pruebas.
# =========================================================

# -----------------------------
# 1) CONDICIONALES
# -----------------------------

def tarifa_transporte(edad, es_estudiante):
    """
    Retorna la tarifa (int). Si es gratis, retorna 0 (el llamador decide imprimir "Gratis").
    Reglas:
    - <5: 0
    - 5–18: 2500
    - >18 y estudiante: 3000
    - >18 y no estudiante: 3500
    """
    e = 0
    if edad < 5:
        e = 0
    else:
        es_est = (es_estudiante == "si" or es_estudiante == "SI" or es_estudiante == "Si")
        if edad <= 18:
            e = 2500
        else:
            if es_est:
                e = 3000
            else:
                e = 3500
    return e

def total_libreria_con_descuento(monto, tiene_carnet):
    """
    Aplica:
    - monto >= 100000 => 15%
    - monto >= 50000  => 10%
    - adicional carnet 'si' => +5%
    Retorna entero truncado hacia abajo.
    """
    base = 0.0
    if monto >= 100000:
        base = 0.15
    else:
        if monto >= 50000:
            base = 0.10
        else:
            base = 0.0

    extra = 0.0
    if tiene_carnet == "si" or tiene_carnet == "SI" or tiene_carnet == "Si":
        extra = 0.05

    desc = base + extra
    total = monto - (monto * desc)
    return int(total)

def clasificar_nota(nota):
    """
    Retorna: "Bajo", "Básico", "Alto", "Superior" según:
    - Bajo:    < 3.0
    - Básico:  3.0–3.4
    - Alto:    3.5–4.4
    - Superior:4.5–5.0
    """
    if nota < 3.0:
        return "Bajo"
    else:
        if nota <= 3.4:
            return "Básico"
        else:
            if nota <= 4.4:
                return "Alto"
            else:
                return "Superior"

# # Ejemplos rápidos:
# print(tarifa_transporte(3, "no"))  # 0 (Gratis)
# print(tarifa_transporte(15, "si")) # 2500
# print(total_libreria_con_descuento(120000, "si"))  # 96000
# print(clasificar_nota(4.7))  # "Superior"


# -----------------------------
# 2) CICLOS (while / for)
# -----------------------------

def semanas_para_meta(meta, ahorro_semanal):
    """
    Simula ahorro semanal hasta alcanzar la meta.
    Retorna el número de semanas.
    Supone meta > 0 y ahorro_semanal > 0.
    """
    acumulado = 0
    semanas = 0
    while acumulado < meta:
        acumulado = acumulado + ahorro_semanal
        semanas = semanas + 1
    return semanas

def contar_digitos(n):
    """
    Retorna la cantidad de dígitos de un entero positivo.
    No convierte a string.
    Si n == 0, retorna 1.
    """
    if n == 0:
        return 1
    if n < 0:
        n = -n
    c = 0
    while n > 0:
        n = n // 10
        c = c + 1
    return c

def tabla_multiplicar(n):
    """
    Retorna una lista de strings con la forma "n x i = r" para i=1..10.
    """
    lineas = []
    i = 1
    while i <= 10:
        r = n * i
        # Sin f-strings también sería válido; aquí usamos lo básico de formateo.
        linea = str(n) + " x " + str(i) + " = " + str(r)
        lineas.append(linea)
        i = i + 1
    return lineas

# # Ejemplos:
# print(semanas_para_meta(100000, 15000))  # 7
# print(contar_digitos(12345))  # 5
# print("\n".join(tabla_multiplicar(4)))


# -----------------------------
# 3) CICLOS ANIDADOS
# -----------------------------

def calendario_simplificado(semanas, dias_por_semana):
    """
    Retorna lista de líneas "Semana s — Día d" para s=1..semanas, d=1..dias_por_semana.
    """
    res = []
    s = 1
    while s <= semanas:
        d = 1
        while d <= dias_por_semana:
            res.append("Semana " + str(s) + " — Día " + str(d))
            d = d + 1
        s = s + 1
    return res

def cuadricula_inventario(filas, columnas):
    """
    Retorna una lista de strings donde cada string es una fila:
    'F1C1 F1C2 ...'
    """
    out = []
    f = 1
    while f <= filas:
        fila_str = ""
        c = 1
        while c <= columnas:
            codigo = "F" + str(f) + "C" + str(c)
            if c == 1:
                fila_str = codigo
            else:
                fila_str = fila_str + " " + codigo
            c = c + 1
        out.append(fila_str)
        f = f + 1
    return out

# # Ejemplos:
# print("\n".join(calendario_simplificado(2, 3)))
# print("\n".join(cuadricula_inventario(3, 4)))


# -----------------------------
# 4) LISTAS
# -----------------------------

def total_y_promedio(valores):
    """
    Recibe una lista de enteros (>=1 elemento).
    Retorna (total:int, promedio:int truncado).
    """
    total = 0
    i = 0
    while i < len(valores):
        total = total + valores[i]
        i = i + 1
    prom = total // len(valores)
    return total, prom

def temperaturas_resumen(temperaturas):
    """
    Recibe lista de floats (>=1).
    Retorna (maximo, minimo, fuera_de_rango) siendo el rango [18, 28].
    """
    maximo = temperaturas[0]
    minimo = temperaturas[0]
    fuera = 0
    i = 0
    while i < len(temperaturas):
        t = temperaturas[i]
        if t > maximo:
            maximo = t
        if t < minimo:
            minimo = t
        if t < 18 or t > 28:
            fuera = fuera + 1
        i = i + 1
    return maximo, minimo, fuera

def buscar_producto(nombres, objetivo):
    """
    Búsqueda lineal. Retorna índice si lo encuentra; -1 si no.
    Comparación exacta (sensible a mayúsculas/minúsculas).
    """
    i = 0
    while i < len(nombres):
        if nombres[i] == objetivo:
            return i
        i = i + 1
    return -1

# # Ejemplos:
# print(total_y_promedio([10000, 8000, 0, 7000]))  # (25000, 6250)
# print(temperaturas_resumen([20, 17, 28, 30]))     # (30, 17, 2)
# print(buscar_producto(["teclado", "mouse", "monitor"], "mouse"))  # 1


# -----------------------------
# 5) MATRICES (listas de listas)
# -----------------------------

def ventas_trimestrales_resumen(matriz):
    """
    matriz: lista de filas (departamentos), cada fila con c trimestres (enteros).
    Retorna (totales_fila, totales_col, idx_mayor_fila).
    """
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return [], [], -1

    filas = len(matriz)
    columnas = len(matriz[0])

    # Totales por fila
    totales_fila = []
    f = 0
    while f < filas:
        suma = 0
        c = 0
        while c < columnas:
            suma = suma + matriz[f][c]
            c = c + 1
        totales_fila.append(suma)
        f = f + 1

    # Totales por columna
    totales_col = []
    c = 0
    while c < columnas:
        suma_col = 0
        f = 0
        while f < filas:
            suma_col = suma_col + matriz[f][c]
            f = f + 1
        totales_col.append(suma_col)
        c = c + 1

    # Índice de la fila con mayor total
    idx_mayor = 0
    i = 1
    while i < len(totales_fila):
        if totales_fila[i] > totales_fila[idx_mayor]:
            idx_mayor = i
        i = i + 1

    return totales_fila, totales_col, idx_mayor

def ocupacion_salas(matriz01):
    """
    matriz01: matriz de 0/1.
    Retorna (porcentaje_total:int, porcentajes_por_fila:list[int]).
    El porcentaje es truncado (entero).
    """
    if len(matriz01) == 0 or len(matriz01[0]) == 0:
        return 0, []

    filas = len(matriz01)
    columnas = len(matriz01[0])

    # Total ocupadas y total celdas
    ocupadas = 0
    f = 0
    while f < filas:
        c = 0
        while c < columnas:
            if matriz01[f][c] == 1:
                ocupadas = ocupadas + 1
            c = c + 1
        f = f + 1

    total_celdas = filas * columnas
    porcentaje_total = int((ocupadas * 100) // total_celdas)

    # Porcentajes por fila
    porcentajes = []
    f = 0
    while f < filas:
        ocup_fila = 0
        c = 0
        while c < columnas:
            if matriz01[f][c] == 1:
                ocup_fila = ocup_fila + 1
            c = c + 1
        p_fila = int((ocup_fila * 100) // columnas)
        porcentajes.append(p_fila)
        f = f + 1

    return porcentaje_total, porcentajes

# # Ejemplos:
# m = [[100, 120, 110],
#      [ 90,  95, 105]]
# print(ventas_trimestrales_resumen(m))  # ([330, 290], [190, 215, 215], 0)
#
# a = [[1,0,1],
#      [0,1,0],
#      [1,1,0]]
# print(ocupacion_salas(a))  # (55, [66, 33, 66])


# -----------------------------
# 6) FUNCIONES
# -----------------------------

def calcular_imc(peso, estatura):
    """
    Retorna (imc_float, categoria_str).
    Categorías:
    - <18.5: Bajo
    - 18.5–24.9: Normal
    - 25–29.9: Sobrepeso
    - >=30: Obesidad
    """
    imc = peso / (estatura * estatura)
    cat = ""
    if imc < 18.5:
        cat = "Bajo"
    else:
        if imc < 25.0:
            cat = "Normal"
        else:
            if imc < 30.0:
                cat = "Sobrepeso"
            else:
                cat = "Obesidad"
    return imc, cat

def aplicar_descuento(monto, porcentaje):
    """
    Retorna monto con descuento aplicado (entero truncado).
    """
    descuento = (monto * porcentaje) / 100.0
    total = monto - descuento
    return int(total)

def promedio_lista(lista_enteros):
    """
    Retorna el promedio entero truncado.
    """
    if len(lista_enteros) == 0:
        return 0
    s = 0
    i = 0
    while i < len(lista_enteros):
        s = s + lista_enteros[i]
        i = i + 1
    return s // len(lista_enteros)

# # Ejemplos:
# print(calcular_imc(70, 1.75))  # (~22.857..., "Normal")
# print(aplicar_descuento(100000, 12))  # 88000
# print(promedio_lista([10, 20, 30]))   # 20


# -----------------------------
# 7) INTEGRADOR — Cafetería Universitaria
# -----------------------------

def total_dia(fila):
    """
    Suma los dos turnos (o n turnos si la fila tiene más columnas).
    """
    s = 0
    i = 0
    while i < len(fila):
        s = s + fila[i]
        i = i + 1
    return s

def total_semanal(matriz):
    """
    Suma de todos los días/turnos.
    """
    s = 0
    f = 0
    while f < len(matriz):
        s = s + total_dia(matriz[f])
        f = f + 1
    return s

def conteo_umbral(matriz, umbral):
    """
    Cuenta cuántas celdas superan el umbral (strictamente > umbral).
    """
    celdas = 0
    f = 0
    while f < len(matriz):
        c = 0
        while c < len(matriz[f]):
            if matriz[f][c] > umbral:
                celdas = celdas + 1
            c = c + 1
        f = f + 1
    return celdas

def indice_dia_mayor(matriz):
    """
    Retorna el índice del día (fila) con mayor venta total.
    En caso de empate, retorna el primero.
    Si matriz vacía, retorna -1.
    """
    if len(matriz) == 0:
        return -1
    idx = 0
    mayor = total_dia(matriz[0])
    f = 1
    while f < len(matriz):
        t = total_dia(matriz[f])
        if t > mayor:
            mayor = t
            idx = f
        f = f + 1
    return idx

def imprimir_matriz_como_lineas(matriz):
    """
    Devuelve una lista de strings formateados 'v1 v2 ...' por fila.
    (No imprime en pantalla para facilitar pruebas).
    """
    out = []
    f = 0
    while f < len(matriz):
        linea = ""
        c = 0
        while c < len(matriz[f]):
            val = str(matriz[f][c])
            if c == 0:
                linea = val
            else:
                linea = linea + " " + val
            c = c + 1
        out.append(linea)
        f = f + 1
    return out

# # Ejemplo integrador (prueba rápida del enunciado):
# ventas = [
#     [30000, 20000],  # L
#     [25000, 35000],  # M
#     [40000, 15000],  # X
#     [20000, 20000],  # J
#     [50000, 30000]   # V
# ]
# umbral = 30000
# print("\n".join(imprimir_matriz_como_lineas(ventas)))
# # Totales por día:
# totales = []
# i = 0
# while i < len(ventas):
#     totales.append(total_dia(ventas[i]))
#     i = i + 1
# print("Totales por día:", totales)           # [50000, 60000, 55000, 40000, 80000]
# print("Total semanal:", total_semanal(ventas))  # 285000
# print("Día mayor:", indice_dia_mayor(ventas))   # 4
# print("Celdas > umbral:", conteo_umbral(ventas, umbral))  # 4

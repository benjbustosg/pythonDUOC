# 1. Definimos la función (La "regla" matemática)
def calcular_tiempo(n):
    # La fórmula es: 3 por n, más 5
    return 3 * n + 5

# 2. Definimos tu número objetivo (n)
elementos = 101

# 3. La "Sustitución": Llamamos a la función con ese número
resultado = calcular_tiempo(elementos)

# 4. Mostramos la respuesta
print(f"Para {elementos} elementos, tardara {resultado} ms")



print("-------------------------------------------------------------")




import math

def calcular_usuarios(tiempo_meses):
    # La fórmula del problema: 1000 * e^(0.1 * t)
    # math.exp(x) es como se escribe e^x en Python
    usuarios = 1000 * math.exp(0.1 * tiempo_meses)
    return usuarios

# Paso clave: Convertir 1 año a 12 meses
meses = 12
resultado = calcular_usuarios(meses)

print(f"En {meses} meses (1 año), habrá aproximadamente: {resultado} usuarios.")
# Esto imprimirá: 3320.1169... -> Redondeado es 3320




print("--------------------------------------------------------------")



import math

def calcular_tiempo_crecimiento():
    # DATOS DEL PROBLEMA
    # Fórmula: D(t) = 2 * 1.2^t
    meta_tb = 20    # Queremos llegar a 20 TB
    inicial_tb = 2  # Empezamos con 2 TB
    base = 1.2      # Tasa de crecimiento
    
    # PASO 1: Simplificar la ecuación
    # 20 = 2 * 1.2^t  --->  10 = 1.2^t
    # Dividimos la meta entre el valor inicial
    ratio = meta_tb / inicial_tb  # Esto da 10
    
    # PASO 2: Aplicar la fórmula del logaritmo
    # Matemáticamente: t = ln(10) / ln(1.2)
    # En Python: math.log() calcula el logaritmo natural
    tiempo = math.log(ratio) / math.log(base)
    
    return tiempo

# Ejecutamos la función
t = calcular_tiempo_crecimiento()

print(f"Resultado exacto: {t}")

# PASO 3: Formatear para la respuesta del examen
# Redondear a 2 decimales
redondeado = round(t, 2)

# Convertir a texto y cambiar punto por coma (formato español)
respuesta_final = str(redondeado).replace('.', ',')

print(f"deben pasar {respuesta_final} años para que la base de datos llegue a los 20TB")




print("-----------------------------------------------------------------")




import numpy as np

def resolver_examen():
    # ECUACIONES DEL PROBLEMA:
    # 1) 4x + 8y = 72
    # 2) 2x + 6y = 40
    
    # MATRIZ A (Los números que acompañan a las letras)
    # [Fila 1, Fila 2]
    A = np.array([
        [4, 8], 
        [2, 6]
    ])
    
    # MATRIZ B (Los resultados finales)
    B = np.array([72, 40])
    
    # RESOLVER
    # Esta función busca los valores de X e Y automáticamente
    solucion = np.linalg.solve(A, B)
    
    # Imprimir
    x = solucion[0] # Estaciones
    y = solucion[1] # Servidores
    
    print(f"Solución encontrada:")
    print(f"Estaciones de trabajo: {x}")
    print(f"Servidores: {y}")

# Ejecutar
resolver_examen()

print("--------------------------------------------------------------")



def resolver_pregunta_20():
    # --- DATOS DEL PROBLEMA ---
    inversionista = 8
    dia = 3  # Lunes=1, Martes=2, Miercoles=3
    
    # Número de tipos de acciones (es la dimensión compartida)
    # Matriz A es 15x10, Matriz E es 10x5 -> El nexo es 10.
    total_acciones = 10
    
    suma_total = 0
    
    print(f"Calculando ticket para Inversionista {inversionista} en el Día {dia}...")
    
    # Recorremos las 10 acciones (del 1 al 10)
    for k in range(1, total_acciones + 1):
        
        # 1. CALCULAR CANTIDAD (Matriz A)
        # Fórmula: a_ij = 20 * i * j
        # OJO: Aquí 'i' es el inversionista (8) y 'j' es la acción (k)
        cantidad = 20 * inversionista * k
        
        # 2. CALCULAR PRECIO (Matriz E)
        # Fórmula: e_ij = 4 * i * j
        # OJO: Aquí 'i' es la acción (k) y 'j' es el día (3)
        precio = (4 * k) + dia
        
        # 3. SUBTOTAL (Cantidad * Precio)
        subtotal = cantidad * precio
        
        # Acumulamos al total
        suma_total += subtotal
        
        # (Opcional) Ver el paso a paso
        # print(f"Acción {k}: {cantidad} unidades a ${precio} = ${subtotal}")

    return suma_total

# Ejecutar
resultado = resolver_pregunta_20()

print("-" * 30)
print(f"VALOR TOTAL DE LA CARTERA: {resultado} euros")

print("--OTRA POSIBLE RESPUESTA A LA PREGUNTA ANTERIOR--")

# Definimos las variables fijas del problema
inversionista = 8
dia = 3
suma_total = 0

print(f"{'Acción':^6} | {'Cantidad':^8} | {'Precio':^6} | {'Subtotal':^10}")
print("-" * 40)

# Hacemos un ciclo simple del 1 al 10
for accion in range(1, 11):
    
    # 1. Calculamos la Cantidad (Columna 1)
    # Fórmula A: 20 * inversionista * accion
    cantidad = 20 * inversionista * accion
    
    # 2. Calculamos el Precio (Columna 2)
    # Fórmula E: 4 * accion + dia
    precio = 4 * accion + dia
    
    # 3. Multiplicamos (Columna 3)
    subtotal = cantidad * precio
    
    # 4. Acumulamos en la bolsa total
    suma_total = suma_total + subtotal
    
    # Mostramos la fila de la tabla para verificar
    print(f"{accion:^6} | {cantidad:^8} | {precio:^6} | {subtotal:^10}")

print("-" * 40)
print(f"RESPUESTA FINAL: {suma_total}")
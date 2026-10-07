print("Karla Saenz 0133 NL 52 ")
# ==============================================================================
# EJERCICIOS DE PYTHON - ESTRUCTURAS DE CONTROL Y BUCLES
# Nota: Configurado para 1 ejemplo por caso.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. PYTHON CONDITIONS & IF STATEMENTS (Condicional simple)
# ------------------------------------------------------------------------------
print("--- 1. Conditions & If ---")

# Ejemplo 1: Verificación simple si un número es mayor que otro
a = 33
b = 200
if b > a:
    print("b es mayor que a")

print("\n" + "="*50 + "\n")


# ------------------------------------------------------------------------------
# 2. PYTHON IF ... ELIF (Condicional múltiple)
# ------------------------------------------------------------------------------
print("--- 2. If ... Elif ---")

# Ejemplo 1: Evaluar si dos variables son iguales cuando no se cumple el if inicial
x = 33
y = 33
if y > x:
    print("y es mayor que x")
elif x == y:
    print("x e y son iguales")

print("\n" + "="*50 + "\n")


# ------------------------------------------------------------------------------
# 3. PYTHON IF ... ELSE (Condicional completo / caso por defecto)
# ------------------------------------------------------------------------------
print("--- 3. If ... Else ---")

# Ejemplo 1: Evaluación con alternativa final (else)
temperatura = 18
if temperatura >= 25:
    print("Hace calor afuera.")
else:
    print("El clima está fresco o frío.")

print("\n" + "="*50 + "\n")

# ------------------------------------------------------------------------------
# 4. PYTHON FOR LOOPS (Bucle For)
# ------------------------------------------------------------------------------
print("--- 4. For Loops ---")

# Ejemplo 1: Recorrer una lista de elementos
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

print("\n" + "="*50 + "\n")

# ------------------------------------------------------------------------------
# 5. PYTHON WHILE LOOPS (Bucle While)
# ------------------------------------------------------------------------------
print("--- 5. While Loops ---")

# Ejemplo 1: Bucle con contador mientras se cumpla la condición
i = 1
while i <= 5:
    print(f"Iteración número: {i}")
    i += 1  # Incremento del contador para evitar un bucle infinito
print("Karla Saenz 0133  NL 52")
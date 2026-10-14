# Archivo principal: calculadora_imc.py
# 1. Captura de datos desde el teclado (se esperan strings inicialmente)
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")

# Captura de datos numéricos y 2. Realización del casting (conversión de tipos)
edad = int(input("Ingresa tu edad: "))  # int: entero
peso = float(input("Ingresa tu peso en kg: "))  # float: decimal
estatura = float(input("Ingresa tu estatura en metros (ej. 1.91): "))  # float: decimal

# 3. Aplicación de la fórmula del IMC
# IMC = peso / (estatura^2)
imc = peso / (estatura ** 2)

# Mostrar resultados en consola
print("\n--- Resultados del IMC ---")
print(f"Usuario: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg | Estatura: {estatura} m")
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

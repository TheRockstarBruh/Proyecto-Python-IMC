# 1. Captura de datos desde el teclado
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")

# Captura de datos numéricos y realización del casting
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros (ej. 1.91): "))

# 3. Aplicación de la fórmula del IMC y redondeo a dos decimales
imc = round(peso / (estatura ** 2), 2)

# Formateo de cadenas: asegurando la primera letra en mayúscula con .title()
nombre_fmt = nombre.strip().title()
apellido_paterno_fmt = apellido_paterno.strip().title()
apellido_materno_fmt = apellido_materno.strip().title()

# 2 y 4. Uso de f-strings para desplegar el resumen de datos limpio y legible
print("\n" + "="*30)
print(f"{'RESUMEN DE DATOS - IMC':^30}")
print("="*30)
print(f"Nombre completo : {nombre_fmt} {apellido_paterno_fmt} {apellido_materno_fmt}")
print(f"Edad            : {edad} años")
print(f"Peso            : {peso} kg")
print(f"Estatura        : {estatura} m")
print(f"Tu IMC final    : {imc}")
print("="*30)

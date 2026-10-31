
def pedir_cadena(mensaje):
    """Solicita un texto y valida que no esté vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede estar vacío. Inténtalo de nuevo.")

def pedir_entero(mensaje):
    """Solicita un número entero y evita que el programa colapse si se ingresan letras."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: Este campo no puede estar vacío.")
            continue
        try:
            return int(valor)
        except ValueError:
            print("Error: Debes ingresar un número entero válido (ej. 28).")

def pedir_flotante(mensaje):
    """Solicita un número decimal y evita que el programa colapse si se ingresan letras."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: Este campo no puede estar vacío.")
            continue
        try:
            return float(valor)
        except ValueError:
            print("Error: Debes ingresar un número válido (ej. 1.91 o 112.5).")

# Captura de datos con validaciones integradas
nombre = pedir_cadena("Ingresa tu nombre: ")
apellido_paterno = pedir_cadena("Ingresa tu apellido paterno: ")
apellido_materno = pedir_cadena("Ingresa tu apellido materno: ")

edad = pedir_entero("Ingresa tu edad: ")
peso = pedir_flotante("Ingresa tu peso en kg: ")
estatura = pedir_flotante("Ingresa tu estatura en metros (ej. 1.91): ")

# Aplicación de la fórmula del IMC y redondeo a dos decimales
imc = round(peso / (estatura ** 2), 2)

# Formateo de cadenas: iniciales en mayúscula
nombre_fmt = nombre.title()
apellido_paterno_fmt = apellido_paterno.title()
apellido_materno_fmt = apellido_materno.title()

# Despliegue de datos usando f-strings
print("\n" + "="*30)
print(f"{'RESUMEN DE DATOS - IMC':^30}")
print("="*30)
print(f"Nombre completo : {nombre_fmt} {apellido_paterno_fmt} {apellido_materno_fmt}")
print(f"Edad            : {edad} años")
print(f"Peso            : {peso} kg")
print(f"Estatura        : {estatura} m")
print(f"Tu IMC final    : {imc}")
print("="*30)

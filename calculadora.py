import math

# Mensaje de bienvenida
print("Bienvenida a la Calculadora Python")

# Menú de opciones
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Exponenciación")
print("6. Raíz Cuadrada")

# Solicitar al usuario seleccionar una operación
operacion = int(input("Seleccione una operación (1-6): "))

# Solicitar los números de entrada para las operaciones
if operacion == 1:
    #operación de suma para Naima
    print("Agregar la operación de suma")

elif operacion == 2:
    #operación de resta para Milena
    print("Agregar la operación de resta")

elif operacion == 3:
    #operación de multiplicación para Lucety
    print("Agregar la operación de multiplicación")

elif operacion == 4:
    #operación de división validar división cero, para Paula
    print("Agregar la operación de división")

elif operacion == 5:
    #operación de exponenciación para Fransheska
    print("Agregar la operación de exponenciación")

elif operacion == 6:
    #operación de raíz cuadrada validando que no se puede realizar a negativos, para Layla
    try:
        num = float(input("Ingrese el número para calcular la raíz cuadrada: "))
        if num < 0:
            print("Error: no se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = math.sqrt(num)
            print(f"La raíz cuadrada de {num} es {resultado}")
    except ValueError:
        print("Entrada no válida. Introduzca un número.")

else:
    print("Opción no válida. Por favor seleccione una operación entre 1 y 6.")
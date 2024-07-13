
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Consideraciones para las operaciones
    # 2. Debe controlar la división entre cero
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def solicitar_numero(mensaje):
    # Consideraciones para las operaciones
    while True:
        try:
            numero = float(input(mensaje))  # 1. Intenta convertir la entrada a float
            if numero < 0: # 3. No debe permitir números negativos
                raise ValueError("El número no puede ser negativo")
            return numero
        except ValueError as e: # Mensaje de error si se ingresa letra o numero negativo
            print(e)

def menu_calculadora():
    while True:
        print("\nCalculadora Basica:")
        print("\nIndique la operación a realizar:")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Salir de la calculadora")

        opcion = input()
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = solicitar_numero("Introduzca el primer número: ")
            num2 = solicitar_numero("Introduzca el segundo número: ")

            if opcion == '1':
                resultado = sumar(num1, num2)
                print(f"La suma de {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = restar(num1, num2)
                print(f"La resta de {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
                print(f"La multiplicación de {num1} * {num2} = {resultado}")
            elif opcion == '4':
                try:
                    resultado = dividir(num1, num2)
                    print(f"La división de {num1} / {num2} = {resultado}")
                except ValueError as e:
                    print(e)
        else:
            # Si coloca un numero distinto a las opciones
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_calculadora()

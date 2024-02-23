def convertir_a_binario(numero):
    """Función recursiva para convertir un número entero a binario."""
    if numero <= 1:
        return str(numero)
    else:
        return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    """Función recursiva para contar la cantidad de dígitos en un número entero."""
    if abs(numero) < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

def calcular_raiz_cuadrada(numero, estimacion=1):
    """Función auxiliar recursiva para encontrar la raíz cuadrada entera de un número."""
    if estimacion * estimacion == numero:
        return estimacion
    elif estimacion * estimacion > numero:
        return estimacion - 1
    else:
        return calcular_raiz_cuadrada(numero, estimacion + 1)

def raiz_cuadrada_entera(numero):
    """Función principal para encontrar la raíz cuadrada entera de un número."""
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada entera de un número negativo."
    else:
        return calcular_raiz_cuadrada(numero)

def convertir_a_decimal(romano):
    """Función recursiva para convertir un número romano a decimal."""
    romano_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return romano_decimal[romano[0]]
    else:
        if romano_decimal[romano[0]] < romano_decimal[romano[1]]:
            return romano_decimal[romano[1]] - romano_decimal[romano[0]] + convertir_a_decimal(romano[2:])
        else:
            return romano_decimal[romano[0]] + convertir_a_decimal(romano[1:])

def suma_numeros_enteros(numero):
    """Función recursiva para sumar todos los números enteros desde cero hasta el número dado."""
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_enteros(numero - 1)

def mostrar_menu():
    """Función para mostrar el menú de opciones."""
    print("Menú de opciones:")
    print("1. Convertir a binario")
    print("2. Contar dígitos")
    print("3. Raíz cuadrada entera")
    print("4. Convertir a decimal desde romano")
    print("5. Suma de números enteros")
    print("6. Salir")

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            numero = int(input("Ingrese un número entero: "))
            print("El número en binario es:", convertir_a_binario(numero))
        elif opcion == '2':
            numero = int(input("Ingrese un número entero: "))
            print("La cantidad de dígitos es:", contar_digitos(numero))
        elif opcion == '3':
            numero = int(input("Ingrese un número entero: "))
            print("La raíz cuadrada entera es:", raiz_cuadrada_entera(numero))
        elif opcion == '4':
            romano = input("Ingrese un número romano: ")
            print("El número en decimal es:", convertir_a_decimal(romano))
        elif opcion == '5':
            numero = int(input("Ingrese un número entero positivo: "))
            print("La suma de todos los números enteros hasta", numero, "es:", suma_numeros_enteros(numero))
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

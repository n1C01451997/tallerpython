def agregar_numero(lista):
    numero = int(input("Ingrese un número para agregar a la lista: "))
    lista.append(numero)
    print(f"Número {numero} agregado a la lista.")

def mostrar_lista(lista):
    print("Lista actual:", lista)

def main():
    numeros = []

    while True:
        print("\nMenú Ejercicio 1:")
        print("1. Agregar número a la lista")
        print("2. Mostrar lista")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_numero(numeros)
        elif opcion == "2":
            mostrar_lista(numeros)
        elif opcion == "0":
            print("Saliendo del ejercicio 1...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

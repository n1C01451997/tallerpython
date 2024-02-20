def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

def agregar_numero(lista):
    numero = int(input("Ingrese un número para agregar a la lista: "))
    lista.append(numero)
    print(f"Número {numero} agregado a la lista.")

def agregar_numero_posicion(lista):
    numero = int(input("Ingrese un número: "))
    posicion = int(input("Ingrese la posición en la que desea agregar el número: "))
    lista.insert(posicion, numero)
    print(f"Número {numero} agregado en la posición {posicion}.")

def obtener_longitud(lista):
    print(f"La longitud de la lista es: {len(lista)}")

def eliminar_ultimo_numero(lista):
    if lista:
        numero_eliminado = lista.pop()
        print(f"Se ha eliminado el último número de la lista: {numero_eliminado}")
    else:
        print("La lista está vacía. No hay números para eliminar.")

def eliminar_numero(lista):
    numero = int(input("Ingrese el número que desea eliminar: "))
    if numero in lista:
        lista.remove(numero)
        print(f"Número {numero} eliminado de la lista.")
    else:
        print("El número ingresado no está en la lista.")

def contar_numeros(lista):
    numero = int(input("Ingrese el número que desea contar: "))
    conteo = lista.count(numero)
    print(f"El número {numero} aparece {conteo} veces en la lista.")

def posiciones_numero(lista):
    numero = int(input("Ingrese el número del que desea conocer las posiciones: "))
    posiciones = [i for i, n in enumerate(lista) if n == numero]
    if posiciones:
        print(f"El número {numero} está en las posiciones: {posiciones}")
    else:
        print(f"El número {numero} no está en la lista.")

def mostrar_numeros(lista):
    print("Lista de números:", lista)

def main():
    lista_numeros = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_numero(lista_numeros)
        elif opcion == "2":
            agregar_numero_posicion(lista_numeros)
        elif opcion == "3":
            obtener_longitud(lista_numeros)
        elif opcion == "4":
            eliminar_ultimo_numero(lista_numeros)
        elif opcion == "5":
            eliminar_numero(lista_numeros)
        elif opcion == "6":
            contar_numeros(lista_numeros)
        elif opcion == "7":
            posiciones_numero(lista_numeros)
        elif opcion == "8":
            mostrar_numeros(lista_numeros)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

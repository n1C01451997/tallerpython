def obtener_precio(fruta, cantidad, precios_frutas):
    if fruta in precios_frutas:
        precio_unitario = precios_frutas[fruta]
        precio_total = precio_unitario * cantidad
        return precio_total
    else:
        return None

def main():
    precios_frutas = {
        'manzana': 2.5,
        'banana': 1.8,
        'naranja': 3.0,
        'pera': 2.0,
        'uva': 4.5
    }

    while True:
        fruta = input("Ingrese el nombre de la fruta: ").lower()
        cantidad = int(input("Ingrese la cantidad vendida: "))

        precio_total = obtener_precio(fruta, cantidad, precios_frutas)

        if precio_total is not None:
            print(f"El precio total de {cantidad} {fruta}(s) es: {precio_total} pesos.")
        else:
            print("La fruta ingresada no está en la lista.")

        continuar = input("¿Desea hacer otra consulta? (Sí/No): ").lower()
        if continuar != "sí" and continuar != "si":  # Consideramos "si" también como una respuesta afirmativa
            break

if __name__ == "__main__":
    main()

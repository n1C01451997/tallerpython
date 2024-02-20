def main():
    cesta_compra = {}

    while True:
        articulo = input("Ingrese el nombre del artículo (o escriba 'terminar' para finalizar): ")
        if articulo.lower() == 'terminar':
            break

        precio = float(input(f"Ingrese el precio de {articulo}: "))
        cesta_compra[articulo] = precio

    print("\nLista de la compra:")
    total = 0
    for i, (articulo, precio) in enumerate(cesta_compra.items(), start=1):
        print(f"{i}. {articulo} ---------- {precio}")
        total += precio

    print(f"\nCoste total de la lista de la compra: {total} pesos.")

if __name__ == "__main__":
    main()

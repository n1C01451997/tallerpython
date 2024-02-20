def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 30000
    else:
        return 50000

def main():
    print("Bienvenido al sistema de cálculo de precio de entrada.")
    edad = int(input("Por favor, ingrese su edad: "))

    precio_entrada = calcular_precio_entrada(edad)

    print(f"\nEl precio de su entrada es: {precio_entrada} pesos.")

if __name__ == "__main__":
    main()

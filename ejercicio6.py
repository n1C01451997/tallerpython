def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total

def main():
    cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))
    porcentaje_iva = float(input("Ingrese el porcentaje de IVA (si no ingresa ninguno, se aplicará el 21% por defecto): ") or 21)

    total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)

    print(f"\nEl total de la factura es: {total_factura} pesos.")

if __name__ == "__main__":
    main()

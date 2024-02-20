def ingresar_notas_alumno():
    notas = []
    while True:
        nota = float(input("Ingrese una nota (ingrese un número negativo para finalizar): "))
        if nota < 0:
            break
        notas.append(nota)
    return notas

def main():
    cantidad_alumnos = int(input("Ingrese el número de alumnos: "))
    alumnos = {}

    for _ in range(cantidad_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print("¡Error! Este nombre ya existe en la lista de alumnos.")
            continue

        print(f"Ingrese las notas del alumno {nombre}:")
        notas = ingresar_notas_alumno()
        alumnos[nombre] = notas

    print("\nLista de alumnos y notas:")
    for nombre, notas in alumnos.items():
        media = sum(notas) / len(notas)
        print(f"{nombre}: {notas} - Nota media: {media}")

if __name__ == "__main__":
    main()

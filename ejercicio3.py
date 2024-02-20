def determinar_grupo(nombre, sexo):
    if (sexo.lower() == 'f' and nombre.lower() < 'm') or (sexo.lower() == 'm' and nombre.lower() >= 'n'):
        return 'Grupo A'
    else:
        return 'Grupo B'

def main():
    print("Bienvenido al programa de asignación de grupos.")
    nombre = input("Ingresa tu nombre: ")
    sexo = input("Ingresa tu sexo (M/F): ")

    grupo_asignado = determinar_grupo(nombre, sexo)

    print(f"\nTe corresponde al {grupo_asignado}.")

if __name__ == "__main__":
    main()

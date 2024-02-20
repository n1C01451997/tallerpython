def main():
    contraseña_correcta = "contraseña123"  # Contraseña correcta

    while True:
        contraseña_usuario = input("Por favor, ingrese la contraseña: ")

        if contraseña_usuario == contraseña_correcta:
            print("¡Contraseña correcta! Bienvenido.")
            break
        else:
            print("Contraseña incorrecta. Inténtelo nuevamente.")

if __name__ == "__main__":
    main()

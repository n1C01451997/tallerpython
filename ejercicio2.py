import random

def tirar_dado():
    return random.randint(1, 6)

def juego():
    print("¡Bienvenido al juego de tirar dados!")
    input("Presiona Enter para que Álvaro tire el dado...")
    alvaro = tirar_dado()
    print(f"Álvaro sacó un {alvaro}")
    
    input("Presiona Enter para que Bárbara tire el dado...")
    barbara = tirar_dado()
    print(f"Bárbara sacó un {barbara}")

    if alvaro > barbara:
        print("¡Álvaro gana!")
    elif alvaro < barbara:
        print("¡Bárbara gana!")
    else:
        print("¡Empate!")

if __name__ == "__main__":
    juego()

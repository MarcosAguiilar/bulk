import os

SALIDA = "SALIR"
LISTAR_DISPONIBLES = "Lista"
lista_compra = []
productos_disponibles = ["Pollo", "Pan", "Arroz", "Pipas", "Manzanas", "Limones", "Lechuga", "Agua", "Cerveza"]

def pregunta_a_usuario():
    return input("Introduce un producto:\n[{} para salir]\n"
                 "[{} para ver los productos disponibles]".format(SALIDA, LISTAR_DISPONIBLES))

def crear_lista_txt():
    nombre_lista = input("Que nombre desea poner a su lista de compra?")
    a = open("{}.txt".format(nombre_lista), "w")
    a.write(("\n".join(lista_compra)))
    a.close()


def main():
    input_usuario = pregunta_a_usuario()

    while input_usuario != SALIDA:
        input_usuario = input_usuario.capitalize()
        if input_usuario in productos_disponibles:
            os.system("cls")
            lista_compra.append(input_usuario)
            print("\n".join(lista_compra))
            input_usuario = pregunta_a_usuario()
        elif input_usuario == LISTAR_DISPONIBLES:
            os.system("cls")
            print("/".join(productos_disponibles))
            input_usuario = pregunta_a_usuario()
        else:
            os.system("cls")
            print("{} no esta disponible en este momento".format(input_usuario))
            input_usuario = pregunta_a_usuario()

    crear_lista_txt()




if __name__ == "__main__":
    main()
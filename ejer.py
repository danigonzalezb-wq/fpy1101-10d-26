dicc_consola={ }
dicc_ventas={  }

def menu_principal():
    print("--Menú Principal--")
    print("1.	Agregar consola")
    print("2.	Buscar consola por sigla")
    print("3.	Eliminar consola")
    print("4.	Mostrar todas las consolas")
    print("5.	Salir")

def op_menu():
    op=int("Ingrese la opcion deseada")
    while True:
        try:
            op = int(input("Ingrese su opcion deseada"))
            if op<1 or op>5: 
               print
            else:
                return op
        except ValueError:
            print("opcion no valida, ingrese una opcion entre 1 y 5")


def agregar_consola(lista_consola):
    sigla=input("Agrege la sigla de la consola: ")
    nombre=input("Ingrese el nombre de la consola: ")
    fabricante=input("Ingrese el fabricante: ")
    año_lanzamiento=int("ingrese el año de fabricacion: ")
    precio=int("ingrese el precio de la consola: ")
    stock=int("ingrese la cantidad de consolas en stock: ")

    if len(sigla.strip())>2 or len(sigla.strip())<5:
        print("h")


while True:
    menu_principal
    op=op_menu

    if op==1:
        agregar_consola(dicc_consola)
    elif op==2:
        print
    elif op==3:
        print
    elif op==4:
        print
    elif op==5:
        print
    else:
        print
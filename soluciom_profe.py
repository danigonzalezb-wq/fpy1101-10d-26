#ppal
consolas={}#{sigla:[nombre,fabricante,añolanzamiento]}
ventas={}#{sigla:[precio, stock]}

def menu():
    print("="*40)
    print("sistema de consola")
    print("1._")
    print("2._")
    print("3._")
    print("4._")
    print("5._")
    print("="*40)


def leer_op():
    while True:
        try:
            op=int(input(".."))
            return op
        except ValueError:
            print("...")

#funcion de validacion que retornan True o False
def validar_sigla_formato(sigla):
    return sigla.upper() and sigla.isalpha() and len(sigla) >=2 and len(sigla)<=5
    # return True
    #upper()= letras
    # isalpha()= mayusculas

def validar_sigla_no_existe(sigla,consola):



while True:
    menu()
    op=leer_op()

    if op==1:
       agregar_consola(consolas, ventas)
    elif op==2:
        buscar_consola(consolas, ventas)
    elif op==3:
        eliminar_consola(consolas, ventas)
    elif op==4:
        mostar_consola(consolas,ventas)
    elif op==4:
        print("saliendo...")
        break
    else:
        print("...")
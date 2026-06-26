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
    return sigla not in consola
    #""" if sigla not in consola:
    #       retrun true
    #    else:
    #       retrun false"""

def validar_nombre(nombre):
    return 3<= len(nombre.strip()) <=40
   #el .strip() quita espacios

def validar_año(añoSTR):
    if not añoSTR.isdigit():
        return False
    
    return 1972<=int(añoSTR)<=2025

def validar_precio(precioStr):
    try:
        return float(precioStr)>0
    except ValueError:
        return False

def validar_stock(stockStr):
   if not stockStr.isdigit():
       return False
   
   return int(stockStr)>=0

def validar_fabricante(fabricante):
    return 2<= len(fabricante.strip()) <=30

def agregar_consola(consolas, ventas):
    sigla=input("ingrese sigla de 2 a 5 letras").strip()
    while not validar_sigla_formato(sigla):
        print("error de sigla, debe tener 2 a5 letras mayusculas,vuelva a intentar")
        sigla=input("sigla: ").strip

    if not validar_sigla_no_existe(sigla, consolas):
        print("...")
        return
    
    nombre=input("ingrese").strip()
    while not validar_nombre(nombre):
        print("error de sigla, debe tener 2 a5 letras mayusculas,vuelva a intentar")
        nombre=input("ingrese").strip()
    
    fabricante=input("...").strip()
    while not validar_fabricante(fabricante):
        print("error")
        fabricante=input("...").strip()
    
    añoSTR=input("año de lanzamiento").strip()
    while not validar_año(añoSTR):
        print("error")
        añoSTR=input("año de lanzamiento").strip()

    precioStr=input("pecio").strip()
    while not validar_precio(precioStr):
        print("error")
        precioStr=input("pecio").strip()
    
    stockStr=input("...").strip()
    while not validar_stock(stockStr):
        print("error")
        stockStr=input("...").strip()

    
    consolas[sigla]=[nombre, fabricante,int(añoSTR)]
    ventas[sigla]=[float(precioStr, int(stockStr))]

def buscar_consola(consolas, sigla):
    return sigla in consolas

def opcion_buscar(consolas, ventas):
    sigla=input("ingresar").strip().upper()
    if buscar_consola(consolas,sigla):
        detalle_consola(sigla,consolas,ventas)
    else:
        print("no se encontro consola buscada", sigla)

def mostrar_todas(consolas,ventas):
    print("="*60)
    print("lista d econsolas")
    print("="*60)
    if len(consolas)==0:
        print("no hay datos")
    else:
        for sigla, datos in consolas.items():
            nombre,fabricante,año=datos
            precio,stock=ventas[sigla]
            print(f"sigla:{sigla}, {nombre}, {fabricante}, {año}, ${precio}, {stock}")
    print("="*62)
    print(f"total de consolas: {len(consolas)}")

def detalle_consola(sigla,consolas,ventas):
    nombre,fabricante,año=consolas[sigla]
    precio,stock=ventas[sigla]

    print("consola encontrada")
    print("sigla: ", sigla)
    print("nombre: ", nombre)


def eliminar_consola(consolas, ventas):
    print("eliinar")
    sigla=input("ingrese consola").strip.upper()

    if not buscar_consola(consolas, sigla):
        print
        return
    detalle_consola(sigla, consolas, ventas)
    confirmar=input("segura").strip().lower()
    if confirmar=="s":
        del consolas[sigla]
        del ventas[sigla]
        print("eliminado exirosamente")
    else:
        print("eliminacion cancelada")


#principal

while True:
    menu()
    op=leer_op()

    if op==1:
       agregar_consola(consolas, ventas)
    elif op==2:
        opcion_buscar(consolas, ventas)
    elif op==3:
        eliminar_consola(consolas, ventas)
    elif op==4:
        mostrar_todas(consolas,ventas)
    elif op==4:
        print("saliendo...")
        break
    else:
        print("...")
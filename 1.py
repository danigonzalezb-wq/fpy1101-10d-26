# MENÚ PRINCIPAL


def mostrar_menu():
    #Imprime las opciones del menú principal.
    print("========== SISTEMA DE GESTIÓN DE CONSOLAS ==========")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")


def leer_opcion():
    while True:
        op = input("Seleccione una opción (1-5): ").strip()
       
        if op in ["1", "2", "3", "4", "5"]:
            return op
        else:
            print("Error: Opción inválida. Debe ser un número del 1 al 5.")


# FUNCIONES 


def validar_sigla(sigla, consolas):
    #Valida entre 2 y 5 caracteres, solo mayúsculas y que no exista.
    
    if len(sigla) < 2 or len(sigla) > 5:
        return False
        
    
    if sigla.isupper() == False or sigla.isalpha() == False:
        return False
        
    if sigla in consolas:
        return False
    return True


def validar_nombre(nombre):
    #Valida entre 3 y 40 caracteres, no vacío.
    nombre_limpio = nombre.strip()
    
    if len(nombre_limpio) < 3 or len(nombre_limpio) > 40:
        return False
    return True


def validar_fabricante(fabricante):
    #Valida entre 2 y 30 caracteres, no vacío.
    fabricante_limpio = fabricante.strip()

    if len(fabricante_limpio) < 2 or len(fabricante_limpio) > 30:
        return False
    return True


def validar_anio(anio_str):
    #Valida que sea un entero entre 1972 y 2025.

    if anio_str.isdigit() == False:
        return False
    anio = int(anio_str)

    if anio < 1972 or anio > 2025:
        return False
    return True


def validar_precio(precio_str):
    #Valida que sea un número decimal/entero mayor a 0.
    try:
        precio = float(precio_str)
        return precio > 0
    except ValueError:
        return False


def validar_stock(stock_str):
    #Valida que sea un número entero mayor o igual a 0.
    if stock_str.isdigit() == False:
        return False
    stock = int(stock_str)
    return stock >= 0


# FUNCIONES DEL SISTEMA


def agregar_consola(consolas, ventas):
    #Solicita, valida y agrega
    print("--- AGREGAR NUEVA CONSOLA ---")
    
    # 1. Validar Sigla
    sigla = input("Ingrese Sigla (2-5 letras mayúsculas): ").strip()
    if validar_sigla(sigla, consolas) == False:
        print("Error: Sigla inválida o ya registrada en el sistema.")
        return

    # 2. Validar Nombre
    nombre = input("Ingrese Nombre (3-40 caracteres): ")
    if validar_nombre(nombre) == False:
        print("Error: Nombre inválido (debe tener entre 3 y 40 caracteres).")
        return

    # 3. Validar Fabricante
    fabricante = input("Ingrese Fabricante (2-30 caracteres): ")
    if validar_fabricante(fabricante) == False:
        print("Error: Fabricante inválido (debe tener entre 2 y 30 caracteres).")
        return

    # 4. Validar Año
    anio_str = input("Ingrese Año de lanzamiento (1972-2025): ").strip()
    if validar_anio(anio_str) == False:
        print("Error: Año inválido (debe ser un número entero entre 1972 y 2025).")
        return
    anio = int(anio_str)

    # 5. Validar Precio
    precio_str = input("Ingrese Precio (Mayor a 0): ").strip()
    if validar_precio(precio_str) == False:
        print("Error: Precio inválido (debe ser un valor numérico mayor a 0).")
        return
    precio = float(precio_str)

    # 6. Validar Stock
    stock_str = input("Ingrese Stock (Mayor o igual a 0): ").strip()
    if validar_stock(stock_str) == False:
        print("Error: Stock inválido (debe ser un número entero mayor o igual a 0).")
        return
    stock = int(stock_str)

    # Guardado sincronizado en ambos diccionarios
    consolas[sigla] = [nombre, fabricante, anio]
    ventas[sigla] = [precio, stock]
    print(f"¡Consola [{sigla}] agregada exitosamente!")


def buscar_consola(sigla, consolas):
    #Busca la sigla en el diccionario y retorna True o False.
    return sigla in consolas


def consultar_consola(consolas, ventas):
    #Muestra los datos combinados de consola
    print("--- BUSCAR CONSOLA ---")
    sigla = input("Ingrese la sigla de la consola a buscar: ").strip().upper()
    
    if buscar_consola(sigla, consolas):
        datos_c = consolas[sigla]
        datos_v = ventas[sigla]
         
        print("--- Consola Encontrada ---")
        print(f"Sigla: {sigla}")
        print(f"Nombre: {datos_c[0]}")
        print(f"Fabricante: {datos_c[1]}")
        print(f"Año lanzamiento: {datos_c[2]}")
        print(f"Precio: ${datos_v[0]}")
        print(f"Stock: {datos_v[1]} unidades")
    else:
        print("Error: La consola no se encuentra registrada.")


def eliminar_consola(consolas, ventas):
    #Elimina los datos de ambos diccionarios
    print("--- ELIMINAR CONSOLA ---")
    sigla = input("Ingrese la sigla de la consola a eliminar: ").strip().upper()
    
    if buscar_consola(sigla, consolas):
        del consolas[sigla]  #del == eliminar del diccionario
        del ventas[sigla]
        print(f"¡La consola [{sigla}] fue eliminada exitosamente de ambos registros!")
    else:
        print("Error: No se puede eliminar. La sigla no existe.")


def mostrar_todas(consolas, ventas):
    #Muestra el listado completo  ambos diccionarios.
    
    if len(consolas) == 0:
        print("El sistema está vacío. No hay consolas registradas.")
        return

    print("LISTADO COMPLETO DE CONSOLAS")
    
    
    for sigla in consolas.keys():
        nombre, fabricante, anio = consolas[sigla]
        precio, stock = ventas[sigla]
        print(f"Sigla: {sigla} | {nombre} | {fabricante} | {anio} | ${precio} | Stock: {stock}")

    print(f"Total de consolas: {len(consolas)}")


def main():

    dicc_consolas = {}
    dicc_ventas = {}
    
    while True:
        mostrar_menu()
        op = leer_opcion()
        
        if op == "1":
            agregar_consola(dicc_consolas, dicc_ventas)
        elif op == "2":
            consultar_consola(dicc_consolas, dicc_ventas)
        elif op == "3":
            eliminar_consola(dicc_consolas, dicc_ventas)
        elif op == "4":
            mostrar_todas(dicc_consolas, dicc_ventas)
        elif op == "5":
            print("\nGracias por utilizar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

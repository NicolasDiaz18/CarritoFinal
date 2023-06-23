from carritoFunciones import CarritoCompras
carrito = CarritoCompras()

def mostrarMenu():
    print("----- Menú -----")
    print("1. Mostrar productos en detalle")
    print("2. Mostrar información breve del producto")
    print("3. Buscar producto por código")
    print("4. Realizar compra")
    print("5. Modificar carrito")
    print("6. Finalizar compra")
    print("7. Salir")

def validarOpcion(opcion):
    try:
        opcion = int(opcion)
        if opcion >= 1 and opcion <= 7:
            return True
        else:
            return False
    except ValueError:
        return False

while True:
    mostrarMenu()
    opcion = input("Seleccione una opción: ")
    if validarOpcion(opcion):
        if opcion == "1":
            carrito.mostrarProductosDetalle()
        elif opcion == "2":
            carrito.mostrarProductosInfoBreve()
        elif opcion == "3":
            codigo = input("Ingrese el código del producto: ")
            carrito.buscarProducto(codigo)
        elif opcion == "4":
            carrito.realizarCompra()
        elif opcion == "5":
            carrito.modificarCarrito()
        elif opcion == "6":
            carrito.finalizarCompra()
        elif opcion == "7":
            break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
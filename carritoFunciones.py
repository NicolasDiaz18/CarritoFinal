class Producto:
    def __init__(self, codigo, nombre, marca, precio, stock, color, caracteristicas):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.color = color
        self.caracteristicas = caracteristicas

    def mostrarDetalle(self):
        print("Código: ", self.codigo)
        print("Nombre: ", self.nombre)
        print("Marca: ", self.marca)
        print("Precio: ", self.precio)
        print("Stock: ", self.stock)
        print("Color: ", self.color)
        print("Características: ", self.caracteristicas)
        print("\n---------------------------\n")

    def mostrarInfoBreve(self):
        print("Código: ", self.codigo)
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)
        print("Cantidad disponible: ", self.stock)
        print("\n---------------------------\n")


class CarritoCompras:
    def __init__(self):
        self.productosDisponibles = {
            "001": Producto("001", "Camiseta", "Adidas", 25.99, 10, "Rojo", "Algodón"),
            "002": Producto("002", "Pantalón", "Adidas", 39.99, 5, "Azul", "Poliéster"),
            "003": Producto("003", "Zapatos", "Adidas", 59.99, 3, "Negro", "Cuero"),
            # Agregar más productos acá
        }
        self.carrito = {}

    def mostrarProductosDetalle(self):
        print("----- Productos en detalle -----\n")
        for codigo, producto in self.productosDisponibles.items():
            producto.mostrarDetalle()

    def mostrarProductosInfoBreve(self):
        print("----- Información breve de los productos -----\n")
        for codigo, producto in self.productosDisponibles.items():
            producto.mostrarInfoBreve()

    def buscarProducto(self, codigo):
        if codigo in self.productosDisponibles:
            producto = self.productosDisponibles[codigo]
            producto.mostrarDetalle()
        else:
            print("El producto no existe en la tienda.\n")

    def realizarCompra(self):
        print("----- Agregar producto al carrito -----\n")
        codigo = input("Ingrese el código del producto que desea comprar: ")
        if codigo in self.productosDisponibles:
            producto = self.productosDisponibles[codigo]
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            if cantidad <= producto.stock:
                if codigo in self.carrito:
                    productoEnCarrito = self.carrito[codigo]
                    productoEnCarrito["cantidad"] += cantidad
                    productoEnCarrito["costoTotal"] = round(producto.precio * productoEnCarrito["cantidad"], 2)
                else:
                    precioTotal = round(producto.precio * cantidad, 2)
                    self.carrito[producto.codigo] = {
                        "nombre": producto.nombre,
                        "cantidad": cantidad,
                        "precioUnitario": producto.precio,
                        "costoTotal": precioTotal
                    }
                producto.stock -= cantidad
                print("\nProducto agregado al carrito.\n")
            else:
                print("\nNo hay suficiente stock disponible.\n")
        else:
            print("\nEl producto no existe en la tienda.\n")

    def modificarCarrito(self):
        print("----- Modificar carrito -----")
        if len(self.carrito) == 0:
            print("\nEl carrito está vacío.\n")
            return

        print("Productos en el carrito:\n")
        for codigo, producto in self.carrito.items():
            print("Código: ", codigo)
            print("Nombre: ", producto["nombre"])
            print("Cantidad: ", producto["cantidad"])
            print("Precio unitario: ", producto["precioUnitario"])
            print("Costo total: ", producto["costoTotal"])
            print("\n---------------------------\n")

        modificar = input("Desea modificar la cantidad de algún producto en el carrito? (SI/NO): ")
        if modificar.upper() == "SI":
            codigo = input("\nIngrese el código del producto que desea modificar: ")
            if codigo in self.carrito:
                producto = self.carrito[codigo]
                nuevaCantidad = int(input("\nIngrese la nueva cantidad: "))
                if nuevaCantidad <= self.productosDisponibles[codigo].stock + producto["cantidad"]:
                    self.productosDisponibles[codigo].stock += producto["cantidad"] - nuevaCantidad
                    producto["cantidad"] = nuevaCantidad
                    producto["costoTotal"] = round(producto["precioUnitario"] * nuevaCantidad, 2)
                    print("\nCantidad modificada exitosamente.\n")
                else:
                    print("No hay suficiente stock disponible.\n")
            eliminar = input("Desea eliminar el producto del carrito? (SI/NO): ")
            if eliminar.upper() == "SI":
                del self.carrito[codigo]
                print("\nProducto eliminado del carrito.\n")
        else:
            print("\nEl producto no se encuentra en el carrito.\n")

    def finalizarCompra(self):
        if len(self.carrito) == 0:
            print("\nEl carrito está vacío.\n")
            return

        total = 0
        print("----- Detalle de los productos comprados -----\n")
        for codigo, producto in self.carrito.items():
            print("Nombre: ", producto["nombre"])
            print("Cantidad: ", producto["cantidad"])
            print("Precio unitario: ", producto["precioUnitario"])
            print("Costo total: ", producto["costoTotal"])
            total += producto["costoTotal"]
            print()

        print("Total a pagar: ", total)

        confirmar = input("Desea confirmar la compra? (SI/NO): ")
        if confirmar.upper() == "SI":
            """for codigo, producto in self.carrito.items():
                self.productosDisponibles[codigo].stock -= producto["cantidad"]
            self.carrito = {}"""
            print("\nCompra realizada exitosamente.\n")
        elif confirmar.upper() == "NO":
            print("\nCompra cancelada\n")
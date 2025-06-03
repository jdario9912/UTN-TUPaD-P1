class Productos:
    productos = {}

    def consultar_stock(self, nombre=""):
        print(f"Nombre producto: {nombre}\nStock: {self.productos[nombre]}\n")

    def agregar_unidades(self, nombre, cantidad):
        self.productos[nombre] += cantidad

    def nuevo_producto(self, nombre):
        self.productos[nombre] = 0


opcion = -1
producto1 = Productos()

while not opcion == 0:
    opcion = int(
        input(
            (
                "Opciones: \n1. Agregar un nuevo producto\n2. Agregar unidades a un producto\n3. Consultar stock\n0. Salir\n\nIngresa una opcion: "
            )
        )
    )

    if opcion == 1:
        nombre = input(f"Vas a ingresar un nuevo producto\nNombre: ")
        producto1.nuevo_producto(nombre)
        print("\n\n")
    elif opcion == 2:
        nombre = input(f"Vas a agregar stock a un prodcuto\nNombre: ")
        stock = int(input("Stock: "))
        producto1.agregar_unidades(nombre, stock)
        print("\n\n")
    elif opcion == 3:
        nombre = input("Nombre: ")
        producto1.consultar_stock(nombre)
        print("\n\n")

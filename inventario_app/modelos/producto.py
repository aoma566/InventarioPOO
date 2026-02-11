class Producto:
    """
    Representa un producto dentro del inventario.
    """

    def __init__(self, producto_id: int, nombre: str, cantidad: int, precio: float):
        # Atributos privados (encapsulación)
        self.__producto_id = producto_id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__producto_id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return (
            f"ID: {self.__producto_id} | "
            f"Nombre: {self.__nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio: ${self.__precio:.2f}"
        )

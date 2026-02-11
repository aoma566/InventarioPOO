from modelos.producto import Producto


class Inventario:
    """
    Gestiona el conjunto de productos del sistema.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        # Validar ID único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, producto_id: int):
        for p in self.productos:
            if p.get_id() == producto_id:
                self.productos.remove(p)
                print("🗑️ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, producto_id: int, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == producto_id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("✏️ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_producto(self, nombre: str):
        resultados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("🔍 No se encontraron productos.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 Inventario vacío.")
            return
        print("\n📋 Inventario:")
        for p in self.productos:
            print(p)

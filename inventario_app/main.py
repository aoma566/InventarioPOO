from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("0. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto_id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            producto_id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(producto_id)

        elif opcion == "3":
            producto_id = int(input("ID del producto: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(producto_id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "0":
            print("👋 Saliendo del sistema.")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()

from typing import TYPE_CHECKING, List
from product import Producto
from colores import Colores

if TYPE_CHECKING:
    from main import GestorTienda

class Tienda:
    def __init__(self, nombre: str = "Tienda sin nombre", direccion: str = "Calle sin nombre", productos: list[Producto] = []) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.productos = productos

    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Tienda]{Colores.ENDC} {Colores.LIGHTRED}Nombre{Colores.ENDC}: {self.nombre}, {Colores.LIGHTRED}Direccion{Colores.ENDC}: {self.direccion}, {Colores.LIGHTRED}Productos{Colores.ENDC}: {', '.join(f'{product.nombre}'for product in self.productos)}"

    def modificar(self, gestor_tienda: "GestorTienda") -> None:

        # nombre
        print(f"{Colores.YELLOW}[Tienda]{Colores.ENDC}\nNombre actual: {self.nombre}\nNuevo nombre(en blanco para no cambiar):")
        nombre = input()
        if nombre:
            self.nombre = nombre
        print(f"{Colores.OKGREEN}Nuevo nombre: {self.nombre}{Colores.ENDC}")

        # direccion
        print(f"\nDireccion: {self.direccion}\nNueva direccion(en blanco para no cambiar):")
        direccion = input()
        if direccion:
            self.direccion = direccion
        print(f"{Colores.OKGREEN}Nueva direcion: {self.direccion}{Colores.ENDC}")
        
        # productos 
        print(f"\nProductos actuales: {', '.join(p.nombre for p in self.productos)}")
        print("¿Quieres modificar los productos de la tienda? (s/n):")
        if input().lower() == 's':
            while True:
                print(f"1. Agregar producto\n2. Eliminar producto\n3. Terminar modificacion{Colores.ENDC}")
                try:
                    op = int(input())
                    match op :
                        case 1:
                            print(f"{Colores.YELLOW}Productos{Colores.ENDC} disponibles:")
                            for i in range(len(gestor_tienda.productos)):
                                print(f"{Colores.LIGHTGREEN}{i + 1}{Colores.ENDC} - {gestor_tienda.productos[i]}")
                            print("Indice del producto a agregar:")
                            indice = int(input()) - 1
                            if not self.productos.count(gestor_tienda.productos[indice]):
                                self.productos.append(gestor_tienda.productos[indice])
                            else:
                                print(f"{Colores.FAIL}Ese producto ya esta en la tienda.{Colores.ENDC}")
                        case 2:
                            if not self.productos:
                                print(f"{Colores.FAIL}No hay productos para eliminar.{Colores.ENDC}")
                                continue

                            print("Productos actuales:")
                            for i, producto in enumerate(self.productos, 1):
                                print(f"- {Colores.OKGREEN}{i}{Colores.ENDC} - {producto.nombre}")

                            print("Numero del producto a eliminar:")
                            try:
                                indice = int(input()) - 1
                                if 0 <= indice < len(self.productos):
                                    producto_eliminado = self.productos.pop(indice)
                                    print(f"Producto eliminado: {producto_eliminado.nombre}")
                                else:
                                    print(f"{Colores.FAIL}Indice invalido.{Colores.ENDC}")
                            except ValueError:
                                print(f"{Colores.FAIL}Debes introducir un numero entero valido.{Colores.ENDC}")
                        case 3:
                            break
                        case _:
                            print(f"{Colores.FAIL}Opcion invalida.{Colores.ENDC}")
                except ValueError:
                    print(f"{Colores.FAIL}Debe introducir un numero entero valido.{Colores.ENDC}")
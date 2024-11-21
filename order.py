from datetime import date
from typing import List, TYPE_CHECKING
from colores import Colores
from client import Cliente

if TYPE_CHECKING:
    from product import Producto
    from main import GestorTienda

    
class Pedido:
    def __init__(self, cliente: Cliente = Cliente(), productos: list["Producto"] = [], fecha: date = None, estado: str = "pendiente") -> None:
        self.cliente = cliente
        self.productos = productos
        self.fecha = fecha if fecha else date.today()
        self.estado = estado
        
        if cliente is not None:
            cliente.pedidos.append(self)

    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Pedido]{Colores.ENDC} {Colores.LIGHTRED}Cliente{Colores.ENDC}: {self.cliente.nombre}, {Colores.LIGHTRED}Productos{Colores.ENDC}: {', '.join(f'{product.nombre}' for product in self.productos)}, {Colores.LIGHTRED}Fecha{Colores.ENDC}: {self.fecha}, {Colores.LIGHTRED}Estado{Colores.ENDC}: {self.estado}"
        
    def modificar(self, gestor_tienda: "GestorTienda") -> None:

        # peido
        print(f"[Pedido]\nEstado actual: {self.estado}")
        print("Nuevo estado (pendiente/enviado/entregado):")
        while True:
            nuevo_estado = input().lower()
            if nuevo_estado in ['pendiente', 'enviado', 'entregado']:
                self.estado = nuevo_estado
                break
            else:
                print(f"{Colores.FAIL}{Colores.UNDERLINE}Estado no valido. Usa: pendiente, enviado, o entregado.{Colores.ENDC}")
        print(f"{Colores.OKGREEN}Nuevo estado: {self.estado}{Colores.ENDC}")
        
        # fecha
        print(f"\nFecha actual: {self.fecha.strftime('%Y-%m-%d')}\nNueva fecha (YYYY-MM-DD):")
        while True:
            nueva_fecha = input()
            if nueva_fecha:
                try:
                    self.fecha = date.fromisoformat(nueva_fecha)
                    break
                except ValueError:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}Formato de fecha invalido. Usa YYYY-MM-DD.{Colores.ENDC}")
            else:
                break
        print(f"{Colores.OKGREEN}Nueva fecha: {self.fecha}{Colores.ENDC}")
        
        # productos
        print(f"\nProductos actuales: {', '.join(p.nombre for p in self.productos)}")
        print("¿Quieres modificar los productos del pedido? (s/n):")
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
                                print(f"{Colores.FAIL}Ese producto ya esta en el pedido.{Colores.ENDC}")
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
        
        # cliente
        print(f"\nQue cliente tiene asociado este pedido(introduce el indice)?")
        for i in range(len(gestor_tienda.clientes)):
            print(f"- {Colores.OKGREEN}{i + 1}{Colores.ENDC} - {gestor_tienda.clientes[i].nombre}")

        while True:
            try:
                indice_cliente = int(input()) - 1
                if 0 <= indice_cliente < len(gestor_tienda.clientes):
                    self.cliente = gestor_tienda.clientes[indice_cliente]
                    gestor_tienda.clientes[indice_cliente].pedidos.append(self)
                    break
                else:
                    print(f"{Colores.FAIL}Indice invalido.{Colores.ENDC}")
            except ValueError:
                print(f"{Colores.FAIL}Debes introducir un numero entero valido.{Colores.ENDC}")

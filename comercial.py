from typing import TYPE_CHECKING, List
from client import Cliente
from order import Pedido
from colores import Colores

if TYPE_CHECKING:
    from main import GestorTienda

class Comercial:
    def __init__(self, nombre: str = "Comercial sin nombre", clientes_asignados: List[Cliente] = None, lista_pedidos: List[Pedido] = None) -> None:
        self.nombre = nombre
        self.clientes_asignados = clientes_asignados if clientes_asignados else []
        self.lista_pedidos = lista_pedidos if lista_pedidos else []
        
    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Comercial]{Colores.ENDC} {Colores.LIGHTRED}Nombre{Colores.ENDC}: {self.nombre}, {Colores.LIGHTRED}Clientes asignados{Colores.ENDC}: {', '.join(f'{cliente.nombre}'for cliente in self.clientes_asignados)}, {Colores.LIGHTRED}Lista pedidos{Colores.ENDC}: {', '.join(f'[{pedido.cliente.nombre}, {pedido.fecha}, {pedido.estado}]'for pedido in self.lista_pedidos)}"
        
    def modificar(self, gestor_tienda: "GestorTienda") -> None:

        # nombre
        print(f"{Colores.YELLOW}[Comercial]{Colores.ENDC}\nNombre actual: {self.nombre}\nNuevo nombre(en blanco para no cambiar):")
        nombre = input()
        if nombre:
            self.nombre = nombre
        print(f"{Colores.OKGREEN}Nuevo nombre: {self.nombre}{Colores.ENDC}")

        # clientes 
        print(f"\nClientes asignados: {', '.join(p.nombre for p in self.clientes_asignados)}")
        print("¿Quieres modificar los clientes asignados? (s/n):")
        if input().lower() == 's':
            while True:
                print(f"1. Agregar cliente\n2. Eliminar cliente\n3. Terminar modificacion{Colores.ENDC}")
                try:
                    op = int(input())
                    match op :
                        case 1:
                            print(f"{Colores.YELLOW}Clientes{Colores.ENDC} disponibles:")
                            for i in range(len(gestor_tienda.clientes)):
                                print(f"{Colores.LIGHTGREEN}{i + 1}{Colores.ENDC} - {gestor_tienda.clientes[i]}")
                            print("Indice del cliente a agregar:")
                            indice = int(input()) - 1
                            if not self.clientes_asignados.count(gestor_tienda.clientes[indice]):
                                self.clientes_asignados.append(gestor_tienda.clientes[indice])
                            else:
                                print(f"{Colores.FAIL}Ese cliente esta añadido.{Colores.ENDC}")
                        case 2:
                            if not self.clientes_asignados:
                                print(f"{Colores.FAIL}No hay clientes para eliminar.{Colores.ENDC}")
                                continue

                            print("Clientes actuales:")
                            for i, cliente in enumerate(self.clientes_asignados, 1):
                                print(f"- {Colores.OKGREEN}{i}{Colores.ENDC} - {cliente.nombre}")

                            print("Numero del cliente a eliminar:")
                            try:
                                indice = int(input()) - 1
                                if 0 <= indice < len(self.clientes_asignados):
                                    cliente_eliminado = self.clientes_asignados.pop(indice)
                                    print(f"Cliente eliminado: {cliente_eliminado.nombre}")
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

        # pedidos 
        # TODO: solo se deben poder añadir clientes que esten contendiso en clientes lista (entiendo yo), arreglar.
        print(f"\nPedidos asignados: {', '.join(p.fecha.strftime('%Y/%m/%d') for p in self.lista_pedidos)}")
        print("¿Quieres modificar los pedidos asignados? (s/n):")
        if input().lower() == 's':
            while True:
                print(f"1. Agregar pedido\n2. Eliminar pedido\n3. Terminar modificacion{Colores.ENDC}")
                try:
                    op = int(input())
                    match op :
                        case 1:
                            # TODO: hacer algo para que solo aparezcan clientes en clientes lista. 

                            print(f"{Colores.YELLOW}Pedidos{Colores.ENDC} disponibles:")

                            pedidos_cliente = []

                            for i in range(len(gestor_tienda.pedidos)):
                                for cliente in self.clientes_asignados:
                                    if gestor_tienda.pedidos[i].cliente.nombre == cliente.nombre:
                                        pedidos_cliente.append(gestor_tienda.pedidos[i])

                            for i in range(len(pedidos_cliente)):
                                print(f"{Colores.LIGHTGREEN}{i + 1}{Colores.ENDC} - {pedidos_cliente[i]}")
                            
                            while True:
                                print("Indice del pedido a agregar:")
                                indice = int(input()) - 1
                                
                                if indice < 0 or indice >= len(pedidos_cliente):
                                    print(f"{Colores.FAIL}Ese pedido no existe.{Colores.ENDC}")
                                    continue
                                
                                if not self.lista_pedidos.count(pedidos_cliente[indice]):
                                    self.lista_pedidos.append(pedidos_cliente[indice])
                                    break
                                else:
                                    print(f"{Colores.FAIL}Ese pedido ya esta añadido.{Colores.ENDC}")
                        case 2:
                            if not self.lista_pedidos:
                                print(f"{Colores.FAIL}No hay pedidos para eliminar.{Colores.ENDC}")
                                continue

                            print("Pedidos actuales:")
                            for i, pedido in enumerate(self.lista_pedidos, 1):
                                print(f"- {Colores.OKGREEN}{i}{Colores.ENDC} - {pedido.cliente}, {pedido.fecha}, {pedido.estado}")

                            print("Numero del pedido a eliminar:")
                            try:
                                indice = int(input()) - 1
                                if 0 <= indice < len(self.lista_pedidos):
                                    pedido_eliminado = self.lista_pedidos.pop(indice)
                                    print(f"Pedido eliminado: {pedido_eliminado.nombre}")
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
from typing import List, TYPE_CHECKING
from colores import Colores

if TYPE_CHECKING:
    from order import Pedido
    from main import GestorTienda

class Cliente:
    def __init__(self, nombre: str = "Sin nombre", email: str = "sin@email.com", telefono: str = "000000000", pedidos: List["Pedido"] = None) -> None:
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.pedidos: List["Pedido"] = pedidos if pedidos else []
        
    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Cliente]{Colores.ENDC} {Colores.LIGHTRED}Nombre{Colores.ENDC}: {self.nombre}, {Colores.LIGHTRED}Email{Colores.ENDC}: {self.email}, {Colores.LIGHTRED}Telefono{Colores.ENDC}: {self.telefono}, {Colores.LIGHTRED}Pedidos{Colores.ENDC}: {', '.join(f'[{pedido.fecha}, {pedido.estado}]'for pedido in self.pedidos)}"
      
    def modificar(self, gestor_tienda: "GestorTienda") -> None:

        # nombre
        print(f"{Colores.YELLOW}[Cliente]{Colores.ENDC}\nNombre: {self.nombre}\nNuevo nombre(en blanco para no cambiar):")
        nombre = input()
        if nombre:
            self.nombre = nombre
        print(f"{Colores.OKGREEN}Nuevo nombre: {self.nombre}{Colores.ENDC}")
        
        # email
        print(f"\nEmail: {self.email}\nNuevo email(en blanco para no cambiar):")
        email = input()
        if email:
            while '@' not in email: 
                print(f"{Colores.FAIL}{Colores.UNDERLINE}Email no valido. Debe contener '@'.{Colores.ENDC}")
                email = input()
            self.email = email
        print(f"{Colores.OKGREEN}Nuevo email: {self.email}{Colores.ENDC}")
        
        # tlefono
        print(f"\nTelefono: {self.telefono}\nNuevo telefono(en blanco para no cambiar):")
        telefono = input()
        if telefono:
            while not telefono.replace('+', '').replace(' ', '').isdigit(): 
                print(f"{Colores.FAIL}{Colores.UNDERLINE}Telefono no valido. Debe contener solo numeros (se permite + y espacios).{Colores.ENDC}")
                telefono = input()
            self.telefono = telefono
        print(f"{Colores.OKGREEN}Nuevo telefono: {self.telefono}{Colores.ENDC}")
        
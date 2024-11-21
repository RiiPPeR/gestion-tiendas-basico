from typing import TYPE_CHECKING
from colores import Colores

if TYPE_CHECKING:
    from main import GestorTienda

class Producto:
    def __init__(self, nombre: str = "Sin nombre", precio: float = 0, stock: int = 0) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Producto]{Colores.ENDC} {Colores.LIGHTRED}Nombre{Colores.ENDC}: {self.nombre}, {Colores.LIGHTRED}Precio{Colores.ENDC}: {self.precio}, {Colores.LIGHTRED}Stock{Colores.ENDC}: {self.stock}"
            
    def modificar(self, gestor_tienda: "GestorTienda") -> None:
        
        # nombre
        print(f"{Colores.YELLOW}[Producto]{Colores.ENDC}\nNombre: {self.nombre}\nNuevo nombre(en blanco para no cambiar):")
        nombre = input()
        if nombre:    
            self.nombre = nombre
        print(f"{Colores.OKGREEN}Nuevo nombre: {self.nombre}{Colores.ENDC}")
        
        # precio
        print(f"\nPrecio: {self.precio}\nNuevo precio(en blanco para no cambiar):")
        while True:
            numero = input()
            if numero:
                try:
                    numero = float(numero)
                    self.precio = numero
                    break
                except ValueError:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}No es un valor valido. Introduce un numero decimal.{Colores.ENDC}")
            else:
                break
        print(f"{Colores.OKGREEN}Nuevo precio: {self.precio}{Colores.ENDC}")
        
        # stock
        print(f"\nStock: {self.stock}\nNuevo stock:")
        while True:
            numero = input()
            if numero:
                try:
                    numero = int(numero)
                    self.stock = numero
                    break
                except ValueError:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}No es un valor valido. Introduce un numero entero.{Colores.ENDC}")              
            else:
                break
        print(f"{Colores.OKGREEN}Nuevo stock: {self.stock}{Colores.ENDC}")
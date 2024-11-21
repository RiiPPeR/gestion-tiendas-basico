from datetime import date
from typing import TYPE_CHECKING
from order import Pedido
from colores import Colores

if TYPE_CHECKING:
    from main import GestorTienda

class Incidente:
    def __init__(self, pedido: Pedido = None, descripcion: str = "Sin descripcion", fecha: date = date.today(), estado: str = "pendiente") -> None:
        self.pedido = pedido
        self.descripcion = descripcion
        self.fecha = fecha  
        self.estado = estado
        
    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Incidencia]{Colores.ENDC} {Colores.LIGHTRED}Pedido{Colores.ENDC}: {Colores.MAGENTA}[{Colores.ENDC}{self.pedido}{Colores.MAGENTA}]{Colores.ENDC} {Colores.LIGHTRED}Descripcion{Colores.ENDC}: {self.descripcion}, {Colores.LIGHTRED}Fecha{Colores.ENDC}: {self.fecha}, {Colores.LIGHTRED}Estado{Colores.ENDC}: {self.estado}"

    def modificar(self, gestor_tienda: "GestorTienda"):
        pass

        # pedido
        print(f"{Colores.YELLOW}[Incidencia]{Colores.ENDC}\nQue pedido tiene asociado esta incidencia(introduce el indice)?")
        for i in range(len(gestor_tienda.pedidos)):
            print(f"- {Colores.OKGREEN}{i + 1}{Colores.ENDC} - {gestor_tienda.pedidos[i]}")

        while True:
            try:
                indice_producto = int(input()) - 1
                if 0 <= indice_producto < len(gestor_tienda.pedidos):
                    self.pedido = gestor_tienda.pedidos[indice_producto]
                    break
                else:
                    print(f"{Colores.FAIL}Indice invalido.{Colores.ENDC}")
            except ValueError:
                print(f"{Colores.FAIL}Debes introducir un numero entero valido.{Colores.ENDC}")
        
        print(f"{Colores.OKGREEN}Pedido asignado: {self.pedido}{Colores.ENDC}")

        # descripcion
        print(f"\nDescripcion: {self.descripcion}\nNueva descripcion(en blanco para no cambiar):")
        descripcion = input()
        if descripcion:
            self.descripcion = descripcion
        print(f"{Colores.OKGREEN}Nuevo descripcion: {self.descripcion}{Colores.ENDC}")

        # fecha 
        print(f"\nFecha : {self.fecha}\nNueva fecha(enter para no cambiar):")

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

        # estado
        print(f"\nEstado actual: {self.estado}")

        print("Nuevo estado (pendiente/en proceso/resuelta):")
        while True:
            nuevo_estado = input().lower()
            if nuevo_estado in ['pendiente', 'en proceso', 'resuelta']:
                self.estado = nuevo_estado
                break
            else:
                print(f"{Colores.FAIL}{Colores.UNDERLINE}Estado no valido. Usa: pendiente, enviado, o entregado.{Colores.ENDC}")

        print(f"{Colores.OKGREEN}Nuevo estado: {self.estado}{Colores.ENDC}")
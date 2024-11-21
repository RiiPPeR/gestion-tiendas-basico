from datetime import date
from typing import TYPE_CHECKING
from product import Producto
from colores import Colores

if TYPE_CHECKING:
    from main import GestorTienda

class Oferta:
    def __init__(self, producto: Producto = None, descuento: int = 0, fecha_inicio: date = None, fecha_fin: date = None) -> None:
        self.producto = producto
        self.descuento = descuento
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self) -> str:
        return f"{Colores.YELLOW}[Oferta]{Colores.ENDC} {Colores.LIGHTRED}Productos{Colores.ENDC}: {self.producto.nombre}, {Colores.LIGHTRED}Descuento{Colores.ENDC}: {self.descuento}, {Colores.LIGHTRED}Fecha inicio{Colores.ENDC}: {self.fecha_inicio}, {Colores.LIGHTRED}Fecha fin{Colores.ENDC}: {self.fecha_fin}"

    def es_valida(self, fecha: date): 
        return fecha >= self.fecha_inicio and fecha <= self.fecha_fin
    
    def modificar(self, gestor_tienda: "GestorTienda"):
        
        # producto
        print(f"{Colores.YELLOW}[Oferta]{Colores.ENDC}\nQue producto tiene asociado esta oferta(introduce el indice)?")
        for i in range(len(gestor_tienda.productos)):
            print(f"- {Colores.OKGREEN}{i + 1}{Colores.ENDC} - {gestor_tienda.productos[i].nombre}")

        while True:
            try:
                indice_producto = int(input()) - 1
                if 0 <= indice_producto < len(gestor_tienda.productos):
                    self.producto = gestor_tienda.productos[indice_producto]
                    break
                else:
                    print(f"{Colores.FAIL}Indice invalido.{Colores.ENDC}")
            except ValueError:
                print(f"{Colores.FAIL}Debes introducir un numero entero valido.{Colores.ENDC}")
        
        print(f"{Colores.OKGREEN}Producto asignado: {self.producto}{Colores.ENDC}")

        # descuento
        print(f"\nDescuento: {self.descuento}\nNuevo descuento(enter para no cambiar):")

        while True:
            numero = input()
            if numero:
                try:
                    numero = int(numero)
                    self.descuento = numero
                    break
                except ValueError:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}No es un valor valido. Introduce un numero entero.{Colores.ENDC}")              
            else:
                break

        print(f"{Colores.OKGREEN}Nuevo descuento: {self.descuento}{Colores.ENDC}")

        # fecha inicio
        print(f"\nFecha inicio: {self.fecha_inicio}\nNueva fecha inicio(enter para no cambiar):")

        while True:
            nueva_fecha = input()
            if nueva_fecha:
                try:
                    self.fecha_inicio = date.fromisoformat(nueva_fecha)
                    break
                except ValueError:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}Formato de fecha invalido. Usa YYYY-MM-DD.{Colores.ENDC}")
            else:
                break

        print(f"{Colores.OKGREEN}Nueva fecha inicial: {self.fecha_inicio}{Colores.ENDC}")

        # fecha fin
        print(f"\nFecha fin: {self.fecha_fin}\nNueva fecha fin(enter para no cambiar):")

        while True:
            nueva_fecha = input()
            if nueva_fecha:
                try:
                    self.fecha_fin = date.fromisoformat(nueva_fecha)
                    break
                except ValueError:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}Formato de fecha invalido. Usa YYYY-MM-DD.{Colores.ENDC}")
            else:
                break
        
        print(f"{Colores.OKGREEN}Nueva fecha final: {self.fecha_fin}{Colores.ENDC}")
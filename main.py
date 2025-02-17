from typing import List
import datetime
import os

from product import Producto
from client import Cliente
from order import Pedido
from shop import Tienda
from comercial import Comercial
from offer import Oferta
from incident import Incidente
from colores import Colores

class GestorTienda:
    def __init__(self):
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []
        self.pedidos: List[Pedido] = []
        self.tiendas: List[Tienda] = []
        self.comerciales: List[Comercial] = []
        self.ofertas: List[Oferta] = []
        self.incidencias: List[Incidente] = []
        self.load_data()

    def load_data(self) -> None:
        productos_data = [
            {"nombre": "Smart TV 4K", "precio": 599.0, "stock": 100},
            {"nombre": "PlayStation 5", "precio": 499.0, "stock": 200},
            {"nombre": "Laptop Gamer", "precio": 1299.0, "stock": 150},
            {"nombre": "PC de Escritorio", "precio": 899.0, "stock": 75},
            {"nombre": "Tablet Android", "precio": 399.0, "stock": 50},
            {"nombre": "Auriculares Bluetooth", "precio": 99.0, "stock": 120},
            {"nombre": "Smartwatch", "precio": 249.0, "stock": 90},
            {"nombre": "Altavoz Inteligente", "precio": 99.0, "stock": 110},
            {"nombre": "Consola Retro", "precio": 129.0, "stock": 85},
            {"nombre": "Batería Externa", "precio": 39.0, "stock": 300},
            {"nombre": "Monitor Curvo", "precio": 349.0, "stock": 100},
            {"nombre": "Drone con Cámara", "precio": 499.0, "stock": 40},
            {"nombre": "VR Headset", "precio": 599.0, "stock": 25},
            {"nombre": "Ratón Gaming", "precio": 59.0, "stock": 140},
            {"nombre": "Teclado Mecánico", "precio": 99.0, "stock": 160},
            {"nombre": "Smart Home Hub", "precio": 149.0, "stock": 100},
            {"nombre": "Cámara de Seguridad", "precio": 199.0, "stock": 60},
            {"nombre": "Consola Portátil", "precio": 299.0, "stock": 70},
            {"nombre": "Impresora 3D", "precio": 399.0, "stock": 45},
            {"nombre": "Kindle", "precio": 129.0, "stock": 95}
        ]

        for producto in productos_data:
            self.productos.append(Producto(producto.get("nombre"), producto.get("precio"), producto.get("stock")))

        clientes_data = [
            {"nombre": "Jose Miguel", "email": "cliente1@example.com", "telefono": "123456789"},
            {"nombre": "Vicenta", "email": "cliente2@example.com", "telefono": "987654321"},
            {"nombre": "Roberto", "email": "cliente3@example.com", "telefono": "456123789"},
            {"nombre": "Concha", "email": "cliente4@example.com", "telefono": "789456123"},
            {"nombre": "Juan Cuesta", "email": "cliente5@example.com", "telefono": "321789654"}
        ]

        for cliente in clientes_data:
            self.clientes.append(Cliente(cliente.get("nombre"), cliente.get("email"), cliente.get("telefono"), []))

        pedidos_data = [
            {"cliente": "Jose Miguel", "productos": ["Smart TV 4K", "Laptop Gamer"], "fecha": "2024-10-01", "estado": "pendiente"},
            {"cliente": "Vicenta", "productos": ["Tablet Android", "Batería Externa"], "fecha": "2024-10-05", "estado": "enviado"},
            {"cliente": "Roberto", "productos": ["PlayStation 5", "Smartwatch"], "fecha": "2024-10-08", "estado": "entregado"},
            {"cliente": "Jose Miguel", "productos": ["Auriculares Bluetooth"], "fecha": "2024-10-10", "estado": "pendiente"},
            {"cliente": "Concha", "productos": ["Teclado Mecánico", "Ratón Gaming"], "fecha": "2024-10-12", "estado": "pendiente"},
            {"cliente": "Vicenta", "productos": ["Consola Portátil", "Drone con Cámara"], "fecha": "2024-10-15", "estado": "entregado"},
            {"cliente": "Juan Cuesta", "productos": ["Monitor Curvo"], "fecha": "2024-10-18", "estado": "enviado"},
            {"cliente": "Roberto", "productos": ["PC de Escritorio", "Consola Retro"], "fecha": "2024-10-20", "estado": "pendiente"}
        ]

        for pedido in pedidos_data:
            index = -1
            for i in range(len(self.clientes)):
                if self.clientes[i].nombre == pedido.get("cliente"):
                    index = i
            if index != -1:
                self.pedidos.append(Pedido(self.clientes[index], [], datetime.date.fromisoformat(pedido.get("fecha")), pedido.get("estado")))

                for producto in pedido.get("productos"):
                    for producto_objeto in self.productos:
                        if producto == producto_objeto.nombre:
                            self.pedidos[(len(self.pedidos) - 1)].productos.append(producto_objeto)
                            
                            

        tiendas_data = [
            {"nombre": "Tienda Central", "direccion": "Calle Principal 123", "productos": ["Smart TV 4K", "Tablet Android", "Batería Externa"]},
            {"nombre": "Tienda Norte", "direccion": "Avenida Norte 456", "productos": ["Laptop Gamer", "Drone con Cámara", "Consola Portátil"]}
        ]

        for tienda in tiendas_data:
            self.tiendas.append(Tienda(tienda.get("nombre"), tienda.get("direccion"), []))

            for producto in tienda.get("productos"):
                for producto_objeto in self.productos:
                    if producto == producto_objeto.nombre:
                        self.tiendas[(len(self.tiendas) - 1)].productos.append(producto_objeto)


        comerciales_data = [
            {"nombre": "Comercial A", "clientes_asignados": ["Jose Miguel", "Vicenta"], "ventas_realizadas": []},
            {"nombre": "Comercial B", "clientes_asignados": ["Roberto", "Concha", "Juan Cuesta"], "ventas_realizadas": []}
        ]

        for comercial in comerciales_data:
            clientes_asignados: List[Cliente] = []

            for cliente in comercial.get("clientes_asignados"):
                for cliente_objeto in self.clientes:
                    if cliente == cliente_objeto.nombre:
                        clientes_asignados.append(cliente_objeto)

            self.comerciales.append(Comercial(comercial.get("nombre"), clientes_asignados, []))

        ofertas_data = [
            {"producto": "Smart TV 4K", "descuento": 10, "fecha_inicio": "2024-11-01", "fecha_fin": "2024-11-10"},
            {"producto": "Tablet Android", "descuento": 15, "fecha_inicio": "2024-11-03", "fecha_fin": "2024-11-20"},
            {"producto": "Drone con Cámara", "descuento": 20, "fecha_inicio": "2024-11-05", "fecha_fin": "2024-11-15"},
            {"producto": "Consola Portátil", "descuento": 25, "fecha_inicio": "2024-11-08", "fecha_fin": "2024-11-12"}
        ]

        for oferta in ofertas_data:
            index = -1
            for i in range(len(self.productos)):
                if self.productos[i].nombre == oferta.get("producto"):
                    index = i
            if index != -1:
                self.ofertas.append(Oferta(self.productos[index], oferta.get("descuento") ,datetime.date.fromisoformat(oferta.get("fecha_inicio")), datetime.date.fromisoformat(oferta.get ("fecha_fin"))))

        incidencias_data = [
            {"pedido": "Pedido 1", "descripcion": "Producto defectuoso", "fecha_reporte": "2024-10-02", "estado": "pendiente"},
            {"pedido": "Pedido 2", "descripcion": "Retraso en la entrega", "fecha_reporte": "2024-10-06", "estado": "en proceso"},
            {"pedido": "Pedido 4", "descripcion": "Error en la dirección", "fecha_reporte": "2024-10-11", "estado": "resuelta"},
            {"pedido": "Pedido 5", "descripcion": "Producto dañado en el transporte", "fecha_reporte": "2024-10-13", "estado": "pendiente"},
            {"pedido": "Pedido 7", "descripcion": "Cantidad incorrecta", "fecha_reporte": "2024-10-19", "estado": "en proceso"}
        ]

        for incidencia in incidencias_data:
            self.incidencias.append(Incidente(self.pedidos[int(incidencia.get("pedido")[len(incidencia.get("pedido")) - 1:])], incidencia.get("descripcion"), datetime.date.  fromisoformat(incidencia.get("fecha_reporte")), incidencia.get("estado")))

    def mostrar(self, lista: List) -> None:
        for i in range(len(lista)):
            print(f"{Colores.LIGHTGREEN}{i + 1}{Colores.ENDC} - {lista[i]}")

    def crud(self, lista: List, tipo_clase: Producto | Cliente | Pedido | Tienda | Comercial | Oferta | Incidente) -> None:
        while True:
            print(f"{Colores.YELLOW}[{str(tipo_clase.__name__)}]{Colores.ENDC}\n1. Crear 🆕\n2. Editar 🔧\n3. Eliminar 🚮\n4. Mostrar 👀\n5. Volver 🎇")
            
            try:
                op = int(input())
            except ValueError:
                print(f"{Colores.FAIL}{Colores.UNDERLINE}Debe de ser un numero.{Colores.ENDC}")
                return
            
            match op:
                case 1:  
                    nuevo_objeto = tipo_clase()  
                    nuevo_objeto.modificar(self)     
                    lista.append(nuevo_objeto)
                case 2:  
                    #? se podrian factorizar muchas cosas de mostrar
                    self.mostrar(lista)
                    print("Introduce indice a modificar: ")
                    try:
                        indice = int(input()) - 1
                        if 0 <= indice < len(lista):
                            lista[indice].modificar(self)
                        else:
                            print(f"{Colores.FAIL}{Colores.UNDERLINE}Indice fuera de rango.{Colores.ENDC}")
                    except ValueError:
                        print(f"{Colores.FAIL}{Colores.UNDERLINE}Debe de ser un numero.{Colores.ENDC}")
                case 3:  
                    self.mostrar(lista)
                    print("Introduce indice a eliminar: ")
                    try:
                        indice = int(input()) - 1
                        if 0 <= indice < len(lista):
                            lista.pop(indice)
                        else:
                            print(f"{Colores.FAIL}{Colores.UNDERLINE}Indice fuera de rango.{Colores.ENDC}")
                    except ValueError:
                        print(f"{Colores.FAIL}{Colores.UNDERLINE}Debe de ser un numero.{Colores.ENDC}")
                case 4:  
                    self.mostrar(lista)
                case 5:
                    return
                case _:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}Opcion invalida.{Colores.ENDC}")
            
            print("Pulse enter para continuar....")
            input()
            os.system('cls')

    def run(self):
        os.system('cls')
        print(f"{Colores.YELLOW}Bienvendo al administrador. Pulse enter para comenzar 😁{Colores.ENDC}")
        input()
        
        loop = False
        
        while (True):
            if loop:
                print("Pulse enter para continuar...")
                input()      
            os.system('cls')
            
            print(f"{Colores.YELLOW}[Menu principal]{Colores.ENDC}\n1. Productos 🛒\n2. Clientes 👨👩\n3. Pedidos 📦\n4. Tiendas 🏤\n5. Comerciales 💼\n6. Ofertas 🎡\n7. Incidencias 🔔\n8. Salir ❌")
            try:
                op = int(input())
            except:
                print(f"{Colores.FAIL}{Colores.UNDERLINE}Debe de ser un numero.{Colores.ENDC}")
            else:
                if op == 8:
                    exit()
                
                opciones_lista = {
                    1: self.productos,
                    2: self.clientes,
                    3: self.pedidos,
                    4: self.tiendas,
                    5: self.comerciales,
                    6: self.ofertas,
                    7: self.incidencias,
                }
                clases_lista = {
                    1: Producto,
                    2: Cliente,
                    3: Pedido,
                    4: Tienda,
                    5: Comercial,
                    6: Oferta,
                    7: Incidente,
                }
                
                if op in opciones_lista:
                    self.crud(opciones_lista[op], clases_lista[op])
                else:
                    print(f"{Colores.FAIL}{Colores.UNDERLINE}Opcion invalida.{Colores.ENDC}")
                    
                if not loop:
                    loop = True

def main():
    gestor_tienda = GestorTienda()
    gestor_tienda.run()

if __name__ == "__main__":
    main()
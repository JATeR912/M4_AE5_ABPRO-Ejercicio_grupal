from datetime import datetime
from bicicleta import Bicicleta
from error import FormatoRutInvalido

class Reservas:
    reservas_realizadas = 0
    def __init__(self, rut_cliente, id_reserva, fecha_inicio, fecha_fin, bicicleta, monto=0): 
        self.rut_cliente = rut_cliente
        self.id_reserva = id_reserva
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.bicicleta = bicicleta
        self.monto = monto

    def reserva(self):
        try:
            cliente = input("Ingrese su rut (sin puntos ni guión): ")
            fecha_inicio = input("Ingrese la fecha y hora de inicio (mm/dd/aaaa hh:mm): ")
            fecha_fin = input("Ingrese la fecha y hora de término (mm/dd/aaaa hh:mm): ")

            if len(cliente) != 9:
                raise FormatoRutInvalido(cliente)

            fecha_inicio = datetime.strptime(fecha_inicio, "%m/%d/%Y %H:%M")
            fecha_fin = datetime.strptime(fecha_fin, "%m/%d/%Y %H:%M")

            self.rut_cliente = cliente
            self.fecha_inicio = fecha_inicio
            self.fecha_fin = fecha_fin

            print(f"El rut es: {cliente}")
            print(f"Fecha inicio: {fecha_inicio.strftime('%m/%d/%Y %H:%M')}")
            print(f"Fecha fin: {fecha_fin.strftime('%m/%d/%Y %H:%M')}")

        except (FormatoRutInvalido, ValueError) as e:
            print(f"Error al registrar la reserva: {e}")

        else:
            self.bicicleta.disponible()
            aceptar = input("¿Desea realizar la reserva? (si/no): ").lower()
            if aceptar == "si":
                self.bicicleta.disponibilidad = False
                print(f"Se confirma la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
            else:
                self.bicicleta.disponibilidad = True
                print(f"No se ha realizado la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
                self.bicicleta.precio = 0

        finally:
            print("Proceso de reserva finalizado.\n")

        return self
    

    def cancelar_reserva (self):
        cancelar = input("Desea cancelar la reserva : si/no ")
        if cancelar == "si":
            self.bicicleta.disponibilidad = True
            print(f"Se ha cancelado la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
        else:
            print(f"Se confirma la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
        print()
        return self
    
    def monto_pagar (self):
        monto_dias = self.fecha_fin - self.fecha_inicio
        monto_horas = monto_dias.total_seconds() / 3600
        monto = monto_horas * self.bicicleta.precio
        self.monto = monto
        print(f"El monto a pagar es de: ${monto}")
        print()
        return self

    def pago (self):
        if self.monto == 0:
            print("No hay saldo pendiente.")
        else:
            input("Presente la TDC : ")
            print("Pago realizado con éxito")
            self.bicicleta.disponibilidad = True
        print()
        return self

            
        
        
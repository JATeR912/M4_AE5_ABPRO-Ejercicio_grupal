from bicicletas import Bicicleta
from reservas import Reservas    
from datetime import datetime

bicicleta1:Bicicleta = Bicicleta(1, "merida", "Big Nine 500", True, 2000) 
bicicleta2:Bicicleta = Bicicleta(2, "Bianchi", "Trek", True, 1000)
bicicleta3:Bicicleta = Bicicleta(3, "Silverback", "Strela", True, 3000)

inventario_bicicletas = [bicicleta1, bicicleta2, bicicleta3]

fecha_inicio1= datetime(2025, 8, 10, 10, 00)
fecha_fin1= datetime(2025, 8, 11, 10, 00)

fecha_inicio2= datetime(2025, 8, 15, 13,30)
fecha_fin2= datetime(2025, 8, 17, 16,00)

fecha_inicio3= datetime(2025, 8, 12, 10,00)
fecha_fin3= datetime(2025, 8, 22, 18,30)   

reserva1:Reservas = Reservas(12345678, 1, fecha_inicio1, fecha_fin1, bicicleta1) 
reserva2:Reservas = Reservas(12345678, 2, fecha_inicio2, fecha_fin2, bicicleta2)
reserva3:Reservas = Reservas(12345678, 3, fecha_inicio3, fecha_fin3, bicicleta3)  

inventario_reservas = [reserva1, reserva2, reserva3]    

reserva1.reserva()
reserva1.monto_pagar()
reserva1.pago()
reserva1.cancelar_reserva()
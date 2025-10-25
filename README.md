# 🚴‍♂️ BIKECITY – Sistema de Gestión de Renta de Bicicletas

## 📋 Descripción General

**BIKECITY** es un sistema automatizado desarrollado en **Python** para gestionar la renta de bicicletas urbanas.  
Su objetivo es eliminar errores comunes del sistema manual como reservas duplicadas, cobros incorrectos y falta de control del inventario.

El sistema aplica principios de **Programación Orientada a Objetos (POO)** y un manejo estructurado de **excepciones**, garantizando procesos más seguros y confiables.

---

## 🎯 Objetivos del Sistema

- Registrar bicicletas disponibles para renta.  
- Gestionar reservas evitando conflictos de horario.  
- Calcular cobros según la duración del uso.  
- Controlar el estado (disponible/reservada) de cada bicicleta.  
- Implementar manejo de errores con excepciones personalizadas.  

---

## 🧩 Estructura del Proyecto

📁 BIKECITY/
│
├── main.py # Archivo principal del sistema (ejecución general)
├── bicicletas.py # Clase Bicicleta y funciones de registro y disponibilidad
├── reservas.py # Clase Reservas y manejo de procesos de reserva/pago
├── error.py # Definición de excepciones personalizadas
│
├── bikecity.png # Diagrama de clases UML
├── respuestas.pdf # Documento teórico con respuestas sobre manejo de excepciones
│
└── README.md # Este archivo

yaml
Copiar código

---

## 🧠 Paso 1: Conceptualización y Análisis

El documento **respuestas.pdf** incluye las respuestas a los temas teóricos solicitados:

1. ¿Qué es una excepción y por qué es importante manejarla?  
2. Tipos comunes de excepciones.  
3. Uso del bloque `try/except`.  
4. Captura de múltiples excepciones.  
5. Uso de `raise` para generar errores personalizados.  
6. Creación de excepciones propias.  
7. Función del bloque `finally`.  
8. Acciones de limpieza después de errores.  

---

## 💻 Paso 2: Implementación en Código

### 🏍️ `bicicletas.py`

Define la clase **`Bicicleta`**, con los siguientes atributos y métodos:

```python
class Bicicleta:
    def __init__(self, id_bicicleta, marca, modelo, disponibilidad, precio):
        self.id_bicicleta = id_bicicleta
        self.marca = marca
        self.modelo = modelo
        self.disponibilidad = disponibilidad
        self.precio = precio
Métodos principales:

registrar(): Guarda la información de la bicicleta en un archivo de texto (bicicletas.txt), usando try/except/finally para manejar errores de archivo.

disponible(): Indica si la bicicleta está disponible o reservada.

Ejemplo de manejo de excepciones:

python
Copiar código
try:
    archivo = open("bicicletas.txt", "a")
    archivo.write(...)
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    archivo.close()
📅 reservas.py
Define la clase Reservas, encargada de:

Crear reservas.

Calcular el monto a pagar.

Procesar pagos y cancelaciones.

Incluye manejo de errores con try/except, raise y excepciones personalizadas.

Ejemplo de flujo principal:

python
Copiar código
def reserva(self):
    try:
        cliente = input("Ingrese su rut (sin puntos ni guión): ")
        if len(cliente) != 9:
            raise FormatoRutInvalido(cliente)
        ...
    except (FormatoRutInvalido, ValueError) as e:
        print(f"Error al registrar la reserva: {e}")
    finally:
        print("Proceso de reserva finalizado.\n")
Métodos clave:

reserva(): Registra una nueva reserva validando RUT y fechas.

monto_pagar(): Calcula el monto total según horas de uso.

pago(): Simula un pago exitoso y libera la bicicleta.

cancelar_reserva(): Permite cancelar una reserva activa.

### ⚠️ `error.py`
Contiene las excepciones personalizadas del sistema.

python
Copiar código
class FormatoRutInvalido(Exception):
    """Excepción lanzada cuando el RUT no cumple el formato esperado."""
    def __init__(self, rut):
        super().__init__(f"El RUT '{rut}' no tiene un formato válido (debe tener 9 caracteres).")
Estas excepciones permiten distinguir errores específicos del negocio de los errores genéricos del sistema.

### 🚀 `main.py`
Archivo principal que crea instancias, simula reservas y ejecuta el sistema completo:

python
Copiar código
from bicicletas import Bicicleta
from reservas import Reservas    
from datetime import datetime
Flujo del programa:

Se crean bicicletas y se almacenan en una lista inventario_bicicletas.

Se definen fechas de inicio y fin para las reservas.

Se instancian objetos Reservas asociados a bicicletas.

Se ejecutan los métodos principales:

reserva()

monto_pagar()

pago()

cancelar_reserva()

Ejemplo de uso:

python
Copiar código
reserva1.reserva()
reserva1.monto_pagar()
reserva1.pago()
reserva1.cancelar_reserva()


### 🧪 `Ejecución del Proyecto`
Clona o descarga el repositorio.

Abre una terminal en la carpeta del proyecto.

Ejecuta el programa principal:

bash
Copiar código
python main.py
Sigue las instrucciones del sistema (ingresar RUT, fechas, etc.).

Observa los mensajes de validación, errores controlados y confirmaciones.

### 👨‍💻 `Colaboradores`
Proyecto desarrollado por:

*Linwi Vargas([Linwi-V](https://github.com/Linwi-V))

*Emily Quintana([EmyQuintana](https://github.com/EmyQuintana))

*Natalia Rodriguez([npuntorodriguez](https://github.com/npuntorodriguez))

*Johana Torres([JATeR912](https://github.com/JATeR912))

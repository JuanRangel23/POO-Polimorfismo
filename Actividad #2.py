# Clase base Empleado
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base  # Encapsulamiento del sueldo base

# Getter para sueldo_base
    def get_sueldo_base(self):
        return self.__sueldo_base

# Setter para sueldo_base
    def set_sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            print("El sueldo no puede ser negativo.")

# Método que se sobrescribirá en las clases hijas
    def calcular_salario(self):
        pass

# Clase para empleados fijos: reciben su sueldo base sin cambios
class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return self.get_sueldo_base()

# Clase para empleados por horas: se les paga por horas trabajadas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora


# Clase para empleados temporales: ganan el sueldo base más un bono temporal
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, bono_temporal):
        super().__init__(nombre, sueldo_base)
        self.bono_temporal = bono_temporal

    def calcular_salario(self):
        return self.get_sueldo_base() + self.bono_temporal


# Creamos una lista de empleados con diferentes tipos
empleados = [
    EmpleadoFijo("Ana", 3000),
    EmpleadoPorHoras("Luis", 0, horas_trabajadas=120, pago_por_hora=20),
    EmpleadoTemporal("Sofía", 2500, bono_temporal=500)
]

# Mostramos el salario de cada empleado usando polimorfismo
for empleado in empleados:
    print(f"Empleado: {empleado.nombre} - Salario: {empleado.calcular_salario()}")


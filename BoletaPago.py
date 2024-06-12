class Trabajador:
    def __init__(self, _nombre, _categoria, _horas_extras, _tardanzas):
        self.nombre = _nombre
        self.categoria = _categoria
        self.horas_extras = _horas_extras
        self.tardanzas = _tardanzas

    def calcular_sueldo_basico(self):
        sueldos = {"A": 3000, "B": 2500, "C": 2000}
        return sueldos.get(self.categoria, 0)

    def calcular_pago_hora_extra(self):
        sueldo_basico = self.calcular_sueldo_basico()
        pago_por_hora = sueldo_basico / 240
        return pago_por_hora * self.horas_extras

    def calcular_descuento_tardanzas(self):
        descuento_por_minuto = self.calcular_sueldo_basico() / 240 / 60
        return descuento_por_minuto * self.tardanzas

    def calcular_sueldo_neto(self):
        sueldo_basico = self.calcular_sueldo_basico()
        pago_hora_extra = self.calcular_pago_hora_extra()
        descuento_tardanzas = self.calcular_descuento_tardanzas()
        sueldo_neto = sueldo_basico + pago_hora_extra - descuento_tardanzas
        return sueldo_neto

class Boleta(Trabajador):
    def generar_boleta_pago(self):
        sueldo_basico = self.calcular_sueldo_basico()
        pago_hora_extra = self.calcular_pago_hora_extra()
        descuento_tardanzas = self.calcular_descuento_tardanzas()
        sueldo_neto = self.calcular_sueldo_neto()

        print("*** BOLETA DE PAGO ***")
        print('{:<20}: {}'.format("NOMBRE", self.nombre))
        print('{:<20}: {}'.format("CATEGORIA", self.categoria))
        print('{:<20}: {:,.2f}'.format("SUELDO BASICO", sueldo_basico))
        print('{:<20}: {:,.2f}'.format("DESCUENTO TARDANZAS", descuento_tardanzas))
        print('{:<20}: {:,.2f}'.format("PAGO HORAS EXTRAS", pago_hora_extra))
        print('{:<20}: {:,.2f}'.format("SUELDO NETO", sueldo_neto))

nombre = input("Ingrese el nombre del trabajador: ")
categoria = input("Ingrese la categoría del trabajador (A, B o C): ")
horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
tardanzas = int(input("Ingrese el total de minutos de tardanzas: "))

print("*** DATOS DE ENTRADA ***")
print('{:<20}: {}'.format("TRABAJADOR", nombre))
print('{:<20}: {}'.format("CATEGORIA", categoria))
print('{:<20}: {:.2f}'.format("HORAS EXTRAS", horas_extras))
print('{:<20}: {}'.format("TARDANZAS (minutos)", tardanzas))

boleta_trabajador = Boleta(nombre, categoria, horas_extras, tardanzas)
boleta_trabajador.generar_boleta_pago()

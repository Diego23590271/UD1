class Trabajador: 
    def __init__(self, nombre, cajas):
        self.nombre = nombre
        self.cajas = cajas
        self.pago = 0
        self.pagot = 0
        self.descuento = 0

    def cal_pago(self):
        if self.cajas <= 10:
            self.pago = self.cajas * 50  
        elif 10 < self.cajas <= 80:  
            self.pago = (10 * 50) + (self.cajas - 10) * (50 * 1.5)
        else:
            self.pago = (10 * 50) + (70 * (50 * 1.5)) + (self.cajas - 80) * (50 * 2)

    def cal_descuento(self):
        self.descuento = self.pago * 0.05

    def cal_pagototal(self):
        self.cal_pago()  
        self.cal_descuento()  
        self.pagot = self.pago - self.descuento

    def conteo_cajas(self):
        abajo_10 = self.cajas < 10
        entre_50_y_80 = 50 <= self.cajas <= 80
        arriba_80 = self.cajas > 80
        
        return {
            "abajo_10": abajo_10,
            "entre_50_y_80": entre_50_y_80,
            "arriba_80": arriba_80
        }

    def resultado(self):
        conteo = self.conteo_cajas()
        print(f"Nombre del trabajador: {self.nombre}")
        print(f"Cajas cosechadas: {self.cajas}")
        print(f"Pago: ${self.pago:}")
        print(f"Descuento para caja de ahorro (5%): ${self.descuento:}")
        print(f"Pago total: ${self.pagot:}")
        print(f"Cajas abajo de 10: {'Sí' if conteo['abajo_10'] else 'No'}")
        print(f"Cajas entre 50 y 80: {'Sí' if conteo['entre_50_y_80'] else 'No'}")
        print(f"Cajas arriba de 80: {'Sí' if conteo['arriba_80'] else 'No'}")

def sistema():
    while True:
        nombre = input("Introduce el nombre del trabajador o si desea salir escriba 'salir' para terminar: ")
        if nombre.lower() == 'salir': 
            print("Saliendo...")
            break

        try:
            cajas = int(input("Introduce la cantidad de cajas cosechadas: "))
            if cajas < 0:
                print("La cantidad de cajas no puede ser negativa.")
                continue
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        t = Trabajador(nombre, cajas)

        t.cal_pagototal()
        t.resultado()

sistema()

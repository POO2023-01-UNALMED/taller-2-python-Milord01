
class Auto: 
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        Auto.cantidadCreados=self.cantidadCreados

    def cantidadAsientos(self):
        a=0
        for i in self.asientos:
            if isinstance(i,Asiento):
                a+=1
        return a
    def verificarIntegridad(self):
        b=True
        if self.motor.registro!= self.registro:
            b=False


        for i in self.asientos:
            if isinstance (i,Asiento):
              if i.registro!=self.registro:
                 b=False


        if b==True:
            return("Auto original")
        else:
            return("Las piezas no son originales")


class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro 

    def cambiarColor(self,color):
        if color=='rojo'or color=='verde'or color=='negro'or color=='amarillo' or color=='blanco':
            self.color=color
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,registro):
        self.registro=registro
    def asignarTipo(self,tipo):
        if tipo=='electrico'or tipo=='gasolina':
            self.tipo=tipo
    
    




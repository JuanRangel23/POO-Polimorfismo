class Transporte:
    def tipo_transpote(self):
        print("Soy un Transporte de tipo:")
   

class Coche(Transporte):
    def tipo_transpote(self):
        return "Soy un trasporte de tipo Terrestre"
    
class Avion(Transporte):
    def tipo_transpote(self):
        return "Soy un transporte de tipo Aereo"

class Barco(Transporte):
    def tipo_transpote(self):
        return "Soy un transporte de tipo Maritimo"
    
Mazda = Coche()

Avianca = Avion()

Titanic = Barco()

print(Mazda.tipo_transpote())
print(Avianca.tipo_transpote())
print(Titanic.tipo_transpote())

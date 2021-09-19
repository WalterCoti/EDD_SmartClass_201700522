class estudiante:
    def __init__(self, ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_, yearlist_):
        self.carnet = ncarnet_
        self.dpi = dpi_
        self.nombre = nombre_
        self.carrera = carrera_
        self.correo = correo_
        self.passw = passw_
        self.credito = credit_
        self.edad = edad_
        self.yearlist = yearlist_


    def getcarnet(self):
        return  self.carnet

    def getdpi(self):
        return self.dpi

    def getnombre(self):
        return self.nombre

    def getcarrera(self):
        return  self.carrera

    def getcorreo(self):
        return self.correo

    def getpassw(self):
        return self.passw

    def getcredito(self):
        return self.credito

    def getedad(self):
        return self.edad


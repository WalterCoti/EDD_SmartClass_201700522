
class NodoSemestre:
    def __init__(self,Nsemestre_):
        self.semestre = Nsemestre_
        self.Cursos = None
        self.sig = None


class ListSemestre:
    def __init__(self):
        self.head = None
        self.size = 0
    def existe(self,semestre_):
        aux = self.head
        while aux is not None:
            if aux.semestre == semestre_:
                return True
            aux = aux.sig
        return False

    def addSemestre(self,semestre_):
        nwSemestre = NodoSemestre(semestre_)
        if self.size < 2:
            if nwSemestre.semestre > 0 and nwSemestre.semestre < 3:
                if self.head == None:
                    self.head = nwSemestre
                else:
                    if self.head.semestre > semestre_:
                        nwSemestre.sig = self.head
                        self.head = nwSemestre
                    else:
                        self.head.sig = nwSemestre
                self.size += 1
            else:
                print("El numero de semestre no es valido: " + str(semestre_))
        else:
            print("la cantidad de semestres excede la cantidad permitida")

    def printlist(self):
        aux = self.head
        while aux is not None:
            print("Semestre" + str(aux.semestre))
            aux = aux.sig

#
# nwList = ListSemestre()
# nwList.addSemestre(2)
# nwList.addSemestre(2)
# nwList.addSemestre(3)
# nwList.printlist()
class NodoSemestre:
    def __init__(self,Nsemestre_):
        self.semestre = Nsemestre_
        self.Cursos = None
        self.sig = None


class ListSemestre:
    def __init__(self):
        self.head = None
        self.size = 0

    def addSemestre(self,semestre_):
        nwSemestre = NodoSemestre(semestre_)
        if self.size > 2:
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
            print("el numero de semestres excede la cantidad permitida")

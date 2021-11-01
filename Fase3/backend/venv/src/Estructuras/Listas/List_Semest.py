from Estructuras.arboles import BTreeCur
class NodoSemestre:
    def __init__(self,Nsemestre_):
        self.semestre = Nsemestre_
        self.cursos = None
        self.sig = None


class ListSemestre:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def getSemestre(self,semestre_):
        aux = self.head
        while aux is not None:
            if aux.semestre == semestre_:
                return aux
            aux = aux.sig
        return None

    def add_curso_semestre(self,semestre_,codigo_,nombre_,creditos_,prereq_,obligatorio_):
        tmp = self.getSemestre(semestre_)
        if tmp:
            tmp.cursos.addCurso(codigo_, nombre_, creditos_, prereq_, obligatorio_)
        else:
            self.addSemestre(semestre_,codigo_,nombre_,creditos_,prereq_,obligatorio_)
            

    def addSemestre(self,semestre_,codigo_,nombre_,creditos_,prereq_,obligatorio_):
        nwSemestre = NodoSemestre(semestre_)
        nwSemestre.cursos = BTreeCur.ArbolB_Cursos()
        nwSemestre.cursos.addCurso(codigo_, nombre_, creditos_, prereq_, obligatorio_)
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


from Estructuras.ListMes import ListMes
from Estructuras.ListSemest import ListSemestre

class NodoYear:
    def __init__(self, year_):
        self.year = year_
        self.mes = None
        self.semestre = None
        self.sig = None

class ListYear:
    def __init__(self):
        self.size = 0
        self.head = None

    def getYear(self,year_):
        ntmp = self.head
        while ntmp:
            if ntmp.year == year_:
                return ntmp
            ntmp = ntmp.sig
        return None

    def add_task_year(self,NodoTask,year_, mes_, dia_, hora_):
        tmpNodo = self.getYear(year_)
        if tmpNodo is not None:
            tmpNodo.mes.add_task_mes(NodoTask,mes_, dia_, hora_)
        else:
            self.addYear(NodoTask, year_, mes_, dia_, hora_)

        #reparar

    def addYear(self,NodoTask, year_, mes_, dia_, hora_):
        nw_nodo = NodoYear(year_)
        nw_nodo.mes = ListMes()
        nw_nodo.mes.add_task_mes(NodoTask, mes_, dia_, hora_)
        if self.head is None or self.head.year > nw_nodo.year:
            nw_nodo.sig = self.head
            self.head = nw_nodo
        else:
            tmp = self.head
            while tmp.sig is not None and tmp.sig.year < nw_nodo.year:
                tmp = tmp.sig
            nw_nodo.sig = tmp.sig
            tmp.sig = nw_nodo
        self.size += 1

    def imprimir(self):
        tmp = self.head
        if self.head is None:
            print("lista vacia")
        else:
            while tmp is not None:
                if tmp.sig is not None:
                    print(str(tmp.year) + " -> " + str(tmp.sig.year))
                tmp = tmp.sig

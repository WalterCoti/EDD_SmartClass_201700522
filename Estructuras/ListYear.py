# from Estructuras.ListMes import ListMes
# from Estructuras.ListSemest import ListSemestre
# import Estructuras.ListSemest

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

    def existeyear(self,year_):
        tmp = self.head
        while tmp is not None:
            if tmp.year == year_:
                return True
            tmp = tmp.sig
        return False

    def addYear(self, year_):
        nw_nodo = NodoYear(year_)
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

    def buscar(self, year_):
        tmpN = NodoYear(year_)


    def graficar(self):
        pass

    def imprimir(self):
        tmp = self.head
        if self.head is None:
            print("lista vacia")
        else:
            while tmp is not None:
                if tmp.sig is not None:
                    print(str(tmp.year) + " -> " + str(tmp.sig.year))
                tmp = tmp.sig


# sptm = ListYear()
# sptm.addYear(1995)
# sptm.addYear(1999)
# sptm.addYear(1996)
# sptm.addYear(1993)
# sptm.addYear(2021)
# sptm.addYear(1500)
# sptm.imprimir()

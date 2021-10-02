import time
from Estructuras.ListYear import ListYear
from os import system
from datetime import datetime

class NodoStd:
    def __init__(self,ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_ ):
        self.carnet = ncarnet_
        self.dpi = dpi_
        self.nombre = nombre_
        self.carrera = carrera_
        self.correo = correo_
        self.passw = passw_
        self.credito = credit_
        self.edad = edad_
        self.yearlist = None
        self.Nizq = None
        self.Nder = None
        self.Tamanio = 0

    def getlistyear(self):
        return  self.yearlist

    def setyear_list(self,year_):
        self.yearlist.addYear(year_)


class AVLTree:
    def __init__(self):
        self.raiz = None

    def height(self,nodo):
        if nodo is not None:
            return nodo.Tamanio
        return -1

    def insert(self, Stdcarnet_, StdNodpi_, Stdnombre_, Stdcarrera_, Stdemail_, Stdpassw_, Stdcredit_, Stdedad_):

        self.raiz = self.insertar_inter(Stdcarnet_, StdNodpi_, Stdnombre_, Stdcarrera_, Stdemail_, Stdpassw_, Stdcredit_, Stdedad_, self.raiz)

    def insertar_inter(self, ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_, raiz_):
        if raiz_ is None:
            nwNodoSt = NodoStd(ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_)
            nwlstYear = ListYear()
            nwNodoSt.yearlist = nwlstYear
            return  nwNodoSt
        else:
            if ncarnet_ < raiz_.carnet:
                raiz_.Nizq = self.insertar_inter(ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_,raiz_.Nizq)
                if self.height(raiz_.Nder) - self.height(raiz_.Nizq) == -2:
                    if ncarnet_ < raiz_.Nizq.carnet:
                        raiz_ = self.RI(raiz_)
                    else:
                        raiz_ = self.RDI(raiz_)
            elif ncarnet_ > raiz_.carnet:
                raiz_.Nder = self.insertar_inter(ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_,raiz_.Nder)
                if self.height(raiz_.Nder) - self.height(raiz_.Nizq) == 2:
                    if ncarnet_ > raiz_.Nder.carnet:
                        raiz_ = self.RD(raiz_)
                    else:
                        raiz_ = self.RID(raiz_)
            else:
                raiz_ = NodoStd(ncarnet_, dpi_, nombre_, carrera_, correo_, passw_, credit_, edad_)

        raiz_.Tamanio = max(self.height(raiz_.Nizq), self.height(raiz_.Nder)) + 1

        return raiz_

    def RI(self, nodo):
        aux = nodo.Nizq
        nodo.Nizq = aux.Nder
        aux.Nder = nodo
        nodo.Tamanio = max(self.height(nodo.Nizq), self.height(nodo.Nder)) + 1
        aux.Tamanio = max(self.height(aux.Nizq), self.height(aux.Nder)) + 1
        return aux

    def RD(self, nodo):
        aux = nodo.Nder
        nodo.Nder = aux.Nizq
        aux.Nizq = nodo
        nodo.Tamanio = max(self.height(nodo.Nizq), self.height(nodo.Nder)) + 1
        aux.Tamanio = max(self.height(aux.Nizq), self.height(aux.Nder)) + 1
        return aux

    def RDI(self,nodo):
        nodo.Nizq = self.RD(nodo.Nizq)
        return self.RI(nodo)

    def RID(self,nodo):
        nodo.Nder = self.RI(nodo.Nder)
        return self.RD(nodo)

    def delete(self,ncarnet):
        try:
            self.raiz = self.delete_Nodo(ncarnet,self.raiz)
        except:
            print("error inesperado")

    def delete_Nodo(self, ncarnet_,nodo):
        rev = ncarnet_
        aver = nodo.carnet
        if nodo is None:
            return nodo
        if ncarnet_ == nodo.carnet:
            if nodo.Nizq is not None and nodo.Nder is not None:
                aux = self.maximo(nodo.Nizq)
                nodo.carnet = aux.carnet
                # nodo.dpi = aux.dpi
                # nodo.nombre = aux.nombre_
                # nodo.carrera = aux.carrera_
                # nodo.correo = aux.correo_
                # nodo.passw = aux.passw_
                # nodo.credito = aux.credit_
                # nodo.edad = aux.edad_
                # nodo.yearlist = aux.yearlist
                # nodo.Tamanio = aux.Tamanio

               # tmp = nodo
              #  nodo = aux
               # nodo.Nder = tmp.Nder
                #nodo.Nizq = self.delete_Nodo(aux.carnet,tmp.Nizq)
                tmp = aux
                nodo.Nizq = self.delete_Nodo(nodo.carnet, nodo.Nizq)

            elif nodo.Nizq is None and nodo.Nder is None:
                return None
            elif nodo.Nizq is None and nodo.Nder is not None:
                nodo = nodo.Nder
            elif nodo.Nder is None and nodo.Nizq is not None:
                nodo = nodo.Nizq
        elif ncarnet_ < nodo.carnet:
            nodo.Nizq = self.delete_Nodo(ncarnet_,nodo.Nizq)
        elif ncarnet_ > nodo.carnet:
            nodo.Nder = self.delete_Nodo(ncarnet_, nodo.Nder)
        nodo.Tamanio = max(self.height(nodo.Nder),self.height(nodo.Nizq)) + 1
        nodo = self.balancear(nodo, ncarnet_)
        return nodo

    def balancear(self,raiz_,ncarnet_):
        if self.height(raiz_.Nizq) - self.height(raiz_.Nder) == -2:
            if ncarnet_ < raiz_.Nizq.carnet:
                raiz_ = self.RI(raiz_)
            else:
                raiz_ = self.RDI(raiz_)

        if self.height(raiz_.Nder) - self.height(raiz_.Nizq) == 2:
            if ncarnet_ >= raiz_.Nder.carnet:
                raiz_ = self.RD(raiz_)
            else:
                raiz_ = self.RID(raiz_)
        return raiz_

    def maximo(self,nodo):
        if nodo.Nder is None:
            return nodo
        else:
            return self.maximo(nodo.Nder)

    #tupla [raiz, nodo izquierdo, nodo derecho]
    def recorrer_arbol(self,nodo,listNodos_):
        if nodo is not None:
            if nodo.Nizq is None and nodo.Nder is not None:
                listNodos_.append([nodo.carnet, None , nodo.Nder.carnet,nodo.carnet,nodo.nombre,nodo.carrera])
                self.recorrer_arbol(nodo.Nder, listNodos_)
            elif nodo.Nder is None and nodo.Nizq is not None:
                listNodos_.append([nodo.carnet, nodo.Nizq.carnet, None,nodo.carnet,nodo.nombre,nodo.carrera])
                self.recorrer_arbol(nodo.Nizq, listNodos_)
            elif nodo.Nder is None and nodo.Nizq is  None:
                listNodos_.append([nodo.carnet, None, None,nodo.carnet,nodo.nombre,nodo.carrera])
            else:
                listNodos_.append([nodo.carnet, nodo.Nizq.carnet, nodo.Nder.carnet, nodo.carnet, nodo.nombre, nodo.carrera])
                self.recorrer_arbol(nodo.Nizq, listNodos_)
                self.recorrer_arbol(nodo.Nder, listNodos_)

    def generarGraph(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute)  + "-" + str(timenow.second)
        self.graphAVL(nameFile)

    #generar archivo.dot
    def graphAVL(self,nombre):
        listNod = []
        file = open(nombre + "-avl.dot", "w")
        file.write("digraph d {\n")
        file.write("\tnode [shape = record, style=rounded];\n")
        self.recorrer_arbol(self.raiz,listNod)
        for nodo in listNod:
            file.write(str(nodo[0]) +"[label=\"" + str(nodo[3]) +" \\n " + str(nodo[4]) +" \\n " + str(nodo[5]) + "\"]; \n")
            if nodo[1] is None and nodo[2] is not None:
                file.write(str(nodo[0]) + "->"+ str(nodo[2])+";\n")
            elif nodo[1] is not None and nodo[2] is None:
                file.write(str(nodo[0]) + "->" + str(nodo[1])+";\n")
            elif nodo[1] is  None and nodo[2] is None:
                pass
            else:
                file.write(str(nodo[0]) + "->" + str(nodo[1])+";\n")
                file.write(str(nodo[0]) + "->" + str(nodo[2])+";\n")

        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-avl.dot -o " + nombre + "-avl.png"
            system(executecmd)
            system("start " + nombre + "-avl.png ")
        except:
            print("Error al abrir la imagen")

    def getStudentNode(self,raiz_,carnet_):
        if raiz_ is None:
            return None
        elif raiz_.carnet == carnet_:
            return raiz_
        elif raiz_.carnet < carnet_:
            self.getStudentNode(raiz_.Nder, carnet_)
        else:
            return self.getStudentNode(raiz_.Nizq,carnet_)
        return None

    def add_year_in_list(self,carnet_,year_):
        nodo = self.getStudentNode(self.raiz,carnet_)
        if nodo is not None:
            nodo.setyear_list(year_)
        else:
            print("el estudiante no se encuentra registrado")

    def add_Mes(self,carnet_,mes):
        pass

    def add_task(self):
        pass
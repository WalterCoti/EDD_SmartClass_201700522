import time

from ListYear import  ListYear
import os
from os import system
from os import path
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

    def inOrden(self):
        self.in_OrdenInter(self.raiz)

    def in_OrdenInter(self,raiz_):
        if raiz_ is not None:
            self.in_OrdenInter(raiz_.Nizq)
            print(str(raiz_.carnet))
            self.in_OrdenInter(raiz_.Nder)

    def delete(self,ncarnet):
        try:
            self.raiz = self.delete_Nodo(ncarnet,self.raiz)
        except:
            print("error inesperado")

    def delete_Nodo(self, ncarnet_,nodo):
        if nodo is None:
            return nodo
        if ncarnet_ == nodo.carnet:
            if nodo.Nizq is not None and nodo.Nder is not None:
                aux = self.maximo(nodo.Nizq)
                nodo.carnet = aux.carnet
                nodo.Nizq = self.delete_Nodo(nodo.carnet,nodo.Nizq)
            elif nodo.Nizq is None and nodo.Nder is None:
                return None
            elif nodo.Nizq is None:
                nodo = nodo.Nder
            elif nodo.Nder is None:
                nodo = nodo.Nizq
        elif ncarnet_ < nodo.carnet:
            nodo.Nizq = self.delete_Nodo(ncarnet_,nodo.Nizq)
        elif ncarnet_ > nodo.carnet:
            nodo.Nder = self.delete_Nodo(ncarnet_, nodo.Nder)

        nodo = self.balancear(nodo,ncarnet_)
        nodo.Tamanio = max(self.height(nodo.Nder),self.height(nodo.Nizq)) + 1
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
                listNodos_.append([nodo.carnet, None , nodo.Nder.carnet])
            elif nodo.Nder is None and nodo.Nizq is not None:
                listNodos_.append([nodo.carnet, nodo.Nizq.carnet, None])
            elif nodo.Nder is None and nodo.Nizq is  None:
                pass
            else:
                listNodos_.append([nodo.carnet,nodo.Nizq.carnet,nodo.Nder.carnet])
                self.recorrer_arbol(nodo.Nder, listNodos_)
                self.recorrer_arbol(nodo.Nizq,listNodos_)


    def generarGraph(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute)  + "-" + str(timenow.second)
        self.graphAVL(nameFile)

    #generar archivo.dot
    def graphAVL(self,name):
        listNod = []

        nombre = name
        file = open(nombre + "-avl.dot", "w")
        file.write("digraph d {\n")
        file.write("\tnode [shape = circle];\n")
        self.recorrer_arbol(self.raiz,listNod)
        for nodo in listNod:
           # file.write(str(nodo) +"[label=\"" + str(nodo) + "\"]; \n")
            if nodo[1] is None and nodo[2] is not None:
                file.write(str(nodo[0]) + "->"+ str(nodo[2])+";\n")
            elif nodo[1] is not None and nodo[2] is None:
                file.write(str(nodo[0]) + "->" + str(nodo[1])+";\n")
            else:
                file.write(str(nodo[0]) + "->" + str(nodo[1])+";\n")
                file.write(str(nodo[0]) + "->" + str(nodo[2])+";\n")

        file.write("}")
        file.close()
      #  ruta = path.dirname(path.abspath(__file__))
      #  system(ruta)
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-avl.dot -o " + nombre + "-avl.png"
            system(executecmd)
            system("start " + nombre + "-avl.png ")
        except:
            print("Error al abrir la imagen")
nwAVL = AVLTree()
# nwAVL.insert(220170052,"25489652145124","awebasdfo","sqwe",'ghjk@gmail.com',"pass1",225,21)
# nwAVL.insert(201700552,"254892545245124","awasdfebo","asdf XD",'hjkl@gmail.com',"pass545",211,45)
# nwAVL.insert(201700666,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
# nwAVL.insert(201845214,"254897845545124","awefdghbo","erty XD",'cvbn@gmail.com',"pa12045",150,30)
# nwAVL.insert(201500001,"254812542145124","awwertebo","dfgh XD",'wqert@gmail.com',"pa858",155,23)
# nwAVL.insert(201912342,"25489652145124","awebasdfo","sqwe",'ghjk@gmail.com',"pass1",225,21)
# nwAVL.insert(201201245,"254892545245124","awasdfebo","asdf XD",'hjkl@gmail.com',"pass545",211,45)
# nwAVL.insert(201896230,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
# nwAVL.insert(201021545,"254897845545124","awefdghbo","erty XD",'cvbn@gmail.com',"pa12045",150,30)
# nwAVL.insert(201124522,"254812542145124","awwertebo","dfgh XD",'wqert@gmail.com',"pa858",155,23)
nwAVL.insert(1,"25489652145124","awebasdfo","sqwe",'ghjk@gmail.com',"pass1",225,21)
nwAVL.insert(2,"254892545245124","awasdfebo","asdf XD",'hjkl@gmail.com',"pass545",211,45)
nwAVL.insert(3,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
nwAVL.insert(4,"254897845545124","awefdghbo","erty XD",'cvbn@gmail.com',"pa12045",150,30)
nwAVL.insert(5,"254812542145124","awwertebo","dfgh XD",'wqert@gmail.com',"pa858",155,23)
nwAVL.insert(6,"25489652145124","awebasdfo","sqwe",'ghjk@gmail.com',"pass1",225,21)
nwAVL.insert(7,"254892545245124","awasdfebo","asdf XD",'hjkl@gmail.com',"pass545",211,45)
nwAVL.insert(8,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
nwAVL.insert(9,"254897845545124","awefdghbo","erty XD",'cvbn@gmail.com',"pa12045",150,30)
nwAVL.insert(10,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
nwAVL.insert(11,"254897845545124","awefdghbo","erty XD",'cvbn@gmail.com',"pa12045",150,30)
nwAVL.insert(12,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
nwAVL.generarGraph()
nwAVL.delete(8)
nwAVL.generarGraph()
nwAVL.delete(4)
nwAVL.generarGraph()
nwAVL.delete(10)
nwAVL.generarGraph()
nwAVL.insert(8,"258487582145124","aweasdfbo","zxcv XD",'bnm,@gmail.com',"pas4512",245,22)
nwAVL.generarGraph()
# nwAVL.inOrden()
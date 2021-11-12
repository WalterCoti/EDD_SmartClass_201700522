import time
from datetime import datetime
from os import system

#======================================= NODOS ====================================
class NodoDoble:

    def __init__(self, codigo_, nombre_, creditos_, pre_codigo_, obligatorio_):
        self.codigo = codigo_
        self.nombre = nombre_
        self.creditos = creditos_
        self.pre_codigo = pre_codigo_
        self.obligatorio = obligatorio_
        self.sig = None
        self.ant = None

    def getcodigo(self):
        return self.codigo
    def getnombre(self):
        return self.nombre
    def getcreditos(self):
        return self.creditos
    def getPrecodigo(self):
        return self.pre_codigo
    def getobligatorio(self):
        return self.obligatorio
    def getsig(self):
        return self.sig
    def getant(self):
        return self.ant

    def setcodigo(self, valor_):
        self.codigo = valor_
    def setnombre(self, valor_):
        self.nombre = valor_
    def setcreditos(self, valor_):
        self.creditos = valor_
    def setPrecodigo(self, valor_):
        self.pre_codigo = valor_
    def setobligatorio(self, valor_):
        self.obligatorio = valor_
    def setsig(self, valor_):
        self.sig = valor_
    def setant(self, valor_):
        self.ant = valor_

class NodoPuntero:

    def __init__(self, puntero_):
        self.puntero = puntero_
        self.sig = None
        self.ant = None

    def getpuntero(self):
        return self.puntero
    def getsig(self):
        return self.sig
    def getant(self):
        return self.ant

    def setpuntero(self, valor_):
        self.puntero = valor_
    def setsig(self, valor_):
        self.sig = valor_
    def setant(self, valor_):
        self.ant = valor_

#=============================================================Lista pagina ====================
class ListaPuntero:

    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0
    
    def isEmpty(self):
        return self.head == None

    def insertpuntero(self, puntero_):
        newNode = NodoPuntero(puntero_)
        if self.count < 5:
            if self.isEmpty():
                self.head = newNode
                self.last = newNode
            else:
                self.last.setsig(newNode)
                newNode.setant(self.last)
                self.last = newNode
            self.count += 1
    
    def insertpunteroP(self, page_, pos_):
        aux = self.head
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getsig()
        aux.setpuntero(page_)
    
    def getpuntero(self, pos_):
        aux = self.head
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getsig()
        return aux

    def gethead(self):
        return self.head
    
    def sethead(self, head_):
        self.head = head_
    
    def getCount(self):
        return self.count

    def setCount(self, count_):
        self.count = count_

class ListaDoble:

    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def isEmpty(self):
        return self.head is None
    
    def addNodoD(self, codigo_, nombre_, creditos_, pre_codigo_, obligatorio_):
        newNode = NodoDoble(codigo_, nombre_, creditos_, pre_codigo_, obligatorio_)
        if self.count < 4:
            if self.isEmpty():
                self.head = newNode
                self.last = newNode
            else:
                self.last.setsig(newNode)
                newNode.setant(self.last)
                self.last = newNode

            self.count += 1

    def addData(self, codigo_, pos_):
        aux = self.head
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getsig()
        aux.setcodigo(codigo_)
        
    def getData(self, pos_):
        aux = self.head
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getsig()
        return aux
    
    def showData(self):
        aux = self.head
        while aux != None:
            print("Dato",aux.getcodigo())
            aux = aux.getsig()

#====================================== PAGINA B ============================================
class Pagina_B:
    
    def __init__(self):
        self.count = 0
        self.maxClaves = 5
        self.punteros = ListaPuntero()
        self.data = ListaDoble()

        for i in range(5):
            if i != 4:
                self.data.addNodoD("", None, None, None, None)
            self.punteros.insertpuntero(None)

    def fullPage(self):
        return self.count == self.maxClaves - 1

    def preFullPage(self):
        return self.count == self.maxClaves/2

    def getCount(self):
        return self.count

    def setCount(self, count_):
        self.count = count_
    
    def getMaxClaves(self):
        return self.maxClaves
    
    def setMaxClaves(self, maxClaves_):
        self.maxClaves = maxClaves_

    def getcodigo(self, pos_):
        return self.data.getData(pos_).getcodigo()

    def setcodigo(self, pos_, codigo_):
        self.data.addData(codigo_, pos_)
    
    def getnombre(self, pos_):
        return self.data.getData(pos_).getnombre()

    def setnombre(self, pos_, nombre_):
        self.data.getData(pos_).setnombre(nombre_)

    def getcreditos(self, pos_):
        return self.data.getData(pos_).getcreditos()
    
    def setcreditos(self, pos_, creditos_):
        self.data.getData(pos_).setcreditos(creditos_)

    def getPrecodigos(self, pos_):
        return self.data.getData(pos_).getPrecodigo()
    
    def setPrecodigos(self, pos_, pre_codigo_):
        self.data.getData(pos_).setPrecodigo(pre_codigo_)

    def getobligatorio(self, pos_):
        return self.data.getData(pos_).getobligatorio()
    
    def setobligatorio(self, pos_, obligatorio_):
        self.data.getData(pos_).setobligatorio(obligatorio_)
    
    def getpuntero(self, pos_):
        return self.punteros.getpuntero(pos_).getpuntero()

    def setpuntero(self, pos_, puntero_):
        self.punteros.insertpunteroP(puntero_, pos_)

# ==================================== CURSOS =====================================
class ArbolB_Cursos:

    def __init__(self):
        #raiz
        self.raiz = None    #B-Page
        #Data Nodes BTree
        self.codigo = None
        self.nombre = None
        self.creditos = None
        self.pre_codigos = None
        self.obligatorio = None
        #punteros
        self.aux1 = False
        self.aux2 = None  # B-Page
        self.toUp = False
        self.status = False
        self.compare = False
        #To Generate Graphcs
        self.grafica = ""
        self.nodos = 0
        self.grafica2 = ""


    def isEmpty(self, raiz_):
        return (raiz_ == None or raiz_.getCount() == 0)
    
    def addCurso(self, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_):
        self.__addCurso(self.raiz, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_)
    
    def __addCurso(self, raiz_, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_):
        self.insert(raiz_, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_)
        if self.toUp:
            self.raiz = Pagina_B()
            self.raiz.setCount(1)
            self.raiz.setcodigo(0, self.codigo)
            self.raiz.setnombre(0, self.nombre)
            self.raiz.setcreditos(0, self.creditos)
            self.raiz.setPrecodigos(0, self.pre_codigos)
            self.raiz.setobligatorio(0, self.obligatorio)

            self.raiz.setpuntero(0, raiz_)
            self.raiz.setpuntero(1, self.aux2)

    def insert(self, raiz, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_):
        pos = 0
        self.status = False
        
        if self.isEmpty(raiz) and self.compare == False:
            self.toUp = True

            self.codigo = codigo_
            self.nombre = nombre_
            self.creditos = creditos_
            self.pre_codigos = pre_codigos_
            self.obligatorio = obligatorio_

            self.aux2 = None
        
        else:
            pos = self.searchNodo_B(codigo_, raiz)
            if self.compare == False:
                if self.status:
                    self.toUp = False
                else:
                    self.insert(raiz.getpuntero(pos), codigo_, nombre_, creditos_, pre_codigos_, obligatorio_)

                    if self.toUp:
                        if raiz.getCount() < 4:
                            self.toUp = False
                            self.insert_hoja(raiz, pos, self.codigo, self.nombre, self.creditos, self.pre_codigos, self.obligatorio)
                        else:
                            self.toUp = True
                            self.divideBPage(raiz, pos, self.codigo, self.nombre, self.creditos, self.pre_codigos, self.obligatorio)
            else:
                print("Curso Repetido", codigo_)
                self.compare = False
            
    def searchNodo_B(self, codigo_, raiz_):
        auxCount = 0
        if codigo_ < raiz_.getcodigo(0):
            self.status = False
            auxCount = 0
        else:
            while auxCount != raiz_.getCount():
                if codigo_ == raiz_.getcodigo(auxCount):
                    self.compare = True
                auxCount += 1
            
            auxCount = raiz_.getCount()

            while codigo_ < raiz_.getcodigo(auxCount-1) and auxCount > 1:
                auxCount -= 1
                self.status = True if (codigo_ == raiz_.getcodigo(auxCount-1)) else False

        return auxCount

    def insert_hoja(self, raiz_, pos_, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_):
        auxC = raiz_.getCount()
        while auxC != pos_:
            if auxC != 0:
                raiz_.setcodigo(auxC, raiz_.getcodigo(auxC-1))
                raiz_.setnombre(auxC, raiz_.getnombre(auxC-1))
                raiz_.setcreditos(auxC, raiz_.getcreditos(auxC-1))
                raiz_.setPrecodigos(auxC, raiz_.getPrecodigos(auxC-1))
                raiz_.setobligatorio(auxC, raiz_.getobligatorio(auxC-1))
                raiz_.setpuntero(auxC+1, raiz_.getpuntero(auxC))
            auxC -= 1
        
        raiz_.setcodigo(pos_, codigo_)
        raiz_.setnombre(pos_, nombre_)
        raiz_.setcreditos(pos_, creditos_)
        raiz_.setPrecodigos(pos_, pre_codigos_)
        raiz_.setobligatorio(pos_, obligatorio_)
        raiz_.setpuntero(pos_+1, self.aux2)
        raiz_.setCount(raiz_.getCount()+1)

    def divideBPage(self, raiz_, pos_, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_):
        pos2 = 0
        posMed = 0
        if pos_ <= 2:
            posMed = 2
        else:
            posMed = 3
        
        pagina_der = Pagina_B()
        pos2 = posMed + 1

        while pos2 != 5:
            if (pos2 - posMed) != 0:
                pagina_der.setcodigo((pos2-posMed)-1, raiz_.getcodigo(pos2-1))
                pagina_der.setnombre((pos2-posMed)-1, raiz_.getnombre(pos2-1))
                pagina_der.setcreditos((pos2-posMed)-1, raiz_.getcreditos(pos2-1))
                pagina_der.setPrecodigos((pos2-posMed)-1, raiz_.getPrecodigos(pos2-1))
                pagina_der.setobligatorio((pos2-posMed)-1, raiz_.getobligatorio(pos2-1))
                pagina_der.setpuntero(pos2-posMed, raiz_.getpuntero(pos2))
            
            pos2 += 1

        pagina_der.setCount(4-posMed)
        raiz_.setCount(posMed)

        if pos_<= 2:
            self.aux1 = True
            self.insert_hoja(raiz_, pos_, codigo_, nombre_, creditos_, pre_codigos_, obligatorio_)
        else:
            self.aux1 = True
            self.insert_hoja(pagina_der, (pos_-posMed), codigo_, nombre_, creditos_, pre_codigos_, obligatorio_)
        
        self.codigo = raiz_.getcodigo(raiz_.getCount()-1)
        self.nombre = raiz_.getnombre(raiz_.getCount()-1)
        self.creditos = raiz_.getcreditos(raiz_.getCount()-1)
        self.pre_codigos = raiz_.getPrecodigos(raiz_.getCount()-1)
        self.obligatorio = raiz_.getobligatorio(raiz_.getCount()-1)

        pagina_der.setpuntero(0, raiz_.getpuntero(raiz_.getCount()))

        raiz_.setCount(raiz_.getCount() - 1)
        self.aux2 = pagina_der

        if self.aux1:
            raiz_.setcodigo(3, "")
            raiz_.setnombre(3,"")
            raiz_.setcreditos(3,"")
            raiz_.setPrecodigos(3,"")
            raiz_.setobligatorio(3,"")
            raiz_.setpuntero(4, None)

            raiz_.setcodigo(2, "")
            raiz_.setnombre(2,"")
            raiz_.setcreditos(2,"")
            raiz_.setPrecodigos(2,"")
            raiz_.setobligatorio(2,"")
            raiz_.setpuntero(3, None)
    
    def graficar(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.graph_dot(nameFile)
    
    def graph_dot(self, nombre):
        file = open(nombre + "-treeB.dot", "w")
        file.write("digraph treeB {\n")
        file.write("\t nodesep=.05;\n")
        file.write("\tnode [shape=record,width=.1,height=.1, style=\"rounded,filled\"  fillcolor = crimson , color=black, fontcolor=white];\n")
        self.graph_nodes(self.raiz)
        self.graph_edges(self.raiz)
        file.write(self.grafica)
        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-treeB.dot -o " + nombre + "-treeB.png"
            system(executecmd)
            system("start " + nombre + "-treeB.png ")
        except:
            print("Error al abrir la imagen")
    
    def graph_nodes(self,pagina_):
        contador = 0
        if pagina_ is not None:
            self.nodos = 0
            for i in range(pagina_.getCount()):
                if pagina_.getcodigo(i) is not None:
                    if pagina_.getcodigo(i) != "":
                        self.nodos += 1
                        if i != 0:
                            self.grafica = self.grafica + "|"
                        if self.nodos == 1:
                            self.grafica = self.grafica + "\nNodo" + str(pagina_.getcodigo(i)) + "[label=\"<f0> |"
                        if i == 0:
                            self.grafica += "<f"+str(i+1)+">" + str(pagina_.getcodigo(i)) +"\\n"+pagina_.getnombre(i) + "|<f"+str(i+2)+"> "
                            contador=3
                        else: 
                            self.grafica = self.grafica + "<f"+str(contador) + ">" + str(pagina_.getcodigo(i)) +"\\n"+pagina_.getnombre(i) + "|<f"+str(contador+1)+"> "
                            contador+=2
                        if i == (pagina_.getCount()-1):
                            contador=0
                            self.grafica = self.grafica + " \",group=0];\n"


            self.graph_nodes(pagina_.getpuntero(0))
            self.graph_nodes(pagina_.getpuntero(1))
            self.graph_nodes(pagina_.getpuntero(2))
            self.graph_nodes(pagina_.getpuntero(3))
            self.graph_nodes(pagina_.getpuntero(4))

    def graph_edges(self, pagina_):
        if pagina_ is not None:
            if  pagina_.getcodigo(0) is not None:
                if pagina_.getcodigo(0) != "":
                    if pagina_.getpuntero(0)!=None and pagina_.getpuntero(0).getcodigo(0)!=None:
                        self.grafica = self.grafica + "\nNodo"+str(pagina_.getcodigo(0))+":f0->"+"Nodo"+str(pagina_.getpuntero(0).getcodigo(0))
                        
                    if pagina_.getpuntero(1)!=None and pagina_.getpuntero(1).getcodigo(0)!=None:
                        self.grafica = self.grafica + "\nNodo"+ str(pagina_.getcodigo(0)) + ":f2->"+"Nodo"+ str(pagina_.getpuntero(1).getcodigo(0))
                        
                    if pagina_.getpuntero(2)!=None and pagina_.getpuntero(2).getcodigo(0)!=None:
                        self.grafica = self.grafica +"\nNodo"+ str(pagina_.getcodigo(0)) + ":f4->"+"Nodo"+ str(pagina_.getpuntero(2).getcodigo(0))
                
                    if pagina_.getpuntero(3)!=None and pagina_.getpuntero(3).getcodigo(0)!=None:
                        self.grafica = self.grafica +"\nNodo"+ str(pagina_.getcodigo(0)) + ":f6->"+"Nodo"+ str(pagina_.getpuntero(3).getcodigo(0))
                        
                    if pagina_.getpuntero(4)!=None and pagina_.getpuntero(4).getcodigo(0)!=None:
                        self.grafica = self.grafica +"\nNodo"+ str(pagina_.getcodigo(0)) + ":f8->"+"Nodo"+ str(pagina_.getpuntero(4).getcodigo(0))
            self.graph_edges(pagina_.getpuntero(0))
            self.graph_edges(pagina_.getpuntero(1))
            self.graph_edges(pagina_.getpuntero(2))
            self.graph_edges(pagina_.getpuntero(3))
            self.graph_edges(pagina_.getpuntero(4))

nwtreeb = ArbolB_Cursos()
nwtreeb.addCurso(725,"curso 1",5,"15,12,13",True)
nwtreeb.addCurso(2025,"curso 2",4,"12,13",False)
nwtreeb.addCurso(25,"curso 3",2,"1,2,3",True)
nwtreeb.addCurso(15,"curso 4",1,"8,9,2",False)
nwtreeb.addCurso(33,"curso 5",9,"3,2,1",True)
nwtreeb.addCurso(255,"curso 6",5,"7,8,9,20",True)
nwtreeb.addCurso(72,"curso 7",5,"15,12,13",True)
nwtreeb.addCurso(2020,"curso 8",4,"12,13",False)
nwtreeb.addCurso(5,"curso 9",2,"1,2,3",True)
nwtreeb.addCurso(16,"curso 10",1,"8,9,2",False)
nwtreeb.addCurso(45,"curso 11",9,"3,2,1",True)
nwtreeb.addCurso(222,"curso 12",5,"7,8,9,20",True)
# nwtreeb.graficar()
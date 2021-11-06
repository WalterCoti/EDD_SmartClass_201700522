import time
from datetime import datetime
from os import system

# import sys
# sys.path.append('D:\\Segundo_Semestre\\EDD\\Lab\\Fase3\\backend\\venv\\src\\Estructuras\\')
# from Listas.List_Cursos import Lista_cursos

class NodoAdy: 
    def __init__(self,codigo_):
        self.codigo = codigo_
        self.sig  = None
        self.ant = None

class Nodograph:
    def __init__(self, codigo_,nombre_,creditos_,list_):
        self.codigo = codigo_
        self.nombre = nombre_
        self.creditos = creditos_
        self.list = list_
        self.sig = None
        self.ant = None

class Lista:
    def __init__(self):
        self.head = None
        self.cola = None
        self.tam = 0

    def isempty(self):
        return self.head is None

    def existe(self,codigo):
        tmp = self.head
        while tmp:
            if tmp.codigo == codigo:
                return True
            tmp = tmp.sig
        return False

    def get_list(self):
        aux = self.head
        res_lst = []
        while aux is not None:
            res_lst.append(aux.codigo)
            aus = aux.sig
        return res_lst

    def addnodoad(self,codigo_):
        nwNodo = NodoAdy(codigo_)
        if self.isempty():
            self.head = nwNodo
            self.cola = nwNodo
        else:
            if self.existe(codigo_):
                pass
            else:
                self.cola.sig = nwNodo
                nwNodo.ant = self.cola
                self.cola = nwNodo
        self.tam += 1
        

class grafo:
    def __init__(self):
        self.head = None
        self.cola = None
        self.tam = None
    
    def isempty(self):
        return self.head is None

    def exist(self,codigo_):
        tmp = self.head
        while tmp:
            if tmp.codigo == codigo_:
                return True
            tmp = tmp.sig
        return False

    def dameprereq(self,codigo_,lista_):
        tmp = lista_.head
        while tmp is not None:
            if tmp.codigo == codigo_:
                codigos = tmp.pre_codigo.split(',')
                return codigos
            tmp = tmp.sig
        return None

    def damenodo(self,codigo_,lista_):
        tmp = lista_.head
        while tmp is not None:
            if tmp.codigo == codigo_:
                return tmp
            tmp = tmp.sig
        return None
    
    def addnodo(self,nwNodo_):
        if not self.exist(nwNodo_.codigo):      
            if self.isempty():
                self.head = nwNodo_
                self.cola = nwNodo_
            else:
                self.cola.sig = nwNodo_
                nwNodo_.ant = self.cola
                self.cola = nwNodo_
    
    def get_list(self):
        tmp = self.head
        count = 0
        adyacent_list = ""
        while tmp:
            if not tmp.list.isempty():
                tmp2 = tmp.list.head
                while tmp2:
                    adyacent_list += '->' + str(tmp2.codigo)
                    tmp2 = tmp2.sig
            print(str(count) + ") "+ str(tmp.codigo) + " : " + adyacent_list)
            adyacent_list = ""
            count += 1
            tmp = tmp.sig 

    def linkgraph(self,valor1,valor2):
        tmp = self.head
        while tmp:
            if tmp.codigo == valor1:
                tmp.list.addnodoad(valor2)
                break
            tmp = tmp.sig

    def getgrafo(self,codigo_,listacursos_):
        tmp  = listacursos_.getlist()
        while tmp is not None:
            if tmp.codigo == codigo_:
                lstcursos = Lista()
                nodoCu = Nodograph(tmp.codigo,tmp.nombre,tmp.creditos,lstcursos)
                self.addnodo(nodoCu)
                lstpre = tmp.pre_codigo.split(',')
                for cod in lstpre:
                    if cod == "":
                        pass
                    else:
                        self.getgrafo(str(cod),listacursos_)
                        self.linkgraph(str(cod),nodoCu.codigo)
                        
                break
            tmp = tmp.sig

    def getgrafopensum(self,listacursos_):
            tmp  = listacursos_.getlist()
            while tmp is not None:
                lstcursos = Lista()
                nodoCu = Nodograph(tmp.codigo,tmp.nombre,tmp.creditos,lstcursos)
                self.addnodo(nodoCu)
                lstpre = tmp.pre_codigo.split(',')
                for cod in lstpre:
                    if cod == "":
                        pass
                    else:
                        self.getgrafo(str(cod),listacursos_)
                        self.linkgraph(str(cod),nodoCu.codigo)
                tmp = tmp.sig


    def graficarGrafo(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.graph_dot(nameFile)

        # generar archivo.dota

    def graph_dot(self, nombre):
        file = open(nombre + "-grafo.dot", "w")
        file.write("digraph grafo {\n")
        file.write("\t\trankdir=LR;")
        file.write("\tnode [shape = record, style=rounded];\n")
        #file.write("\tnode [shape=record,width=.1,height=.1, style=\"rounded,filled\"  fillcolor = firebrick3 , color=black, fontcolor=white];\n")
        # Graficar grafo
        tmp = self.head
        while tmp:
            file.write(str(tmp.codigo) +"[label=\"" + str(tmp.codigo) +" \\n" + tmp.nombre + "\"]; \n")
            aux = tmp.list.head
            while aux:
                file.write(str(tmp.codigo) +" -> " + str(aux.codigo) + "[label=\"" + str(tmp.creditos) + "\"]; \n")
                aux = aux.sig
            tmp = tmp.sig
        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-grafo.dot -o " + nombre + "-grafo.png"
            system(executecmd)
            system("start " + nombre + "-grafo.png ")
        except:
            print("Error al abrir la imagen")

# #codigo_, nombre_, creditos_, pre_codigo_, obligatorio_):
# nwList = Lista_cursos()
# nwList.addCurso(1,"Prueba1",3,"12,3",True)
# nwList.addCurso(2,"Prueba2",2,"10",False)
# nwList.addCurso(3,"Prueba3",7,"",True)
# nwList.addCurso(4,"Prueba6",5,"",True)
# nwList.addCurso(5,"Prueba4",9,"",False)
# nwList.addCurso(6,"Prueba5",9,"5,3",False)
# nwList.addCurso(7,"Prueba1",3,"",True)
# nwList.addCurso(8,"Prueba2",2,"5,7,9",False)
# nwList.addCurso(9,"Prueba3",7,"4",True)
# nwList.addCurso(10,"Prueba6",5,"8",True)
# nwList.addCurso(11,"Prueba4",9,"5",False)
# nwList.addCurso(12,"Prueba5",9,"4",False)

    
# nwgrf = grafo()
# nwgrf.getgrafo(2,nwList)
# nwgrf.get_list()
# nwgrf.graficarGrafo()
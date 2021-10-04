import time
from datetime import datetime
from os import system
from Estructuras.ListTask import List_Task
from Estructuras.NodoTask import NodoTask

class nodo:
    def __init__(self, valor_=0, posx_=0, posy_=0):
        self.valor = valor_
        self.lstTareas = None
        self.pos_x = posx_
        self.pos_y = posy_
        self.N_der = None
        self.N_izq = None
        self.N_arriba = None
        self.N_abajo = None
        self.sig = None
        self.ant= None


class lista:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_cabecera(self, valor):
        nw_nodo = nodo(valor)
        if self.head is None or self.head.valor > nw_nodo.valor:
            nw_nodo.sig = self.head
            self.head = nw_nodo
        else:
            tmp = self.head
            while tmp.sig is not None and tmp.sig.valor < nw_nodo.valor:
                tmp = tmp.sig
            nw_nodo.sig = tmp.sig
            tmp.sig = nw_nodo
        self.size += 1

    def search(self, valor):
        tmp = self.head
        while tmp is not None:
            if tmp.valor == valor:
                return tmp
            tmp = tmp.sig
        return None

    def print(self):
        tmp = self.head
        while tmp is not None:
            print("Cabecera:", tmp.valor)
            tmp = tmp.sig

    def exist(self,valor):
        if  self.search(valor) is None:
            print("no existe: " + str(valor))
        else:
            print("existe: " + str(valor))

class matriz:
    def __init__(self):
        self.lstDias = lista()
        self.lstHoras = lista()

    def existeNod(self,posx_,posy_):        #Get info nodo
        tmp = self.lstDias.head
        while tmp is not None:
            if tmp.valor == posx_:
                auxH = tmp.N_abajo
                while auxH is not None:
                    if auxH.pos_y == posy_ and auxH.pos_x == posx_:
                        return auxH
                    auxH = auxH.N_abajo
            tmp = tmp.sig
        return None

    def addlistTask(self):
        nwListTask = List_Task()
        return nwListTask

    def insert_Task(self,nodoT,pos_x,pos_y):
        nodo = self.existeNod(pos_x,pos_y)
        if nodo:
            nodo.lstTareas.addTask(nodoT)
        else:
            self.insert_Nodo(nodoT, pos_x, pos_y)

    def insert_Nodo(self, nodoTask_, pos_x, pos_y):
        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        if M_dia is None and M_hora is None:
            self.Caso1(nodoTask_, pos_x, pos_y)
        elif M_dia is None and M_hora is not None:
            self.Caso2(nodoTask_, pos_x, pos_y)
        elif M_dia is not None and M_hora is None:
            self.Caso3(nodoTask_, pos_x, pos_y)
        else:
            self.Caso4(nodoTask_, pos_x, pos_y)

    def Caso1(self, nTask_, pos_x, pos_y):
        self.lstDias.add_cabecera(pos_x)
        self.lstHoras.add_cabecera(pos_y)

        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        nuevo = nodo(0, pos_x, pos_y)
        if nuevo.lstTareas is None:
            nuevo.lstTareas = self.addlistTask()
            nuevo.lstTareas.addTask(nTask_)
        M_dia.N_abajo = nuevo
        nuevo.N_arriba = M_dia

        M_hora.N_der = nuevo
        nuevo.N_izq = M_hora

    def Caso2(self, nTask_, pos_x, pos_y):
        self.lstDias.add_cabecera(pos_x)

        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        agregado = False

        nuevo = nodo(0, pos_x, pos_y)
        if nuevo.lstTareas is None:
            nuevo.lstTareas = self.addlistTask()
            nuevo.lstTareas.addTask(nTask_)
        aux = M_hora.N_der
        cabecera = 0

        while aux is not None:
            cabecera = aux.pos_x
            if cabecera < pos_x:
                aux = aux.N_der
            else:
                nuevo.N_der = aux
                nuevo.N_izq = aux.N_izq
                aux.N_izq.N_der = nuevo
                aux.N_izq = nuevo
                agregado = True
                break
        if agregado == False:
            aux = M_hora.N_der
            while (aux.N_der != None):
                aux = aux.N_der
            nuevo.N_izq = aux
            aux.N_der = nuevo

        M_dia.N_abajo = nuevo
        nuevo.N_arriba = M_dia

    def Caso3(self, nTask_, pos_x, pos_y):
        self.lstHoras.add_cabecera(pos_y)

        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        agregado = False

        nuevo = nodo(0, pos_x, pos_y)
        if nuevo.lstTareas is None:
            nuevo.lstTareas = self.addlistTask()
            nuevo.lstTareas.addTask(nTask_)
        aux = M_dia.N_abajo
        cabecera = 0

        while aux is not None:
            cabecera = aux.pos_y
            if cabecera < pos_y:
                aux = aux.N_abajo
            else:
                nuevo.N_abajo = aux
                nuevo.N_arriba = aux.N_arriba
                aux.N_arriba.N_abajo = nuevo
                aux.N_arriba = nuevo
                agregado = True
                break
        if agregado is False:
            aux = M_dia.N_abajo
            while aux.N_abajo is not None:
                aux = aux.N_abajo
            nuevo.N_arriba = aux
            aux.N_abajo = nuevo

        M_hora.N_der = nuevo
        nuevo.N_izq = M_hora

    def Caso4(self, nTask_, pos_x, pos_y):
        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        nuevo = nodo(0, pos_x, pos_y)
        if nuevo.lstTareas is None:
            nuevo.lstTareas = self.addlistTask()
            nuevo.lstTareas.addTask(nTask_)

        agregado = False
        aux = M_dia.N_abajo

        while aux is not None:
            cabecera = aux.pos_y
            if cabecera < pos_y:
                aux = aux.N_abajo
            else:
                nuevo.N_abajo = aux
                nuevo.N_arriba = aux.N_arriba
                aux.N_arriba.N_abajo = nuevo
                aux.N_arriba = nuevo
                agregado = True
                break
        if agregado == False:
            aux = M_dia.N_abajo
            while aux.N_abajo is not None:
                aux = aux.N_abajo
            nuevo.N_arriba = aux
            aux.N_abajo = nuevo
        agregado = False
        aux = M_hora.N_der
        cabecera = 0

        while aux is not None:
            cabecera = aux.pos_x
            if cabecera < pos_x:
                aux = aux.N_der
            else:
                nuevo.N_der = aux
                nuevo.N_izq = aux.N_izq
                aux.N_izq.N_der = nuevo
                aux.N_izq = nuevo
                agregado = True
                break
        if agregado == False:
            aux = M_hora.N_der
            while aux.N_der is not None:
                aux = aux.N_der
            nuevo.N_izq = aux
            aux.N_der = nuevo

    def recorr_H(self,nodoCabecera_):
        rankHoras = "{rank = same;" + str(hash(nodoCabecera_)) + "; "
        tmp = nodoCabecera_.N_der
        while tmp is not None:
            rankHoras = rankHoras + str(hash(tmp)) + " ; "
            tmp = tmp.N_der
        rankHoras = rankHoras + "}\n"
        return rankHoras

    def rank_cabecera(self):
        rankDias = "{rank = same; HEAD "
        tmp = self.lstDias.head
        while tmp is not None:
            rankDias = rankDias + str(hash(tmp)) + " ; "
            tmp = tmp.sig
        rankDias = rankDias + "}\n"
        return rankDias

    def graficarMatriz(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.graph_Mat(nameFile)

        # generar archivo.dota

    def graph_Mat(self, nombre):
        listNod = []
        file = open(nombre + "-matrix.dot", "w")
        file.write("digraph Matrix {\n")
        file.write("\tnode [style=\"rounded,filled\" shape=rectangle fillcolor = chartreuse2 , color=white];\n")
        file.write("\tHEAD[ label = \"H\\\\D\",  fillcolor = firebrick1, group = 0 color=red];\n")
        # Graficar cabeceras Columna Horas
        tmpH = self.lstHoras.head
        while tmpH is not None:
            file.write("\t" + str(hash(tmpH)) + "[label = \"" + str(tmpH.valor) + "\" , fillcolor = orange, group = 0 ];\n")
            if tmpH.sig is not None:
                file.write("\t" + str(hash(tmpH)) + " -> " + str(hash(tmpH.sig)) + "\n")
            # if tmpH.N_der is not None:
            file.write("\t" + str(hash(tmpH)) + " -> " + str(hash(tmpH.N_der)) + "\n")
            file.write("\t" + self.recorr_H(tmpH))
            tmpH = tmpH.sig
        file.write("\t" + self.rank_cabecera())                   #Mantiene la cabecera en la misma linea
        # Graficar cabeceras Fila Dias
        tmpD = self.lstDias.head
        while tmpD is not None:
            file.write("\t" + str(hash(tmpD)) + "[label = \"" + str(tmpD.valor) + "\" , fillcolor = orange, group =" + str(tmpD.valor) + " ];\n")
            auxD = tmpD.N_abajo
            #recorren cada columna y graficar punteros a nodos
            while auxD is not None:
                file.write("\t" + str(hash(auxD)) + "[label = \"" + str(auxD.lstTareas.size) + "\" , group = " + str(tmpD.valor) + " ];\n")
                if auxD.N_der is not None:
                    file.write("\t" + str(hash(auxD)) + " -> " + str(hash(auxD.N_der)) + "\n")
                if auxD.N_izq is not None:
                # if auxD.N_izq is not None and auxD.N_izq.pos_x != 0 and None and auxD.N_izq.pos_y != 0:
                    file.write("\t" + str(hash(auxD)) + " -> " + str(hash(auxD.N_izq)) + "\n")
                if auxD.N_abajo is not None:
                    file.write("\t" + str(hash(auxD)) + " -> " + str(hash(auxD.N_abajo)) + "\n")
                if auxD.N_arriba is not None:
                # if auxD.N_arriba is not None and auxD.N_arriba.pos_x != 0 and None and auxD.N_arriba.pos_y != 0:
                    file.write("\t" + str(hash(auxD)) + " -> " + str(hash(auxD.N_arriba)) + "\n")
                auxD = auxD.N_abajo

            if tmpD.sig is not None:
                file.write("\t" + str(hash(tmpD)) + " -> " + str(hash(tmpD.sig)) + "\n")
            # if tmpD.N_abajo is not None:
            file.write("\t" + str(hash(tmpD)) + " -> " + str(hash(tmpD.N_abajo)) + "\n")
            tmpD = tmpD.sig
        file.write("\t HEAD -> " + str(hash(self.lstDias.head))+ "\n")
        file.write("\t HEAD -> " + str(hash(self.lstHoras.head)))
        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-matrix.dot -o " + nombre + "-matrix.png"
            system(executecmd)
            system("start " + nombre + "-matrix.png ")
        except:
            print("Error al abrir la imagen")



# matriz = matriz()
# #
# nNodo = NodoTask(1,"Prueba1","prueba descripcion 1","Materia 1","12/5/2021","8:00","Finalizado")
# nNodo1 = NodoTask(2,"Prueba2","prueba descripcion 2","Materia 2","12/5/2021","8:00","Finalizado")
# nNodo2 = NodoTask(3,"Prueba3","prueba descripcion 3","Materia 3","12/5/2021","8:00","Finalizado")
# nNodo3 = NodoTask(4,"Prueba4","prueba descripcion 4","Materia 4","12/5/2021","8:00","Finalizado")
# nNodo4 = NodoTask(5,"Prueba5","prueba descripcion 5","Materia 5","12/5/2021","8:00","Finalizado")
# nNodo5 = NodoTask(6,"Prueba6","prueba descripcion 6","Materia 6","12/5/2021","8:00","Finalizado")
# matriz.insert_Task(nNodo,1,1)
# matriz.insert_Task(nNodo1,2, 2)
# matriz.insert_Task(nNodo2,2, 2)
# matriz.insert_Task(nNodo2,3, 3)
# matriz.insert_Task(nNodo3,4, 4)
# matriz.insert_Task(nNodo4,5, 5)
# matriz.insert_Task(nNodo,3, 2)
# matriz.insert_Task(nNodo1,3, 2)
# matriz.insert_Task(nNodo2,3, 2)
# matriz.insert_Task(nNodo3,3, 2)
# matriz.graficarMatriz()
# list = matriz.existeNod(3,2)
# list.lstTareas.graficar()
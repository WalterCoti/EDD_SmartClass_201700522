from Estructuras.NodoTask import NodoTask
from os import system
import time
from datetime import datetime

class List_Task:
    def __init__(self):
        self.head = None
        self.size = 0

    def addTask(self,nodo_Task_):
        if self.head is None:
            nodo_Task_.sig = self.head
            self.head = nodo_Task_
        else:
            tmp = self.head
            while tmp.sig is not None:
                tmp = tmp.sig
            nodo_Task_.sig = tmp.sig
            tmp.sig = nodo_Task_
        self.size += 1

    def deleteTask(self,position):
        tmpPos = 0
        current = self.head
        ante = None
        if position < self.size:
            while current:
                if current.sig is None and tmpPos == position:
                    self.head = None
                    self.size = 0
                elif tmpPos == position:
                    ante.sig = current.sig
                    self.size -= 1
                    return
                tmpPos += 1
                ante = current
                current = current.sig
        else:
            print("La posicion \"" + str(position) + "\" es nula no se puede eliminar")

    def updateTask(self, nwData,position):
        current = self.head
        tmpPos = 0
        ante = None
        if position < self.size:
            while current:
                if tmpPos == position:
                    nwData.sig = current.sig
                    ante.sig = nwData
                    return
                tmpPos += 1
                ante = current
                current = current.sig
        else:
            print("La posicion \"" + str(position) + "\" es nula no puede editarse")

    def getinfo(self,position_):
        current = self.head
        tmpPos = 0
        if position_ < self.size:
            while current:
                if tmpPos == position_:
                    return current
                tmpPos += 1
                ante = current
                current = current.sig
        else:
           return None

    def graficar(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.creardot(nameFile)

    def creardot(self,nombre):
        file = open(nombre + "-Task.dot", "w")
        file.write("digraph d {\n")
        file.write("rankdir = LR\n")
        file.write("\t node [style=\"rounded,filled\" shape=rectangle fillcolor = darkgray , color=white];\n")
        tmp = self.head
        while tmp is not None:
            file.write("\t" + str(hash(tmp)) +"[label=\"Carne: " + str(tmp.carnet) +" \\n Nombre: " + tmp.name_task +" \\n Descripcion: " + tmp.desc_task +" \\n Materia: " + tmp.materia +" \\n Fecha: " + tmp.fecha +"\\n Hora: " + str(tmp.hora) +"\\n Estado: " + tmp.estado + "\"]; \n")
            if tmp.sig is not None:
                file.write("\t" + str(hash(tmp)) + " -> " + str(hash(tmp.sig)))
            tmp = tmp.sig
        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-Task.dot -o " + nombre + "-Task.png"
            system(executecmd)
            system("start " + nombre + "-Task.png ")
        except:
            print("Error al abrir la imagen")

    def printList(self):
        tmp = self.head
        while tmp:
            print("Nodo: " + str(tmp.carnet))
            tmp = tmp.sig
# #
# nNodo = NodoTask(1345,"Prueba1","prueba descripcion 1","Materia 1","12/5/2021","8:00","Finalizado")
# nNodo1 = NodoTask(2345,"Prueba2","prueba descripcion 2","Materia 2","12/5/2021","8:00","Finalizado")
# nNodo2 = NodoTask(4567,"Prueba3","prueba descripcion 3","Materia 3","12/5/2021","8:00","Finalizado")
# nNodo3 = NodoTask(6789,"Prueba4","prueba descripcion 4","Materia 4","12/5/2021","8:00","Finalizado")
# nNodo4 = NodoTask(4568,"Prueba5","prueba descripcion 5","Materia 5","12/5/2021","8:00","Finalizado")
# nNodo5 = NodoTask(24845,"Prueba6","prueba descripcion 6","Materia 6","12/5/2021","8:00","Finalizado")
#
# nwList = List_Task()
# nwList.addTask(nNodo)
# nwList.addTask(nNodo1)
# nwList.addTask(nNodo2)
# nwList.addTask(nNodo3)
# nwList.addTask(nNodo4)
# nwList.addTask(nNodo5)
# nwList.printList()
# nwList.deleteTask(3)
# print("-----------------------------DELETE------------------------------")
# nwList.printList()
# nwList.updateTask(nNodo3,6)
# print("-----------------------------UPDATE------------------------------")
# nwList.printList()
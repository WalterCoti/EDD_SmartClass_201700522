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

    def deleteTask(self):
        pass

    def updateTask(self):
        pass

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
        while tmp is not None:
            print("Nodo: " + str(tmp.carnet))
            tmp = tmp.sig
#
# nNodo = NodoTask(1345,"Prueba1","prueba descripcion 1","Materia 1","12/5/2021","8:00","Finalizado")
# nNodo1 = NodoTask(2345,"Prueba2","prueba descripcion 2","Materia 2","12/5/2021","8:00","Finalizado")
# nNodo2 = NodoTask(4567,"Prueba3","prueba descripcion 3","Materia 3","12/5/2021","8:00","Finalizado")
# nNodo3 = NodoTask(6789,"Prueba4","prueba descripcion 4","Materia 4","12/5/2021","8:00","Finalizado")
# nNodo4 = NodoTask(4568,"Prueba5","prueba descripcion 5","Materia 5","12/5/2021","8:00","Finalizado")
# nNodo5 = NodoTask(24845,"Prueba6","prueba descripcion 6","Materia 6","12/5/2021","8:00","Finalizado")
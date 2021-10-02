import time
from os import system
from datetime import datetime
from Estructuras.NodoTask import NodoTask
from Estructuras.matrisDispersa import matriz

class NodoMes:
    def __init__(self,mes_):
        self.mes = mes_
        self.tareas = None
        self.sig = None
        self.ant = None

class ListMes:
    def __init__(self):
        self.size = 0
        self.head = None

    def getMes(self,mes_):
        tmp = self.head
        while tmp is not None:
            if tmp.mes == mes_:
                return tmp
            tmp = tmp.sig
        return None

    def existemes(self,mes_):
        tmp = self.head
        while tmp is not None:
            if tmp.mes == mes_:
                return True
            tmp = tmp.sig
        return False

    def add_task_mes(self, nodoTask, posx, posy,mes_):
        tmpN = self.getMes(mes_)
        if tmpN is not None:
            tmpN.tareas.inset_Task(nodoTask)
        else:
            self.addmes(mes_, nodoTask, posx, posy)

    def addmes(self, mes_, nodoTask, posx, posy):
        nwNodo = NodoMes(mes_)
        nwMatriz = matriz()
        nwNodo.tareas = nwMatriz
        nwNodo.tareas.insert_Task( nodoTask, posx, posy)
        if self.head is None:
            self.head = nwNodo
        elif self.existemes(mes_):
            print("el mes "+ str(mes_) +" ya se encuentra registrado")
            self.size -= 1
        else:
            tmp = self.head
            while tmp.sig is not None and tmp.sig.mes < mes_:
                tmp = tmp.sig
            if tmp is self.head:
                if tmp.mes > mes_:
                    nwNodo.sig = self.head
                    self.head.ant = nwNodo
                    self.head = nwNodo
                else:
                    nwNodo.sig = tmp.sig
                    nwNodo.ant = tmp
                    tmp.sig.ant = nwNodo
                    tmp.sig = nwNodo
            elif tmp.sig is None:
                tmp.sig = nwNodo
                nwNodo.ant = tmp
            else:
                nwNodo.sig = tmp.sig
                nwNodo.ant = tmp
                tmp.sig.ant = nwNodo
                tmp.sig = nwNodo


        print(str(self.head.mes))
        self.size += 1


    def deletemes(self,mes_):
        pass

    def updatemes(self,mes_):
        pass

    def imprimir(self):
        tmp = self.head
        if self.head is None:
            print("lista vacia")
        else:
            while tmp is not None:
                # print(str(tmp.mes) + " -> " + str(tmp.sig.mes))
                if tmp.ant is not None:
                    print(str(tmp.mes) + " -> " + str(tmp.ant.mes))
                tmp = tmp.sig
        list.append(str(tmp.mes) + " ->  null")
        print(str(self.head.mes))

# nNodo = NodoTask(1345,"Prueba1","prueba descripcion 1","Materia 1","12/5/2021","8:00","Finalizado")
#
# listmn = ListMes()
# listmn.add_task_mes(nNodo,3,5,4)
print("hola mundo")
# nNodo2 = NodoTask(13446,"Prueba3","prueba descripcion 1","Materia 1","12/5/2021","8:00","Finalizado")

# listmn.addmes(4)
# listmn.addmes(6)
# listmn.addmes(8)
# listmn.addmes(3)
# listmn.addmes(5)
# listmn.addmes(12)
# listmn.addmes(7)
# listmn.addmes(9)
# listmn.addmes(1)
# listmn.addmes(2)
# listmn.imprimir()

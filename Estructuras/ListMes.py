import time
from os import system
from datetime import datetime

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

    def existemes(self,mes_):
        tmp = self.head
        while tmp is not None:
            if tmp.mes == mes_:
                return True
            tmp = tmp.sig
        return False

    def addmes(self,mes_):
        nwNodo = NodoMes(mes_)
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

    def graficar(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.graphAVL(nameFile)

    def graphmes(self,nombre):
        file = open(nombre + "-lstMes.dot", "w")
        file.write("digraph d {\n")
        file.write("\tnode [shape = record, style=rounded];\n")
        tmp = self.head
        # while tmp.sig is not None:

            # file.write(str(tmp.mes) + "[label=\" Mes:" + str(nodo[3]) + " \\n " + str(nodo[4]) + " \\n " + str(nodo[5]) + "\"]; \n")
            #
            #     file.write(str(tmp.carnet) + "->" + str(tmp.sig.carnet) + ";\n")
            #     file.write(str(tmp.carnet) + "->" + str(tmp.ant.carnet) + ";\n")

        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + nombre + "-lstMes.dot -o " + nombre + "-lstMes.png"
            system(executecmd)
            system("start " + nombre + "-lstMes.png ")
        except:
            print("Error al abrir la imagen")

    def imprimir(self):
        list = []
        tmp = self.head
        if self.head is None:
            print("lista vacia")
        elif self.size == 1:
            list.append(str(self.head.mes) + "-> null")
        while tmp.sig is not None:
            list.append(str(tmp.mes) + " -> " + str(tmp.sig.mes))
            tmp = tmp.sig
        list.append(str(tmp.mes) + " ->  null")
        print(str(self.head.mes))
        print(list)

#
# listmn = ListMes()
# listmn.addmes(8)
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

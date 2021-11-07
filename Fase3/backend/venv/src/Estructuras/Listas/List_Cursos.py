from os import system
import os
import time
from datetime import datetime
import base64




class NodoCurso:

    def __init__(self, codigo_, nombre_, creditos_, pre_codigo_, obligatorio_):
        self.codigo = codigo_
        self.nombre = nombre_
        self.creditos = creditos_
        self.pre_codigo = pre_codigo_
        self.obligatorio = obligatorio_
        self.sig = None

class Lista_cursos:
    def __init__(self):
        self.head = None
        self.cola = None
        self.tam = 0

    def addCurso(self,codigo_, nombre_, creditos_, pre_codigo_, obligatorio_):
        nwCurso = NodoCurso(codigo_, nombre_, creditos_, pre_codigo_, obligatorio_)
        if self.head is None:
            self.head = nwCurso
            self.cola = nwCurso
        else:
            self.cola.sig = nwCurso
            self.cola = nwCurso
        self.tam += 1


    def getCurso(self,codigo_):
        current = self.head
        while current:
            if current.codigo == codigo_:
                return current
            current = current.sig
        return None

    def graficar(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.creardot(nameFile)

    def creardot(self,nombre):
        directorio = 'C:\\Users\\GustavC\\Desktop\\Reportes_F3'
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Reportes_F3')
        nwpath = path_desktop +"\\"+ nombre 
        openphat = nwpath.replace('\\','\\\\')
        file = open(openphat + "-cursos.dot", "w")
        file.write("digraph d {\n")
        file.write("rankdir = LR\n")
        file.write("\t node [style=\"rounded,filled\" shape=rectangle fillcolor = darkgray , color=white];\n")
        tmp = self.head
        while tmp is not None:
            file.write("\t" + str(hash(tmp)) +"[label=\"Cod_curso: " + str(tmp.codigo) +" \\n Nombre: " + tmp.nombre +" \\n Creditos: " + str(tmp.creditos) +" \\n Pre_requisitos: " + tmp.pre_codigo +" \\n Obligatorio: " + str(tmp.obligatorio) + "\"]; \n")
            if tmp.sig is not None:
                file.write("\t" + str(hash(tmp)) + " -> " + str(hash(tmp.sig)))
            tmp = tmp.sig
        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + openphat + "-cursos.dot -o " + openphat + "-cursos.png"
            system(executecmd)
            system("start " + nwpath + "-cursos.png ")
        except:
            print("Error al abrir la imagen")

    def printList(self):
        tmp = self.head
        while tmp:
            print("Nodo: " + str(tmp.carnet))
            tmp = tmp.sig

    def getlist(self):
        return self.head

    
#codigo_, nombre_, creditos_, pre_codigo_, obligatorio_):
# nwList = Lista_cursos()
# nwList.addCurso(132,"Prueba1",3,"12,3,99",True)
# nwList.addCurso(34,"Prueba2",2,"12,3,99",False)
# nwList.addCurso(67,"Prueba3",7,"12,3,99",True)
# nwList.addCurso(1,"Prueba6",5,"12,3,99",True)
# nwList.addCurso(3,"Prueba4",9,"12,3,99",False)
# nwList.addCurso(2,"Prueba5",9,"12,3,99",False)
# nwList.graficar()

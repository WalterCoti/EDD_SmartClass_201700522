import time
from datetime import datetime
from os import system
import os
from pathlib import Path

class Nodohash:
    def __init__(self, carnet_):
        self.carnet = carnet_
        self.lista_notas = None
    
    def getcarnet(self):
        return self.carnet
    def getApuntes():
        return self.lista_notas

class NodoNota:
    def __init__(self,carnet_, titulo_, contenido_):
        self.id = None
        self.carnet = carnet_
        self.titulo = titulo_
        self.contenido = contenido_
        self.sig = None

class ListNotas:
    def __init__(self):
        self.size = 0
        self.head = None

    def getNote(self,position_):
        cont = 0
        ntmp = self.head
        while ntmp:
            if cont == position_:
                return ntmp
            ntmp = ntmp.sig
            cont += 1
        return None


    def addNote(self,carnet_, titulo_, contenido_):
        nwNodo = NodoNota(carnet_, titulo_, contenido_)
        if self.head is None:
            nwNodo.sig = self.head
            self.head = nwNodo
        else:
            tmp = self.head
            while tmp.sig is not None:
                tmp = tmp.sig
            tmp.sig = nwNodo
        self.size += 1

    def deletenote(self, position_):
        tmpPos = 0
        current = self.head
        ante = None
        if position_ < self.size:
            while current:
                if current.sig is None and tmpPos == position_:
                    if ante:
                        ante.sig = None
                    else:
                        self.head = None
                        self.size = 0
                elif tmpPos == position_:
                    if tmpPos == 0:
                        self.head = current.sig
                        self.size -= 1
                        return
                    else:
                        ante.sig = current.sig
                        self.size -= 1
                        return
                tmpPos += 1
                ante = current
                current = current.sig
        else:
            print("La posicion \"" + str(position_) + "\" es nula no se puede eliminar")

    def updateNotes(self, nwNota,position):
        current = self.head
        tmpPos = 0
        ante = None
        if position < self.size:
            while current:
                if tmpPos == position:
                    nwNota.sig = current.sig
                    ante.sig = nwNota
                    return
                tmpPos += 1
                ante = current
                current = current.sig
        else:
            print("La posicion \"" + str(position) + "\" es nula no puede editarse")

    def getListNotas(self):
        tmp = self.head
        while tmp:
            print("___________________________")
            print("Titulo: " + tmp.titulo)
            print("Contenido: " + tmp.contenido)
            tmp = tmp.sig



class HashTable:
    def __init__(self):
        self.tabla = [None] * 7
    
    def getnextprimo(self,numero_):
        listnum = [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409]
        for i in range(len(listnum)-1):
            if listnum[i] == numero_:
                return listnum[i+1]

    # Función hash
    def func_hash(self, value):
        return value % len(self.tabla)

    def exp_cuadratic(self, numero_,tamanio_,cont_): # Metodo para verificar nueva celda
        return (self.func_hash(numero_) + cont_*cont_) % tamanio_

    def getpersentuse(self):
        cont = 0
        for i in range(len(self.tabla)):
            if self.tabla[i] is not None:
                cont += 1
        total = cont/len(self.tabla)
        return total

    def find_index(self,carnet_):
        hash = self.func_hash(carnet_)
        if self.tabla[hash] is None:
            return hash
        else:               #inicio exploracion cuadratica
            cont = 1
            while True:
                tmphash = (hash + cont*cont) % len(self.tabla)
                if self.tabla[tmphash].carnet == carnet_:
                    return tmphash
                else:
                    cont += 1

    
    def addNota(self,carnet_,titulo_,contenido_):
        hash = 0
        nwNodo = Nodohash(carnet_)
        hash = self.func_hash(carnet_)
        if self.tabla[hash] is None:
            self.tabla[hash] = nwNodo
            nlist = ListNotas()
            nlist.addNote(carnet_,titulo_,contenido_)
            nwNodo.lista_notas = nlist
        elif self.tabla[hash].carnet == carnet_:
            self.tabla[hash].lista_notas.addNote(carnet_,titulo_,contenido_)
        else:
            conteo = 1
            while True:
                hash = self.exp_cuadratic(carnet_,len(self.tabla),conteo)
                if self.tabla[hash] is None:
                    self.tabla[hash] = nwNodo
                    nlist = ListNotas()
                    nlist.addNote(carnet_,titulo_,contenido_)
                    nwNodo.lista_notas = nlist
                    break
                elif self.tabla[hash].carnet == carnet_:
                    self.tabla[hash].lista_notas.addNote(carnet_,titulo_,contenido_)
                    break
                conteo += 1
        self.rehashtable()

    def rehashtable(self):
        if self.getpersentuse() >=0.5:
            old_table = self.tabla.copy()
            nwLenght = self.getnextprimo(len(self.tabla))
            self.tabla = [None] * nwLenght
            for pos in range(len(old_table)):
                if old_table[pos] is not None:
                    nhash = self.func_hash(old_table[pos].carnet)
                    if self.tabla[nhash] is None:
                        self.tabla[nhash] = old_table[pos]
                    else:
                        conteo = 1
                        while True:
                            nhash = self.exp_cuadratic(old_table[pos].carnet,len(self.tabla),conteo)
                            if self.tabla[nhash] is None:
                                self.tabla[nhash] = old_table[pos]
                                break
                            conteo += 1
                
    def getNotas(self,carnet_): # Metodo para buscar elementos
        hash = self.func_hash(carnet_)
        if self.tabla[hash] is None:
            return None
        elif self.tabla[hash].carnet == carnet_: 
            #print("si esta")
            return self.tabla[hash].lista_notas
        else:
            tam = len(self.tabla)
            conteo = 1
            while True:
                if  conteo <= tam:
                    nhash = self.exp_cuadratic(carnet_,tam,conteo)
                    if self.tabla[nhash] is None:
                        pass
                    elif self.tabla[nhash].carnet == carnet_:
                        return self.tabla[nhash].lista_notas
                    conteo += 1
                else:
                    print("carnet no existe")
                    break
            return None
                               

    def graficarTabla(self):
        timenow = datetime.now().time()
        nameFile = str(timenow.hour) + "-" + str(timenow.minute) + "-" + str(timenow.second)
        self.graph_dot(nameFile)

        # generar archivo.dota
        
    def graph_dot(self, nombre):
        directorio = 'C:\\Users\\GustavC\\Desktop\\Reportes_F3'
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Reportes_F3')
        nwpath = path_desktop +"\\"+ nombre 
        openphat = nwpath.replace('\\','\\\\')
        file = open(openphat + '-TabHash.dot', "w")
        file.write("digraph tabhash {\n")
        file.write("\t nodesep=.05;\n \trankdir=LR;")
        file.write("\tnode [shape=record,width=.1,height=.1, style=\"rounded,filled\"  fillcolor = firebrick3 , color=black, fontcolor=white];\n")
        # Graficar tabla
        contTAblahash =""
        for i in range(0,len(self.tabla)-1):
            if self.tabla[i] is not None:
                contTAblahash = contTAblahash + "<f" + str(i)+ "> " + str(self.tabla[i].carnet)+"|"+ "\n"
            else:
                contTAblahash = contTAblahash + "<f" + str(i)+ ">---------|"+ "\n"
        if self.tabla[-1] is not None:
            contTAblahash = contTAblahash +  "<f" + str(len(self.tabla)-1)+ "> " + str(self.tabla[-1].carnet)
        else:
            contTAblahash = contTAblahash + "<f" + str(i)+ ">---------"+ "\n"
            
        file.write("\t nodohash[label = \"" + contTAblahash + "\" , fillcolor = midnightblue height= " + str(len(self.tabla)) +" ];\n")
        for pos in range(len(self.tabla)):
            if self.tabla[pos] is not None:
                tmp = self.tabla[pos].lista_notas.head
                while tmp:
                    if tmp is not None:
                         file.write("\t" + str(hash(tmp)) + "[label = \"" + tmp.titulo + "\"];\n")
                    if tmp.sig is not None:
                        file.write("\t" + str(hash(tmp)) + " -> " + str(hash(tmp.sig)) + "\n")
                    
                    tmp = tmp.sig
                file.write("\t nodohash:f"+str(pos)+ " -> " + str(hash(self.tabla[pos].lista_notas.head)) + "\n") 
        file.write("}")
        file.close()
        try:
            time.sleep(1)
            executecmd = "dot -Tpng " + openphat + "-TabHash.dot -o " + openphat + "-TabHash.png"
            system(executecmd)
            system("start " + nwpath + "-TabHash.png ")
        except:
            print("Error al abrir la imagen")


        
# nwHastab = HashTable()
# nwHastab.addNota(201812453,"Titulo 1","Contenido 1")
# nwHastab.addNota(201912462,"Titulo 2","Contenido 2")
# nwHastab.addNota(201545212,"Titulo 3","Contenido 3")
# nwHastab.addNota(201545212,"Titulo 4","Contenido 4")
# nwHastab.addNota(201912462,"Titulo 5","Contenido 5")
# nwHastab.addNota(201812453,"Titulo 6","Contenido 6")
# nwHastab.addNota(201812453,"Titulo 7","Contenido 7")
# nwHastab.addNota(201812234,"Titulo 8","Contenido 8")
# nwHastab.addNota(206665456,"Titulo 9","Contenido 9")
# nwHastab.addNota(201545345,"Titulo 10","Contenido 10")
# nwHastab.addNota(201545212,"Titulo 11","Contenido 11")
# nwHastab.addNota(201712462,"Titulo 12","Contenido 12")
# nwHastab.addNota(201712346,"Titulo 13","Contenido 13")
# nwHastab.addNota(201353456,"Titulo 14","Contenido 14")
# nwHastab.addNota(201812453,"Titulo 15","Contenido 15")
# nwHastab.addNota(201912462,"Titulo 16","Contenido 16")
# nwHastab.addNota(201545212,"Titulo 17","Contenido 17")
# nwHastab.addNota(201545212,"Titulo 18","Contenido 18")
# nwHastab.addNota(201912462,"Titulo 19","Contenido 19")
# nwHastab.addNota(201812453,"Titulo 20","Contenido 20")
# nwHastab.addNota(201812453,"Titulo 21","Contenido 21")
# nwHastab.addNota(201812234,"Titulo 22","Contenido 22")
# nwHastab.addNota(206665456,"Titulo 23","Contenido 23")
# nwHastab.addNota(201545345,"Titulo 24","Contenido 24")
# nwHastab.addNota(201545212,"Titulo 25","Contenido 25")
# nwHastab.addNota(201712462,"Titulo 26","Contenido 26")
# nwHastab.addNota(201712346,"Titulo 27","Contenido 27")
# nwHastab.addNota(201353456,"Titulo 28","Contenido 28")
# nwHastab.graficarTabla()
# tmp = nwHastab.getNotas(201545212)
# print(tmp)
# aver = tmp.getApuntes()
# print(aver)
# aver.getListNotas()


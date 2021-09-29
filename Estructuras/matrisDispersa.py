class nodo:
    def __init__(self, valor_, posx_=0, posy_=0):
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

#
# listita = lista()
# listita.add_cabecera(9)
# listita.add_cabecera(5)
# listita.add_cabecera(3)
# listita.add_cabecera(90)
# listita.add_cabecera(23)
# listita.add_cabecera(4)
# listita.add_cabecera(2)
# listita.add_cabecera(7)
# listita.add_cabecera(1)
# listita.exist(6)
# listita.exist(1)
# listita.exist(23)
# listita.exist(50)



class matriz:
    def __init__(self):
        self.lstDias = lista()
        self.lstHoras = lista()

    def insertar(self, valor, pos_x, pos_y):
        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        if M_dia is None and M_hora is None:
            self.Caso1(valor, pos_x, pos_y)
        elif M_dia is None and M_hora is not None:
            self.Caso2(valor, pos_x, pos_y)
        elif M_dia is not None and M_hora is None:
            self.Caso3(valor, pos_x, pos_y)
        else:
            self.Caso4(valor, pos_x, pos_y)

    def Caso1(self, valor, pos_x, pos_y):
        self.lstDias.add_cabecera(pos_x)
        self.lstHoras.add_cabecera(pos_y)

        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        nuevo = nodo(valor, pos_x, pos_y)
        M_dia.N_abajo = nuevo
        nuevo.N_arriba = M_dia

        M_hora.N_der = nuevo
        nuevo.N_izq = M_hora

    def Caso2(self, valor, pos_x, pos_y):
        self.lstDias.add_cabecera(pos_x)

        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        agregado = False

        nuevo = nodo(valor, pos_x, pos_y)
        aux = M_hora.N_der
        cabecera = 0

        while (aux != None):
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

    def Caso3(self, valor, pos_x, pos_y):
        self.lstHoras.add_cabecera(pos_y)

        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        agregado = False

        nuevo = nodo(valor, pos_x, pos_y)
        aux = M_dia.N_abajo
        cabecera = 0

        while (aux != None):
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
            while (aux.N_abajo != None):
                aux = aux.N_abajo
            nuevo.N_arriba = aux
            aux.N_abajo = nuevo

        M_hora.N_der = nuevo
        nuevo.N_izq = M_hora

    def Caso4(self, valor, pos_x, pos_y):
        M_dia = self.lstDias.search(pos_x)
        M_hora = self.lstHoras.search(pos_y)

        nuevo = nodo(valor, pos_x, pos_y)

        agregado = False
        aux = M_dia.N_abajo

        while (aux != None):
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
            while (aux.N_abajo != None):
                aux = aux.N_abajo
            nuevo.N_arriba = aux
            aux.N_abajo = nuevo
        agregado = False
        aux = M_hora.N_der
        cabecera = 0

        while (aux != None):
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

    def imprimir_M_dia(self):
        cabecera = self.lstDias.head
        while (cabecera != None):
            aux = cabecera.N_abajo
            while (aux != None):
                print(aux.valor, aux.pos_x, aux.pos_y)
                aux = aux.N_abajo
            cabecera = cabecera.sig

    def imprimir_M_hora(self):
        cabecera = self.lstHoras.head
        while (cabecera != None):
            aux = cabecera.N_der
            while (aux != None):
                print(aux.valor, aux.pos_x, aux.pos_y)
                aux = aux.N_der
            cabecera = cabecera.sig


matriz = matriz()

matriz.insertar(1, 1,1)
matriz.insertar(2, 0,3)
matriz.insertar(3, 10,5)
matriz.insertar(4, 2,9)
print("Cabeceras")
matriz.lstDias.print()
matriz.lstHoras.print()

print("Se imprime de forma M_dia")
matriz.imprimir_M_dia()
print("Se imprime de forma M_hora")
matriz.imprimir_M_hora()
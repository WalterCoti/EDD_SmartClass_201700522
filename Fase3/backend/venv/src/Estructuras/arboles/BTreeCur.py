class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.ant = None
        self.sig = None
        self.der = None
        self.izq = None


class Rama:
    def __init__(self):
        self.contador = 0
        self.hoja = True
        self.raiz = None

    def insertar(self, nodo):
        if self.raiz is None:
            self.raiz = nodo
            self.contador += 1
        else:
            temp = self.raiz
            while temp is not None:
                if (nodo.valor <= temp.valor):
                    self.contador += 1
                    if (temp == self.raiz):
                        self.raiz.ant = nodo
                        self.raiz.izq = nodo.der
                        self.raiz = nodo
                        break
                    else:
                        nodo.ant = temp.ant
                        nodo.sig = temp
                        temp.ant.sig = nodo
                        temp.ant.der= nodo.izq
                        temp.ant = nodo
                        temp.izq = nodo.der
                        break
                elif temp.sig is None:
                    self.contador += 1
                    temp.sig = nodo
                    temp.der = nodo.izq
                    nodo.ant = temp
                    nodo.sig = None
                    break

                temp = temp.sig

    def print(self):
        result = ""
        temp = self.raiz
        contador = 0
        while temp != None:
            if contador == 0:
                result = temp.valor
            else:
                result += "|" + temp.valor
            temp = temp.sig
        return result


class BTree:
    def __init__(self,orden=5):
        self.raiz = None
        self.orden = orden

    def insertar(self,valor):
        nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = Rama()
            self.raiz.insertar(nodo)
            return
        else:
            temp = self.add(nodo, self.raiz)
            if isinstance(temp,Nodo):
                self.raiz = Rama()
                self.raiz.insertar(temp)
                self.raiz.hoja = False

    def add(self,nodo, rama):
        if rama.hoja:
            rama.insertar(nodo)
            if rama.contador == self.orden:
                return self.dividirRama(rama)
            else:
                return rama

        else:
            temp = rama.raiz
            while temp is not None:
                if nodo.valor == temp.valor:
                    return rama
                elif nodo.valor < temp.valor:
                    aux = self.add(nodo, temp.izq)
                    if isinstance(aux, Nodo):
                        rama.insertar(aux)
                        if rama.contador == self.orden:
                            return self.dividirRama(rama)
                        return rama

                elif temp.sig is None:
                    aux = self.add(nodo, temp.der)
                    if isinstance(aux , Nodo):
                        rama.insertar(aux)
                        if rama.contador == self.orden:
                            return self.dividirRama(rama)

                    return rama

                temp = temp.sig
        return rama


    def dividirRama(self,rama):
        der = Rama()
        izq = Rama()
        medio = None
        temp = rama.raiz
        inicio = 1
        valorMedio = int(self.orden / 2) + 1
        final = self.orden
        for i in range(self.orden):
            nodo = Nodo(temp.valor)
            nodo.izq = temp.izq
            nodo.der = temp.der

            if nodo.der is not None and nodo.izq is not None:
                izq.hoja = False
                der.hoja = False

            if i >= inicio and i < valorMedio:
                izq.insertar(nodo)
            elif  i == valorMedio:
                medio = nodo
            elif i <= final and i > valorMedio:
                der.insertar(nodo)


        medio.izq = izq
        medio.der = der
        return medio

nwB = BTree()
nwB.insertar(3)
nwB.insertar(5)
nwB.insertar(7)
nwB.insertar(9)
nwB.insertar(2)
nwB.insertar(1)
nwB.insertar(77)




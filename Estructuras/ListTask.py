class NodoTask:
    def __init__(self,id_task_,carnet_,name_task_,desc_task_,materia_,fecha_,hora_,estado_):
        self.id_task = id_task_
        self.name_task = name_task_
        self.desc_task = desc_task_
        self.carnet = carnet_
        self.materia = materia_
        self.fecha = fecha_
        self.hora = hora_
        self.estado  = estado_
        self.sig = None

class lisTask:
    def __init__(self):
        self.head = None
        self.size = 0
        self.counter = 0

    def addTask(self,carnet_,name_task_,desc_task_,materia_,fecha_,hora_,estado_):
        nwNodo = NodoTask(self.counter,carnet_,name_task_,desc_task_,materia_,fecha_,hora_,estado_)
        if self.head is None:
            nwNodo.sig = self.head
            self.head = nwNodo
        else:
            tmp = self.head
            while tmp.sig is not None:
                tmp = tmp.sig
            nwNodo.sig = tmp.sig
            tmp.sig = nwNodo
            
        self.counter +=1
        self.size += 1

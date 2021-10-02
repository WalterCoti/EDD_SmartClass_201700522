class NodoTask:
    def __init__(self,carnet_,name_task_,desc_task_,materia_,fecha_,hora_,estado_):
        self.carnet = carnet_
        self.name_task = name_task_
        self.desc_task = desc_task_
        self.materia = materia_
        self.fecha = fecha_
        self.hora = hora_
        self.estado  = estado_
        self.sig = None

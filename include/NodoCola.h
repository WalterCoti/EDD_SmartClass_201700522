#ifndef NODOCOLA_H
#define NODOCOLA_H
#include <string>
#include "Estudiante.h"
#include "Tarea.h"
using namespace std;

class NodoCola
{
    public:
        NodoCola();
        NodoCola(int idError_, string descript_, string tipo_,Estudiante *estudiante_,NodoCola *next_);
        NodoCola(int idError_, string descript_, string tipo_, Tarea *tarea_,NodoCola *next_);

        void setnext(NodoCola *next_);
        void setidError(int id_);
        void setdescript(string descript_);
        void setTipo(string tipo_);
        void setEstudiante(Estudiante *nStudent_);
        void setTarea(Tarea *nTarea_);

        int getidError();
        string getdescript();
        string getTipo();
        Estudiante *getEstudiante();
        Tarea *getTarea();
        NodoCola *getNext();




    private:
        int idError;
        string descripcion;
        string tipo;
        Estudiante *estudiante;
        Tarea *tarea;
        NodoCola *next;
};

#endif // NODOCOLA_H

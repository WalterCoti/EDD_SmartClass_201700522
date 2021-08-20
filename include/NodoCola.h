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

    protected:

    private:
        int idError;
        string descripcion;
        string tipo;
        Estudiante *estudiante;
        Tarea *tarea;
};

#endif // NODOCOLA_H

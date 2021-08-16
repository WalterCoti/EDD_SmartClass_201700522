#ifndef NODOD_H
#define NODOD_H
#import "Estudiante.h"

class NodoD
{
    public:
        NodoD();
        NodoD(Estudiante *estudiante_);
        NodoD(Estudiante *estudiante_,NodoD *next_,NodoD *previous_);

        void setnext(NodoD *next_);
        void setprevious(NodoD *previous_);
        void setestudiante(Estudiante *estudiante_);

        NodoD *getnext();
        NodoD *getprevious();
        Estudiante *getEstudiante();


    private:
        NodoD *next;
        NodoD *previous;
        Estudiante *estudiante;
};

#endif // NODOD_H

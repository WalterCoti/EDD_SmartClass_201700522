#ifndef NODODOBLE_H
#define NODODOBLE_H
#include "Tarea.h"
using namespace std;
class NodoDoble
{
    public:
        NodoDoble();
        NodoDoble(Tarea *tarea_);
       // NodoDoble(Tarea *tarea_, NodoDoble *newt, NodoDoble *prev_);

        void setTarea(Tarea *tarea_);
        void setnext(NodoDoble *next);
        void setprev(NodoDoble *prev_);
        void setid(int id);


        Tarea *getTarea();
        NodoDoble *getnext();
        NodoDoble *getprev();
        int getid();

    private:
        Tarea *tarea;
        NodoDoble *next;
        NodoDoble *prev;
        int id ;
};

#endif // NODODOBLE_H

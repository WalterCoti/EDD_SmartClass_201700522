#ifndef COLAERR_H
#define COLAERR_H
#include "NodoCola.h"


class ColaErr
{
    public:
        ColaErr();
        void encolar(NodoCola *newError);
        void descolar();
        void graficar();
        int getnFile();
        bool isEmpty();

    protected:

    private:
        NodoCola *head;
        NodoCola *end;
        int nfile,tamanio;

};

#endif // COLAERR_H

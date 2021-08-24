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
        bool isEmpty();

    protected:

    private:
        NodoCola *head;
        NodoCola *end;
};

#endif // COLAERR_H

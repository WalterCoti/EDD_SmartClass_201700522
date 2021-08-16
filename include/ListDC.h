#ifndef LISTDC_H
#define LISTDC_H
#include "Estudiante.h"
#include "NodoD.h"
using namespace std;

class ListDC
{
    public:
        ListDC();
        void addEstudent(Estudiante *estudiante_);
        bool isEmptyLCD();
        void deleteEstudent(string carnet_);
        void updateEstudent(string carnet_);
        void graphListEstudent();

    private:
        NodoD *head;
        NodoD *end;
        int size;

};

#endif // LISTDC_H

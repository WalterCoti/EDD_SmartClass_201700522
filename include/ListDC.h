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
        void deletStudent(string dpistudent_);
        void updateStudent(string dpistudent_, int opc_);
        void graphListEstudent();

    private:
        NodoD *head;
        NodoD *end;
        int size;

};

#endif // LISTDC_H

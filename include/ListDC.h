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
        bool existEst(string dpi_);
        void deletStudent(string dpistudent_);
        void updateStudent(string dpistudent_, int opc_);
        void printlist();
        void graphListDC();


    private:
        NodoD *head;
        NodoD *end;
        int size;

};

#endif // LISTDC_H

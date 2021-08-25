#ifndef LISTDOBLE_H
#define LISTDOBLE_H
#include "NodoDoble.h"

class ListDoble
{
    public:
        ListDoble();
        void addNodo(NodoDoble *nwNodo_);
        void deletNodo(string indice);
        void getgraphList();
        bool isEmptyLD();


    private:
        NodoDoble *headL;
        NodoDoble *end;
        int tam;
        int numarch;
};

#endif // LISTDOBLE_H

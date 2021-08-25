#include "ListDoble.h"

ListDoble::ListDoble()
{
    this->headL = NULL;
    this->end = NULL;
    this->tam = 0;
    this->numarch = 0;
}

bool ListDoble::isEmptyLD()
{
    if(this->headL = NULL){
        return true;
    }else{
        return false;
    }
}

void ListDoble::addNodo(NodoDoble *nwNodoDoble){
if(isEmptyLD()){
    this->headL = nwNodoDoble;
    this->end = nwNodoDoble;
    nwNodoDoble->setnext(NULL);
    nwNodoDoble->setprev(NULL);
}else{
    this->end->setnext(nwNodoDoble);
    nwNodoDoble->setprev(end);
    nwNodoDoble->setnext(NULL);
    this->end = nwNodoDoble;
}
this->tam++;
}

void ListDoble::deletNodo(string indice){
}

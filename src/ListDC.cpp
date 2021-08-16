#include "ListDC.h"
#include "Estudiante.h"
ListDC::ListDC()
{
    this->head = NULL;
    this->end = NULL;
    this->size = 0;
}

bool ListDC::isEmptyLCD(){
    if(this->head == NULL){
        return true
    }
    return false;
}

void ListDC::addEstudent(Estudiante *estudiante_){
    NodoD *newNodo = new NodoD(estudiante_);
    if(isEmpty()){
        this->head = newNodo;
        this->end = newNodo;
        newNodo->setnext(head)
        newNodo->setprevious(end)
    } else {
        this->end->setnext(newNodo);
        newNodo->setprevious(end);
        this->head->setprevious(newNodo);
        newNodo->setnext(head);
        this->end = newNodo;
    }
}

void ListDC::updateEstudent(string carnet_){

}

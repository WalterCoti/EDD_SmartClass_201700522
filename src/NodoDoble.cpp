#include "NodoDoble.h"

NodoDoble::NodoDoble()
{
    this->tarea = NULL;
    this->next = NULL;
    this->prev = NULL;
    this->id = 0;
}

NodoDoble::NodoDoble(Tarea *tarea_){
    this->tarea = tarea_;
    this->next = NULL;
    this->prev = NULL;
    this->id = 0;
}

void NodoDoble::setTarea(Tarea *tarea_){
    this->tarea = tarea_;
}

void NodoDoble::setnext(NodoDoble *next_){
    this->next = next_;
}

void NodoDoble::setprev(NodoDoble *prev_){
    this->prev = prev_;
}

void NodoDoble::setid(int ID_){
    this->id = ID_;
}

Tarea *NodoDoble::getTarea(){
    return tarea;
}

NodoDoble *NodoDoble::getnext(){
    return next;
}

NodoDoble *NodoDoble::getprev(){
    return prev;
}

int NodoDoble::getid(){
    return id;
}

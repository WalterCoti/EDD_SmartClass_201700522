#include "ColaErr.h"

ColaErr::ColaErr()
{
    this->head = NULL;
    this->end = NULL;
}

bool ColaErr::isEmpty(){
    if(this->head == NULL){
        cout << "esta vacio"<< endl;
        return true;
    }
    cout << "no esta vacio"<< endl;
    return false;
}

void ColaErr::encolar(NodoCola *newErr_){
    if(isEmpty()){
        this->head = newErr_;
        this->end = newErr_;
    } else {
        this->end->setnext(newErr_);
        this->end = newErr_;
    }
}

void ColaErr::descolar(){
    NodoCola *nodoDel = this->head;
    NodoCola *tmp = this->head;
    if(isEmpty()){
        cout << "Cola Vacia"<< endl;
    }else if(this->head == this->end){
        this->head = NULL;
        this->end = NULL;
        //cout << "Dato eliminado : " << nodoDel->getnombre() << " - "<<  nodoDel->getedad() << endl;
    }else{
        this->head = tmp->getNext();
        //cout << "Dato eliminado : " << nodoDel->getnombre() << " - "<<  nodoDel->getedad() << endl;
    }
    delete nodoDel;
    delete tmp;
}


void ColaErr::graficar(){
    NodoCola *tmp = this->head;
    if(isEmpty()){
         cout << "Cola Vacia"<< endl;
    }else{
        do{
            cout << "Nombre: " << tmp->getTipo() << endl;
            tmp = tmp->getNext();
        }while(tmp == end);
    }


    //editar para graficar
}

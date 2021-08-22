#include "ListDC.h"
#include "Estudiante.h"
ListDC::ListDC()
{
    this->head = NULL;
    this->end = NULL;
    this->size = 0;
}

bool ListDC::isEmptyLCD()
{
    if(this->head == NULL){
        return true;
    }
    return false;
}

bool ListDC::existEst(string dpi_){
    NodoD *tmp = new NodoD();
    tmp = this->head;
    if(this->head != NULL){
        do{
            if(tmp->getEstudiante()->getdpi() == dpi_){
                return true;
            }
            cout << tmp->getEstudiante()->getname() << endl;
            tmp = tmp->getnext();
        }while(tmp != this->head);
    } else{
    cout << "\n La lista  Vacia" << endl;
    }
    return false;
}


void ListDC::addEstudent(Estudiante *estudiante_){
    NodoD *newNodo = new NodoD(estudiante_);
    if(isEmptyLCD()){
        this->head = newNodo;
        this->end = newNodo;
        newNodo->setnext(head);
        newNodo->setprevious(end);
    } else {
        this->end->setnext(newNodo);
        newNodo->setprevious(end);
        this->head->setprevious(newNodo);
        newNodo->setnext(head);
        this->end = newNodo;
    }
    this->size++;
}

void ListDC::updateStudent(string dpistudent_,int opc_)
{


}

void ListDC::deletStudent(string dpistudent_){
    NodoD *actual  = this->head;
    NodoD *anterior = NULL;
    bool nodoDel = false;
    if(isEmptyLCD()){
        cout << "Lista vacia" << endl;
    }else{
        do{
            if(actual->getEstudiante()->getdpi() == dpistudent_){
                //obtener datos del que elimino xD
                if(actual == this->head){
                    this->head = this->head->getnext();
                    this->head->setprevious(this->end);
                    this->end->setnext(this->head);
                }else if(actual == this->end){
                    this->end = anterior;
                    this->end->setnext(this->head);
                    this->head->setprevious(this->end);
                }else{
                    anterior->setnext(actual->getnext());
                    actual->getnext()->setprevious(anterior);
                }
                nodoDel = true;
            }
            anterior = actual;
            actual = actual->getnext();

        }while(actual != this->head && nodoDel != true);

        if(!nodoDel){
            cout << " Usuario no registrado";
        }
    }

}


void ListDC::printlist()
{
 NodoD *tmp = new NodoD();
tmp = this->head;
 if(this->head != NULL){
 do{
    cout << tmp->getEstudiante()->getname() << endl;
    tmp = tmp->getnext();
 }while(tmp != this->head);
 } else{
    cout << "\n La lista  Vacia" << endl;
 }
}

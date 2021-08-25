#include "ColaErr.h"
#include <fstream>

ColaErr::ColaErr()
{
    this->head = NULL;
    this->end = NULL;
    this->nfile = 0;
}

bool ColaErr::isEmpty(){
    if(this->head == NULL){
        return true;
    }
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
    NodoCola *aux = this->head;
    string n_data = "";
    string e_data = "";
    string graph = "digraph List {\nrankdir=LR;\nnode [shape = record, color=blue , style=filled, fillcolor=skyblue];\n";
    string n_actual;
    string n_sig;
    if(isEmpty()){
        cout << "Cola vacia" << endl;
    }else if(this->tamanio == 1){
            n_actual = to_string(aux->getidError());

            n_data +=  n_actual + "[label=\"ID : " + to_string(aux->getidError()) + "\\n\" \n"
                         + "+ \" Tipo:   "+ aux->getTipo() + "\\n\" \n"
                         + "+ \" Descripcion:  "+ aux->getdescript() +  + "\"]; \n";
            e_data += n_actual;

        }else{
        while(aux != this->end){
                n_actual = to_string(aux->getidError());
                n_sig =    to_string(aux->getNext()->getidError());
                n_data +=  n_actual + "[label=\"ID : " + to_string(aux->getidError()) + "\\n\" \n"
                         + "+ \" Tipo:   "+ aux->getTipo() + "\\n\" \n"
                         + "+ \" Descripcion:  "+ aux->getdescript() +  + "\"]; \n";
                e_data += n_actual+ "->" + n_sig + ";\n";
                aux = aux->getNext();
        }

     }

    graph += n_data;
    graph += e_data;
    graph += "\n}";
    //-------------------------------------
    try{
        //Esta variable debe ser modificada para agregar su path de creacion de la Grafica
        string path = "D:\\Resultados\\";
        ofstream file;
        file.open(path + "Cola" + to_string(this->nfile) + ".dot",std::ios::out);
        if(file.fail()){
            exit(1);
        }
        file<<graph;
        file.close();
        string command = "dot -Tpng " + path + "Cola"+to_string(this->nfile) +".dot -o  " + path + "Cola"+to_string(this->nfile)+".png";
        system(command.c_str());
        cout<<"Grafica generada con exito"<<endl;
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    //-------------------------------------
    this->nfile++;

    delete aux;
    //editar para graficar
}

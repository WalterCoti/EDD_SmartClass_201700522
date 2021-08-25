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
    if(this->headL == NULL){
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

void ListDoble::getgraphList(){
    cout<< "Tamanio: "<< to_string(this->tam)<< endl;;
    NodoDoble *tmp = this->headL;
    if(this->headL != NULL){
           // cout << "Lista Linealizada vacia" << endl;
    do{
        if(tmp->getTarea() == NULL){
            cout<<"---" <<to_string(tmp->getid())<<endl;
        }else{
            cout << "___" << tmp->getTarea()->getname_t() << endl;
        }
        tmp = tmp->getnext();
    }while(tmp != NULL);
    } else{
        cout << "\n Lista Linealizada vacia" << endl;
    }

}

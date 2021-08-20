#ifndef FECHA_H
#define FECHA_H
#include <string>
using namespace std;

class Fecha
{
    public:
        //constructor
        Fecha(int dia_,int mes_, int anio_);
        //setters
        int getdia();
        int getmes();
        int getanio();
        string getnewFormat();

        //getters
        void setdia(int dia_);
        void setmes(int mes_);
        void setanio(int anio_);


    private:
        int dia;
        int mes;
        int anio;
};

#endif // FECHA_H

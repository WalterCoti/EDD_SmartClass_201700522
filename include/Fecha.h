#ifndef FECHA_H
#define FECHA_H
#include <string>
using namespace std;

class Fecha
{
    public:
        //constructor
        Fecha();
        Fecha(string dia_,string mes_, string anio_);
        //setters
        string getdia();
        string getmes();
        string getanio();
        string getnewFormat();

        //getters
        void setdia(string dia_);
        void setmes(string mes_);
        void setanio(string anio_);


    private:
        string dia,mes,anio;
};

#endif // FECHA_H

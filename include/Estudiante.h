#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H


class Estudiante
{
    public:
        Estudiante();
        Estudiante(int carnet_,string dpi_, string name_, string carrera_, string email_, string pass_, int credit_, int edad_ );
    //setters
    void setcarnet(int carnet_);
    void setdpi(string dpi_);
    void setname(string name_);
    void setcarrera(string carrera_);
    void setemail(string email_);
    void setpass(string pass_);
    void setcredit(int credit_);
    void setedad(int edad_);

    //getters
    int getcarnet();
    string getdpi();
    string getname();
    string getcarrera();
    string getemail();
    string getpass();
    int getcredit();
    int getedad();

    private:
        int carnet;
        string dpi;
        string name;
        string carrera;
        string email;
        string pass;
        int credit;
        int edad;

};

#endif // ESTUDIANTE_H

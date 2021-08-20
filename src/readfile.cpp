#include "readfile.h"
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include "windows.h"
#include <regex>

using namespace std;

void readfiles(string path_){
    string text = "";
    string head = "";
    ifstream fileOp(path_);

    if(!fileOp.is_open()){
        cout << "ERROR: Archivo no pudo ser abierto" << endl;
    }
    getline(fileOp, head,'\n');
    while(fileOp.good()){
        getline(fileOp, text,'\n');
        cout <<text<< endl;
    }
}

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
double mean(vector<double> numero){
    double sum = 0;
    int cont = 0;
    for(double x: numero){
        sum += x;
        cont++;
    }
    double media = sum/cont;
    return (media);
}

double desvio(vector<double> lista){
    double med = mean(lista);
    double desvio = 0;
    int cont = 0;
    for(double x : lista)
    {
        desvio += pow(x-med,2);
        cont++;
    }
    desvio = sqrt(desvio/cont);
    return (desvio);
}

int main(){
    vector<double> notas = {1,2,3,4,5,6};
    double A = mean(notas);
    double B = desvio(notas);
    cout<< "Média: " << A << endl;
    cout<< "Desvio: " << B << endl;
}
#include <stdio.h>

double c_kilven(double _temp, char* key);
int main(void)
{

    printf("hello world\n");
    double result = c_kilven(1234.324234325, "kelvin");
    printf("%f", result);
    return 1;

}

double c_kilven(double _temp, char* key)
{
    char* c = "c";
    char* k = "k";
    char* f = "f";
    
    if(key == c || key == "celsius"){
        _temp = _temp + 273.15;
        return _temp;
    }
    else if(key == k || key == "kelvin"){
        return _temp;
    }
    else if(key == f || key == "fahrenheit"){
        _temp = (_temp - 32) / 1.8;
        _temp = _temp + 273.15;
        return _temp;
    }
    else{
        return 0;
    }

}
#include <iostream>

void main(){
    int s = 5;
    int r = 3;
    int n = 2;
    int p = 1;

    while (r > 0) {
        if (r % 2 == 1){
            p = p*s % n;
        }
        s = s*s % n;
        r = r/2;
    }

    std::cout << p << std::endl;
}
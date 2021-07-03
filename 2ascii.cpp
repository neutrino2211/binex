#include <iostream>

int main(){
    char c;
    while(c != '.'){
        std::cin >> c;
        std::cout << (int) c << std::endl;
    }

    return 0;
}
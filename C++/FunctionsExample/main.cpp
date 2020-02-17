#include <iostream>

using namespace std;

int mult(int x, int y){
    return x*y;
}

int basicMult(){
    int x,y;
    x = 2;
    y = 4;
    return x * y;

}

void voidMult(){
    int x,y;
    x = 2;
    y = 4;
    cout << x*y << endl;
}

#Should represent variable parameter passthrough but isn't working.
int varMult(int& x, int y){
    x = 10;
    return x*y;
}

int main(){

    int x = 12;
    cout<<x<<endl<<varMult(x,3)<<endl<<x<<endl;

    cout<<mult(2,4)<<endl;
    voidMult();
    cout << basicMult();
    return 0;
}

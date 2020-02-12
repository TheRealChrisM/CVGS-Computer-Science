#include <iostream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    //cin.get();
    int x = 0;

    while(x<1000){
        if (((x%5)==0)&&((x%3)==0)){
            cout << "FizzBuzz\n";
        }
        else if((x%3)==0){
            cout << "Fizz\n";
        }
        else if((x%5)==0){
            cout<< "Buzz\n";
        }
        else{
            cout<<x<<"\n";
        }
        x = x+1;

    }
    //return 0;
}

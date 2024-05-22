#include <iostream>
using namespace std;

int main() {
    int count = 0;
    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            cout <<" (i:" << i << " j:" << j << ")";
            count = count + 1;
        }
        cout << "\n";
    }
    cout << " count: " << count;
    return 0;
}

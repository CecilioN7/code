// NAME: Cecilio Navarro
// FILE: nested_loop.cpp
// DATE: Sat May 25 2024
// g++ nestedloop.cpp -o nested_loop -Wall
// n(n-1) / 2

#include <iostream>
using namespace std;

int main() {
    // nested for loop
    int count = 0;

    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            cout <<" (i:" << i << " j:" << j << ")";
            count += 1;
        }
        cout << "\n";
    }

    cout << "\n" << " count: " << count << "\n\n";

    // nested for loop - avoiding self comparison
    count = 0;

    for (int i=0; i<10; i++){
        for (int j=i+1; j<10; j++){
            cout <<" (i:" << i << " j:" << j << ")";
            count += 1;
        }
        cout << "\n";
    }

    cout << " count: " << count << "\n\n";

    // visual output created by ChatGPT
    const string RESET = "\033[0m";         // Reset all attributes
    const string RED = "\033[31m";          // Red text
    const string BLUE = "\033[34m";         // Blue text
    const string WHITE = "\033[37m";        // White text

    count = 0;
    // First loop: default text is blue, highlight the pairs that would match the second loop in red
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (j > i) {
                cout << WHITE << " (" << RED << "i:" << i << WHITE << " " << RED << "j:" << j << WHITE << ")";
            } else {
                cout << WHITE << " (" << BLUE << "i:" << i << WHITE << " " << BLUE << "j:" << j << WHITE << ")";
            }
            count += 1;
        }
        cout << "\n";
    }
    cout << "\n" << " count: " << count << "\n\n";

    return 0;
}

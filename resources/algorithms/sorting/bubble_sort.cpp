// NAME: Cecilio Navarro
// ORGN: 
// FILE: bubble_sort.cpp
// DATE: Fri May 24 2024

#include <iostream>

using namespace std;

int main() {
    const int arraySize = 5;
    int array[] = {5, 24, 7, 2, 10};
    for (int i=0; i<arraySize; i++) {
        for (int j=0; j<arraySize; j++) {
            if (array[j] < array[j+1]) {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    for (int i=0; i<arraySize; i++) {
        cout << array[i] << "\n";
    }
}
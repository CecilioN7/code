# NAME: Cecilio Navarro
# ORGN: resources/algorithms/sorting/bubble_sort.py
# FILE: bubble_sort.py
# DATE: Fri May 24

def bubbleSort(my_array):
    arraySize = len(my_array)
    for i in range(arraySize):
        for j in range(0, my_array-i-1):
            if (my_array[j] < my_array[j+1]):
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array

my_array = [5, 4, 3, 2, 1]

sorted_array = bubbleSort(my_array)

print(sorted_array)


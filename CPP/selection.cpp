#include<iostream>
#include <algorithm>
using namespace std;

void display(int *array, int n) {
   for(int i = 0; i<n; i++)
      cout << array[i] << " ";
   cout << endl;
}

void selectionSort(int *array, int n) {
   int i, j, min;
   for(i = 0; i<n; i++) {
      min = i;   //get index of minimum data
      for(j = i+1; j<n; j++)
      {
        if(array[j] < array[min])
        {
            min = j;
        }   
      }
      swap(array[min],array[i]);
   }
}
int main() {
   int n;
   cout << "Enter the number of elements: ";
   cin >> n;
   int arr[n];           //create an array with given number of elements
   cout << "Enter elements:" << endl;
   for(int i = 0; i<n; i++) {
      cin >> arr[i];
   }
   cout << "Array before Sorting: ";
   display(arr, n);
   selectionSort(arr, n);
   cout << "Array after Sorting: ";
   display(arr, n);
   return 0;
}


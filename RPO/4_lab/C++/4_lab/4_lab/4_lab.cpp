#include <iostream>
using namespace std;


int count_even(int arr[], int size){


        int count = 0;

        for (int i = 0; i < size; i++) {
            if (arr[i] % 2 == 0) 
                count++;
            
        }
        return count;
    }

int factorinal(int num) {
    if (num <= 1) return 1;
    return num * factorinal(num - 1);
    }

int fibonachy(int num) {
    if (num < 1) return 0;
    if (num == 1) return 1;
    return fibonachy(num - 1) + fibonachy(num - 2);
}

int main() {
    int arr[] = {9, 1, 5, 1 ,22, 623, 3, 32 };
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << "count even number in array: " << count_even(arr, size) << endl;
    cout << "factorial 5: " << factorinal(5) << endl;
    cout << "fibonachy 5: " << fibonachy(8) << endl;


}
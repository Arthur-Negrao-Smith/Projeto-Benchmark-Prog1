#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubble_sort (int arr[], int n, int *comparisons, int *swaps){
    *comparisons = 0;
    *swaps = 0;
    for (int i = 0; i<n-1; i++) {
        for (int j = 0; j<n-i-1; j++) {
            (*comparisons)++;
            if (arr[j]>arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                (*swaps)++;
            }
        }
    }
}
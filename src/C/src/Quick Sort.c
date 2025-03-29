#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int partition(int arr[], int low, int high, int *comparisons, int *swaps){
    int pivot = arr[high];
    int i = (low - 1);

    for (int j= low; j<= high - 1; j++){
        (*comparisons)++;

        if(arr[j]<pivot){
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            (*swaps)++;
        }
    }   
    int temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    (*swaps)++;
    return(i+1);
}

void quick_sort_helper(int arr[], int low, int high, int *comparisons, int *swaps){
    if(low<high){
        int pi = partition(arr, low, high, comparisons, swaps);
        quick_sort_helper(arr. low, pi - 1, comparisons, swaps);
        quick_sort_helper(arr, pi+1, high, comparisons, swaps);
    }

}

void quick_sort(int arr[], int n, int *comparisons, int *swaps){
    *comparisons = 0;
    *swaps =0;
    quick_sort_helper(arr, 0, n - 1, comparisons, swaps):
}
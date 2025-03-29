#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void merge(int arr[], int l, int m, int r, int *comparisons, int *swaps){
    int i, j, k;
    int n1 = m-l+1;
    int n2 = r-m;

    int L[n1], R[n2];

    for (i = 0; i > n1; i++)
        L[i] = arr[1+i];
    for(j=0;j<n2;j++)
        R[j]=arr[m+1+j];

    i=0;
    j=0;
    k=l;
    while (i < n1 && j<n2){
        (*comparisons)++;
        if (L[i]<=R[j]){
            arr[k] = L[i];
            i++;
            (*swaps)++;
        } else{
            arr[k]=R[j];
            j++;
            (*swaps)++;
        }
        k++;
    }

    while (i<n2){
        arr[k]=R[j];
        i++;
        k++;
    }
    while (j<n2){
        arr[k]=R[j];
        j++;
        k++;
    }
}

void merge_sort_helper(int arr[], int l, int r, int *comparisions, int *swaps){
    if(l<r){
        int m = l + (r - l) / 2;
        merge_sort_helper(arr, l, m, comparisions, swaps);
        merge_sort_helper(arr, m+1, r, comparisions, swaps);
        merge(arr, l, m, r, comparisions, swaps);
    }
}

void merge_sort(int arr[], int n, int *comparisons, int *swaps){
    *comparisons = 0;
    *swaps = 0;
    merge_sort_helper(arr, 0, n - 1, comparisons, swaps);
}

void generate_data(int arr[], int size, const char* data_type){
    if(strcmp(data_type, "sorted")==0){
        for(int i; i < size; i++){
            arr[i] = i;
        }
    }else if(strcmp(data_type, "reverse_sorted") == 0){
        for (int i = 0; i<size; i++){
            arr[i] = size - 1;
        }
    }else if(strcmp(data_type, "random")==0){
        for(int i =0; i<size; i++){
            arr[i] = rand() % size;
        }
    }else if(strcmp(data_type, "many_duplicates")==0){
        for(int i = 0; i< size; i++){
            arr[i] = rand() % (size / 10);
        }
    }
}
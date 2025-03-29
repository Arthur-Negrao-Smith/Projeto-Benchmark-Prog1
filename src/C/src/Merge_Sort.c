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

void test_merge_sort() {
    int sizes[] = {1000, 10000, 100000, 1000000};
    const char* data_types[] = {"sorted", "reverse_sorted", "random", "many_duplicates"};
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types)/sizeof(data_types[0]);

    printf("Merge Sort Performance Test\n");
    printf("Size\tData Type\t\tTime (s)\tComparisons\tSwaps\n");
    printf("------------------------------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++) {
            int size = sizes[i];
            int* arr = (int*)malloc(size * sizeof(int));
            generate_data(arr, size, data_types[j]);

            int comparisons, swaps;
            clock_t start = clock();
            merge_sort(arr, size, &comparisons, &swaps);
            clock_t end = clock();
            double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

            printf("%d\t%-16s\t%.6f\t%d\t\t%d\n", 
                   size, data_types[j], time_taken, comparisons, swaps);

            free(arr);
        }
    }
}
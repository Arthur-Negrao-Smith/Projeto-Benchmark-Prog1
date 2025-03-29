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
    quick_sort_helper(arr, 0, n - 1, comparisons, swaps);
}

void generate_data(int arr[], int size, const char* data_type){
    if (strcmp(data_type, "sorted") == 0) {
        for (int i = 0; i < size; i++) {
            arr[i] = i;
        }
    } else if (strcmp(data_type, "reverse_sorted") == 0) {
        for (int i = 0; i < size; i++) {
            arr[i] = size - i;
        }
    } else if (strcmp(data_type, "random") == 0) {
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % size;
        }
    } else if (strcmp(data_type, "many_duplicates") == 0) {
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % (size / 10);
        }
    }
}

void test_quick_sort(){
    int sizes[] = {100, 10000, 100000, 1000000};
    const char* data_types[] = {"sorted", "reversed_sorted", "random", "many_duplicates"};
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types)/sizeof(data_types[0]);

    printf("Quick Sort Performance Test\n");
    printf("Size\tData Type\t\tTime (s)\tComparisons\tSwaps\n");
    printf("------------------------------------------------------------\n");

    for (int i= 0; i<num_sizes; i++){
        for (int j = 0; j<num_types; j++){
            int size = sizes[i];
            int* arr = (int*)malloc(size * sizeof(int));
            generate_data(arr, size, data_types[j]);

            int comparisions, swaps;
            clock_t start = clock();
            quick_sort(arr, size, data_types[j]);
            clock_t end = clock();
            double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

            printf("%d\t%-16s\t%.6f\t%d\t\t%d\n", 
                   size, data_types[j], time_taken, comparisions, swaps);

            free(arr);
        }

    }
}

#include "../include/benchmark.h"

void generate_data(int arr[], int size, const char* data_type) {
    if (strcmp(data_type, "sorted") == 0) {
        for (int i = 0; i < size; i++) arr[i] = i;
    } else if (strcmp(data_type, "reverse_sorted") == 0) {
        for (int i = 0; i < size; i++) arr[i] = size - i;
    } else if (strcmp(data_type, "random") == 0) {
        for (int i = 0; i < size; i++) arr[i] = rand() % size;
    } else if (strcmp(data_type, "many_duplicates") == 0) {
        for (int i = 0; i < size; i++) arr[i] = rand() % (size/10);
    }
}

void write_to_csv(FILE *file, const char *algorithm, const char *data_type, 
                 int size, double time_taken, long steps) {
    fprintf(file, "%s_%s_%d,%.6f,%ld\n", 
            algorithm, data_type, size, time_taken, steps);
}

void test_sort_algorithm(void (*sort_func)(int[], int, int*, int*), 
                        const char *algorithm_name,
                        int sizes[], int num_sizes, 
                        const char *data_types[], int num_types) {
    
    FILE *csv_file = fopen("../results/benchmark_c.csv", "a");
    if (!csv_file) {
        printf("Erro ao abrir o arquivo CSV!\n");
        return;
    }
    
    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++) {
            int size = sizes[i];
            int* arr = (int*)malloc(size * sizeof(int));
            if (!arr) {
                printf("Falha ao alocar memória para size=%d\n", size);
                continue;
            }
            
            generate_data(arr, size, data_types[j]);

            int comparisons, swaps;
            clock_t start = clock();
            sort_func(arr, size, &comparisons, &swaps);
            clock_t end = clock();
            
            double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
            long steps = comparisons + swaps;

            write_to_csv(csv_file, algorithm_name, data_types[j], size, 
                        time_taken, steps);

            free(arr);
        }
    }
    fclose(csv_file);
}
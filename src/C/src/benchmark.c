#include "benchmark.h"
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Will generate data to all array
void generate_data(long int arr[], long int size, const char* data_type) {
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

BenchMetrics *create_BenchMetrics(char label[MAX_STRING_SIZE])
{
    BenchMetrics *metrics = (BenchMetrics*) malloc(sizeof(BenchMetrics));
    metrics->steps = 0;
    metrics->memory_usage = 0;
    metrics->execution_time = 0;
    strcpy(metrics->label, label);
    metrics->label[49] = '\0';

    return metrics;
}

// Will write BenchMetrics in csv file
short int write_to_csv(FILE *file, BenchMetrics *metrics) {
    fprintf(file, "%s,%lf,%lld,%lld\n", metrics->label, metrics->execution_time, metrics->memory_usage, metrics->steps);
    return 0;
}

void test_sort_algorithm(void (*sort_func)(long int*, long int, BenchMetrics*), 
                        const char *algorithm_name,
                        long int sizes[], int num_sizes, 
                        const char *data_types[], long int num_types) {
    
    FILE *csv_file = fopen("../results/benchmark_c.csv", "a");
    if (!csv_file) {
        printf("Erro ao abrir o arquivo CSV!\n");
        return;
    }
    
    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++) {
            long int size = sizes[i];
            long int* arr = (long int*)malloc(size * sizeof(long int));
            if (!arr) {
                printf("Falha ao alocar memória para size=%ld\n", size);
                continue;
            }
            
            generate_data(arr, size, data_types[j]);

            char label[MAX_STRING_SIZE] = "Test Sort Algorithm";
            BenchMetrics *metrics = create_BenchMetrics(label);
            clock_t start = clock();
            sort_func(arr, size, metrics);
            clock_t end = clock();
            
            metrics->execution_time = ((double)(end - start)) / CLOCKS_PER_SEC;
            strcpy(metrics->label, algorithm_name);
            metrics->memory_usage = 0;
            
            write_to_csv(csv_file, metrics);

            free(arr);
            free(metrics);
        }
    }
    fclose(csv_file);
}

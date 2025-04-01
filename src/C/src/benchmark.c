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

BenchMetrics *create_BenchMetrics(char algorithm_name[MAX_ALGORITHM_NAME_SIZE], char data_type[MAX_DATA_TYPE_SIZE], long int array_size)
{
    BenchMetrics *metrics = (BenchMetrics*) malloc(sizeof(BenchMetrics));

    metrics->array_size = array_size;
    metrics->steps = 0;
    metrics->memory_usage = 0;
    metrics->execution_time = 0;

    strcpy(metrics->algorithm_name, algorithm_name);
    metrics->algorithm_name[MAX_ALGORITHM_NAME_SIZE-1] = '\0';
    strcpy(metrics->data_type, data_type);
    metrics->algorithm_name[MAX_DATA_TYPE_SIZE-1] = '\0';

    return metrics;
}

// Will write BenchMetrics in csv file
short int write_to_csv(FILE *file, BenchMetrics *metrics) {
    fprintf(file, "%s,%s,%ld,%lf,%lld,%lld\n", metrics->algorithm_name,metrics->data_type, metrics->array_size, metrics->execution_time, metrics->memory_usage, metrics->steps);
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

            char algorithm_name_metrics[MAX_ALGORITHM_NAME_SIZE];
            strcpy(algorithm_name_metrics, algorithm_name);
            char data_type[MAX_DATA_TYPE_SIZE];
            strcpy(data_type, data_types[j]);
            BenchMetrics *metrics = create_BenchMetrics(algorithm_name_metrics, data_type, size);

            clock_t start = clock();
            sort_func(arr, size, metrics);
            clock_t end = clock();
            
            metrics->execution_time = ((double)(end - start)) / CLOCKS_PER_SEC;
            metrics->memory_usage = 0;
            
            write_to_csv(csv_file, metrics);

            free(arr);
            free(metrics);
        }
    }
    fclose(csv_file);
}

#include "benchmark.h"
#include <stdlib.h>
#include <string.h>
#include <time.h>
#if defined(_WIN32) || defined(_WIN64)
    #define WIN32_LEAN_AND_MEAN
    #include <windows.h>
    #include <psapi.h>
#else
    #include <unistd.h>
#endif

// Will generate data to all array
void generate_data(long int arr[], long int size, const char* data_type) {
    if (strcmp(data_type, FIRST_ORDER) == 0) {
        for (int i = 0; i < size; i++) arr[i] = i;
    } else if (strcmp(data_type, SECOND_ORDER) == 0) {
        for (int i = 0; i < size; i++) arr[i] = size - i;
    } else if (strcmp(data_type, THIRD_ORDER) == 0) {
        for (int i = 0; i < size; i++) arr[i] = rand() % size;
    } else if (strcmp(data_type, FOURTH_ORDER) == 0) {
        for (int i = 0; i < size; i++) arr[i] = rand() % (size/10);
    }
}


void swap(long int *a, long int *b)
{
    long int t = *a;
    *a = *b;
    *b = t;
}


void print_array(long int array[], long int size, int items_per_line)
{
    printf("[ ");
    for (int i = 0; i < size; i++)
    {
        if (i % 20 != items_per_line)
            printf("%ld, ", array[i]);
        else
            printf("\n%ld, ", array[i]);
    }
    printf(" ]\n");
}


BenchMetrics *create_BenchMetrics(char algorithm_name[MAX_ALGORITHM_NAME_SIZE], char data_type[MAX_DATA_TYPE_SIZE], long int array_size)
{
    BenchMetrics *metrics = (BenchMetrics*) malloc(sizeof(BenchMetrics));

    if (metrics)
    {
        metrics->array_size = array_size;
        metrics->comparations = 0;
        metrics->swaps = 0;
        metrics->memory_usage = 0;
        metrics->execution_time = 0;

        strncpy(metrics->algorithm_name, algorithm_name, MAX_ALGORITHM_NAME_SIZE);
        metrics->algorithm_name[MAX_ALGORITHM_NAME_SIZE-1] = '\0';
        strncpy(metrics->data_type, data_type, MAX_DATA_TYPE_SIZE);
        metrics->data_type[MAX_DATA_TYPE_SIZE-1] = '\0';
    }

    return metrics;
}


void free_BenchMetrics_array(BenchMetrics *benchmetrics_array[TOTAL_METRICS_POSSIBLES])
{
    for (int i = 0; i < TOTAL_METRICS_POSSIBLES; i++)
    {
        free(benchmetrics_array[i]);
        benchmetrics_array[i] = NULL;
    }
}


// Will write BenchMetrics in csv file
short int write_to_csv(BenchMetrics *metrics) {
    char system[MAX_STRING_SYSTEM_SIZE];
    char path[MAX_STRING_PATH_SIZE];

    #if defined(_WIN32)
        strncpy(system, WINDOWS, MAX_STRING_SYSTEM_SIZE);
        system[MAX_STRING_SYSTEM_SIZE-1] = '\0';
        strncpy(path, WINDOWS_PATH, MAX_STRING_PATH_SIZE);
        path[MAX_STRING_PATH_SIZE-1] = '\0';
    #else
        strncpy(system, LINUX, MAX_STRING_SYSTEM_SIZE);
        system[MAX_STRING_SYSTEM_SIZE-1] = '\0';
        strncpy(path, LINUX_PATH, MAX_STRING_PATH_SIZE);
        path[MAX_STRING_PATH_SIZE-1] = '\0';
    #endif

    strncat(path, metrics->algorithm_name, MAX_STRING_PATH_SIZE-1);
    path[MAX_STRING_PATH_SIZE-1] = '\0';
    strncat(path, "-c.csv", MAX_STRING_PATH_SIZE-1);
    path[MAX_STRING_PATH_SIZE-1] = '\0';
    printf("%s\n", path);

    FILE *file = fopen(path, "r");
    if (file) {
        fclose(file);
        file = fopen(path, "a");
    } else {
        file = fopen(path, "a");
        fprintf(file, "%s", HEADER_OF_CSV);
    }
    
    fprintf(file, "%s,%s,%ld,%lf,%lld,%lld,%lld\n", metrics->algorithm_name,metrics->data_type, metrics->array_size, metrics->execution_time, metrics->memory_usage, metrics->comparations, metrics->swaps);
    fclose(file);
    return 0;
}

void write_BenchMetrics_array_to_csv(BenchMetrics *array[TOTAL_METRICS_POSSIBLES])
{
    char algorithm_name[MAX_ALGORITHM_NAME_SIZE];
    strncpy(algorithm_name, array[0]->algorithm_name, MAX_ALGORITHM_NAME_SIZE);
    algorithm_name[MAX_ALGORITHM_NAME_SIZE-1] = '\0';

    for (int i = 0; i < TOTAL_METRICS_POSSIBLES; i++)
        write_to_csv(array[i]);
}

long long int get_sort_memory_usage(long int size, const char* algorithm_name) {
    const long int element_size = sizeof(long int); // 8 bytes em sistemas 64-bit
    long long base_memory = size * element_size;

    // Fatores empíricos (ajuste conforme necessidade)
    if (strcmp(algorithm_name, MERGE_NAME) == 0) {
        return base_memory * 1.8;  // Merge Sort usa array auxiliar
    } 
    else if (strcmp(algorithm_name, QUICK_NAME) == 0) {
        return base_memory * 1.3;  // Quick Sort tem overhead de recursão
    }
    else { // Bubble Sort e outros in-place
        return base_memory * 1.05; // +5% para variáveis temporárias
    }
}
#include "benchmark.h"
#include "bubble_sort.h"
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char algorithm_name[MAX_ALGORITHM_NAME_SIZE] = "Teste Algoritmo";
    char data_type[MAX_DATA_TYPE_SIZE] = "Teste tipo";
    long int size = FIRST_SIZE;
    BenchMetrics *metrics = create_BenchMetrics(algorithm_name, data_type, size);
    printf("Nome do algoritmo: %s\tNome do tipo: %s\tTamanho do array: %ld\n", metrics->algorithm_name, metrics->data_type, metrics->array_size);
    free(metrics);

    // Tests
    BenchMetrics *benchmetrics_array[TOTAL_METRICS_POSSIBLES];
    benchmark_bubble_sort(benchmetrics_array);
    printf("\nTeste do array de dados:\n");
    printf("1. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array[0]->algorithm_name,
        benchmetrics_array[0]->data_type,
        benchmetrics_array[0]->array_size
    );
    printf("2. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array[1]->algorithm_name,
        benchmetrics_array[1]->data_type,
        benchmetrics_array[1]->array_size
    );

    free_BenchMetrics_array(benchmetrics_array);
    return 0;
}

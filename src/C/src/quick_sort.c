#include "benchmark.h"
#include "quick_sort.h"
#include <stdio.h>   //para funções de entrada/saída (printf, etc.)
#include <stdlib.h>  //para alocação de memória (malloc, free) e números aleatórios (rand)
#include <time.h>    //para medir tempo de execução (clock()) e gerar sementes aleatórias (time)
#include <string.h>  //para comparar strings (strcmp)



/* Função de partição para o Quick Sort (esquema de Lomuto*/
int partition(long int arr[], long int low, long int high, BenchMetrics *metrics) {
    long int pivot = arr[high]; //seleciona o último elemento como pivô
    
    while (low < high)
    {
        while (low < high && arr[low] <= pivot)
        {
            low++;
            metrics->comparations++;
        }
        
        while (low < high && arr[high] > pivot)
        {
            high--;
            metrics->comparations++;
        }

        swap(&arr[low], &arr[high]);
        metrics->swaps++;
    }
    return low;
}

/* Função principal do Quick Sort*/
void quick_sort(long int arr[], long int low, long int high, BenchMetrics *metrics) {
    if (low < high)
    {
        int pos = partition(arr, low, high, metrics);
        quick_sort(arr, low, pos - 1, metrics);
        quick_sort(arr, pos, high, metrics);
    }
}


/* Função que testa o Quick Sort com diferentes configurações */
BenchMetrics **benchmark_quick_sort(BenchMetrics *benchmetrics_array[TOTAL_METRICS_POSSIBLES]) {
    //tamanhos de arrays para teste
    int sizes[] = {FIRST_SIZE, SECOND_SIZE, THIRD_SIZE, FOURTH_SIZE};
    // Tipos de dados para teste
    const char* data_types[] = {FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER};
    
    //calcula quantos tamanhos e tipos de dados existem
    long int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    long int num_types = sizeof(data_types)/sizeof(data_types[0]);

    //cabeçalho dos resultados
    printf("Quick Sort Performance Test\n");
    printf("Size\tData Type\t\tTime (s)\tComparations\t\tSwaps\n");
    printf("---------------------------------------------------------------------------------------\n");

    // Counter
    short int counter = 0;

    //testa para cada combinação de tamanho e tipo de dados
    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++) {
            long int size = sizes[i];
            //aloca memória para o array
            long int* arr = (long int*)malloc(size * sizeof(long int));
            
            //gera dados conforme o tipo atual
            generate_data(arr, size, data_types[j]);

            char algorithm_name[MAX_ALGORITHM_NAME_SIZE] = QUICK_NAME;
            char data_type[MAX_DATA_TYPE_SIZE];
            strncpy(data_type, data_types[j], MAX_DATA_TYPE_SIZE);
            data_type[MAX_DATA_TYPE_SIZE-1] = '\0';
            BenchMetrics *metrics = create_BenchMetrics(algorithm_name, data_type, size); //variável para métricas

            clock_t start = clock(); //marca o tempo inicial
            quick_sort(arr, 0, size-1, metrics); // Executa a ordenação
            clock_t end = clock();//marca o tempo final
            
            //calcula o tempo decorrido em segundos
            metrics->execution_time = ((double)(end - start)) / CLOCKS_PER_SEC;

            //imprime resultados formatados
            printf("%ld\t%-16s\t%.6f\t  %lld\t\t%lld\n",
            size, data_types[j], metrics->execution_time, metrics->comparations, metrics->swaps);

            //libera memória alocada
            free(arr);
            benchmetrics_array[counter] = metrics;
            counter++;
        }
    }
    return benchmetrics_array;
}

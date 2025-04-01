#include "benchmark.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


//simplementação do Bubble Sort
//recebe: array, tamanho do array, ponteiros para contadores de comparações e trocas
void bubble_sort (long int *arr, long int array_size, BenchMetrics *metrics){
    //loop externo: passa por todos os elementos
    for (int i = 0; i < array_size -1; i++) {
        //loop interno: compara elementos adjacentes
        for (int j = 0; j < array_size -i -1; j++) {
            (metrics->steps)++; //incrementa contador de comparações
            //se o elemento atual for maior que o próximo, troca eles
            if (arr[j]>arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                (metrics->steps)++; //incrementa contador de trocas
            }
        }
    }
}

//função que testa o Bubble Sort com diferentes configurações
BenchMetrics **benchmark_bubble_sort(BenchMetrics *benchmetrics_array[TOTAL_METRICS_POSSIBLES]){

    //tamanhos de arrays para teste
        long int sizes[] = {FIRST_SIZE, SECOND_SIZE, THIRD_SIZE, FOURTH_SIZE};

    // Tipos de dados para teste
    const char* data_types[] = {FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER};

    //calcula quantos tamanhos e tipos existem
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types) / sizeof(data_types[0]);

    //cabeçalho dos resultados
    printf("Bubble Sort Performance Test\n");
    printf("Size\tData Type\t\tTime (s)\tSteps\n");
    printf("--------------------------------------------------------------\n");

    // Counter
    short int counter = 0;

    //testa para cada combinação de tamanho e tipo de dados
    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++){
            long int size = sizes[i];

            //aloca memória para o array
            long int* arr = (long int*)malloc(size * sizeof(long int));

            //gera dados conforme o tipo atual
            generate_data(arr, size, data_types[j]);

            char algorithm_name[MAX_ALGORITHM_NAME_SIZE] = "bubble_sort";
            char data_type[MAX_DATA_TYPE_SIZE];
            strncpy(data_type, data_types[j], MAX_DATA_TYPE_SIZE);
            data_type[MAX_DATA_TYPE_SIZE-1] = '\0';
            BenchMetrics *metrics = create_BenchMetrics(algorithm_name, data_type, size); //variável para métricas

            clock_t start = clock(); //marca tempo inicial
            bubble_sort(arr, size, metrics); //executa ordenação
            clock_t end = clock(); //marca tempo final
            metrics->execution_time = ((double)(end - start)) / CLOCKS_PER_SEC; //calcula tempo decorrido em segundos
            
            //imprime resultados formatados
            printf("%ld\t%-16s\t%.6f\t%lld\n",
            size, data_types[j], metrics->execution_time, metrics->steps);

            //libera memória alocada
            free(arr);
            benchmetrics_array[counter] = metrics;
            counter++;
        }
    }
    return benchmetrics_array;
}

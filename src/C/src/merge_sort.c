#include "benchmark.h"
#include "merge_sort.h"
#include <stdio.h>   // Para funções de entrada/saída (printf, etc.)
#include <stdlib.h>  // Para alocação de memória (malloc, free) e rand()
#include <time.h>    // Para medir tempo de execução (clock()) e gerar números aleatórios (time())
#include <string.h>  // Para comparar strings (strcmp())



/*
função que combina dois subarrays ordenados em um único array ordenado
   parâmetros:
   -arr[]: Array principal que será ordenado
   -l: Índice inicial do subarray esquerdo
   -m: Índice do meio (fim do subarray esquerdo)
   -r: Índice final do subarray direito
   -metrics: BenchMetrics to storage BenchMark data
*/
void merge(long int arr[], int l, int m, int r, BenchMetrics *metrics) {
    int i, j, k;
    int n1 = m - l + 1;  //tamanho do subarray esquerdo
    int n2 = r - m;//tamanho do subarray direito

    //arrays temporários para armazenar as metades
    long int *L = malloc(n1 * sizeof(long int));
    long int *R = malloc(n2 * sizeof(long int));

    //copia os dados para os arrays temporários
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];  //correção: alterado de arr[1+i] para arr[l+i]
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Combina os arrays temporários de volta no array principal
    i = 0;  //indice inicial do subarray esquerdo
    j = 0;  //indice inicial do subarray direito
    k = l;  //indice inicial do array combinado
    
    while (i < n1 && j < n2) {
        (metrics->comparations)++;  //incrementa o contador de comparações
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
            (metrics->swaps)++;//incrementa o contador de trocas
        }
        k++;
    }

    //copia os elementos restantes do subarray esquerdo, se houver
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    //copia os elementos restantes do subarray direito, se houver
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}


/*
função auxiliar recursiva que implementa o Merge Sort
   parâmetros:
   -arr[]: Array a ser ordenado
   -l: Índice inicial
   -r: Índice final
   -metrics: BenchMetrics to storage BenchMark data
*/
void merge_sort_helper(long int arr[], int l, int r, BenchMetrics *metrics) {
    if (l < r) {
        //encontra o ponto médio para dividir o array
        int m = l + (r - l) / 2;
        
        //ordena primeira e segunda metades
        merge_sort_helper(arr, l, m, metrics);
        merge_sort_helper(arr, m + 1, r, metrics);
        
        //combina as metades ordenadas
        merge(arr, l, m, r, metrics);
    }
}


/*
função principal do Merge Sort que inicia o processo de ordenação
   parametros:
   -arr[]: Array a ser ordenado
   -n: Tamanho do array
   -metrics: BenchMetrics to storage data
*/
void merge_sort(long int arr[], long int n, BenchMetrics *metrics) {
    merge_sort_helper(arr, 0, n - 1, metrics);  //chama a função auxiliar
}


// função que testa o Merge Sort com diferentes configurações
BenchMetrics **benchmark_merge_sort(BenchMetrics *benchmetrics_array[TOTAL_METRICS_POSSIBLES]) {
    //tamanhos de arrays para teste
    int sizes[] = {FIRST_SIZE, SECOND_SIZE, THIRD_SIZE, FOURTH_SIZE};
    //tipos de dados para teste
    const char* data_types[] = {FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER};
    
    //calcula quantos tamanhos e tipos de dados existem
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types)/sizeof(data_types[0]);

    //cabeçalho dos resultados
    printf("Merge Sort Performance Test\n");
    printf("Size\tData Type\t\tTime (s)\tComparations\t\tSwaps\n");
    printf("---------------------------------------------------------------------------------------\n");

    short int counter = 0;

    //testa para cada combinação de tamanho e tipo de dados
    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++) {
            long int size = sizes[i];
            //aloca memória para o array
            long int* arr = (long int*)malloc(size * sizeof(long int));
            
            //gera dados conforme o tipo atual
            generate_data(arr, size, data_types[j]);


            char algorithm_name[MAX_ALGORITHM_NAME_SIZE] = MERGE_NAME;
            char data_type[MAX_DATA_TYPE_SIZE];
            strncpy(data_type, data_types[j], MAX_DATA_TYPE_SIZE);
            data_type[MAX_DATA_TYPE_SIZE-1] = '\0';
            BenchMetrics *metrics = create_BenchMetrics(algorithm_name, data_type, size); //variável para métricas

            clock_t start = clock();//marca o tempo inicial
            merge_sort(arr, size, metrics);//executa a ordenação
            clock_t end = clock();   //marca o tempo final
            
            //calcula o tempo decorrido em segundos
            metrics->execution_time = ((double)(end - start)) / CLOCKS_PER_SEC;

            //imprime resultados formatados
            printf("%ld\t%-16s\t%.6f\t  %lld\t\t%lld\n",
            size, data_types[j], metrics->execution_time, metrics->comparations, metrics->swaps);

            free(arr);
            benchmetrics_array[counter] = metrics;
            counter++;
        }
    }
    write_BenchMetrics_array_to_csv(benchmetrics_array);
    return benchmetrics_array;
}

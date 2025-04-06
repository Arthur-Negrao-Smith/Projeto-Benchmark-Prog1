#include "benchmark.h"
#include "bubble_sort.h"
#include "merge_sort.h"
#include "quick_sort.h"
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Tests with Merge Sorte
    BenchMetrics *benchmetrics_array_merge[TOTAL_METRICS_POSSIBLES];
    benchmark_merge_sort(benchmetrics_array_merge);
    printf("\nTeste do array de dados: Merge\n");
    printf("1. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array_merge[0]->algorithm_name,
        benchmetrics_array_merge[0]->data_type,
        benchmetrics_array_merge[0]->array_size
    );
    printf("2. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array_merge[1]->algorithm_name,
        benchmetrics_array_merge[1]->data_type,
        benchmetrics_array_merge[1]->array_size
    );
    
    
    free_BenchMetrics_array(benchmetrics_array_merge);
    
    // Tests with Quick Sorte
    BenchMetrics *benchmetrics_array_quick[TOTAL_METRICS_POSSIBLES];
    benchmark_quick_sort(benchmetrics_array_quick);
    printf("\nTeste do array de dados: Quick\n");
    printf("1. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array_quick[0]->algorithm_name,
        benchmetrics_array_quick[0]->data_type,
        benchmetrics_array_quick[0]->array_size
    );
    printf("2. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array_quick[1]->algorithm_name,
        benchmetrics_array_quick[1]->data_type,
        benchmetrics_array_quick[1]->array_size
    );
    
    free_BenchMetrics_array(benchmetrics_array_quick);
    

    // Tests with Bubble Sort
    BenchMetrics *benchmetrics_array_bubble[TOTAL_METRICS_POSSIBLES];
    benchmark_bubble_sort(benchmetrics_array_bubble);
    printf("\nTeste do array de dados: Bubble\n");
    printf("1. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array_bubble[0]->algorithm_name,
        benchmetrics_array_bubble[0]->data_type,
        benchmetrics_array_bubble[0]->array_size
    );
    printf("2. Nome do algoritmo: %s\tNome do tipo: %s\t\tTamanho do array: %ld\n", 
        benchmetrics_array_bubble[1]->algorithm_name,
        benchmetrics_array_bubble[1]->data_type,
        benchmetrics_array_bubble[1]->array_size
    );
    
    free_BenchMetrics_array(benchmetrics_array_bubble);


    return 0;
}

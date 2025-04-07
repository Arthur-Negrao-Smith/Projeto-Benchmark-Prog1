#include "benchmark.h"
#include "bubble_sort.h"
#include "merge_sort.h"
#include "quick_sort.h"
#include <stdio.h>

int main()
{
    // Tests with Merge Sorte
    BenchMetrics *benchmetrics_array_merge[TOTAL_METRICS_POSSIBLES];
    benchmark_merge_sort(benchmetrics_array_merge);
    printf("\n");
    free_BenchMetrics_array(benchmetrics_array_merge);
    
    
    // Tests with Quick Sorte
    BenchMetrics *benchmetrics_array_quick[TOTAL_METRICS_POSSIBLES];
    benchmark_quick_sort(benchmetrics_array_quick);
    printf("\n");
    free_BenchMetrics_array(benchmetrics_array_quick);
    

    // Tests with Bubble Sort
    BenchMetrics *benchmetrics_array_bubble[TOTAL_METRICS_POSSIBLES];
    benchmark_bubble_sort(benchmetrics_array_bubble);
    printf("\n");
    free_BenchMetrics_array(benchmetrics_array_bubble);


    return 0;
}

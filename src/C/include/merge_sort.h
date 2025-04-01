#ifndef MERGE_SORT_H
    #define MERGE_SORT_H

    #include "benchmark.h"

    void merge(long int[], int, int , int, BenchMetrics*);
    void merge_sort_helper(long int[], int, int, BenchMetrics*);
    void merge_sort(long int[], long int, BenchMetrics*);
    BenchMetrics **benchmark_merge_sort(BenchMetrics*[TOTAL_METRICS_POSSIBLES]);

#endif
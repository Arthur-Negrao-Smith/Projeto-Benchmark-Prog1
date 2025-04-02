#ifndef QUICK_SORT_H
    #define QUICK_SORT_H

    #include "benchmark.h"



    int partition(long int[], long int, long int, BenchMetrics*);

    void quick_sort_helper(long int[], long int, long int, BenchMetrics*);

    void quick_sort(long int[], long int, BenchMetrics*);

    BenchMetrics **benchmark_quick_sort(BenchMetrics*[TOTAL_METRICS_POSSIBLES]);


#endif
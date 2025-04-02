#ifndef BUBBLE_SORT_H
    #define BUBBLE_SORT_H

    #include "benchmark.h"

    /// @brief Will apply bubble sort algorithm
    /// @param  arr This is the array that will be sorted
    /// @param  array_size Size of array
    /// @param  metrics BenchMetrics to storage BenchMark data
    void bubble_sort(long int*, long int, BenchMetrics*);


    /// @brief Will calculate BenchMark of the bubble sort
    /// @param benchmetrics_array Array to storage pointers to BenchMetrics
    /// @return Return Array fill with pointers to BenchMetrics
    BenchMetrics **benchmark_bubble_sort(BenchMetrics*[TOTAL_METRICS_POSSIBLES]);

#endif

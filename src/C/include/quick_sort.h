#ifndef QUICK_SORT_H
    #define QUICK_SORT_H

    #include "benchmark.h"



    /// @brief Will partition array in subarrays and order it
    /// @param arr This is the array that will be sorted
    /// @param low Init index of the list
    /// @param high Last index of the list
    /// @param metrics to storage BenchMark data
    /// @return Will return middle position of array
    int partition(long int[], long int, long int, BenchMetrics*);

    /// @brief Will apply quick sort algorithm
    /// @param arr This is the array that will be sorted
    /// @param low Init index of the list
    /// @param high Last index of the list
    /// @param metrics to storage BenchMark data
    void quick_sort(long int[], long int, long int, BenchMetrics*);

    /// @brief Will calculate BenchMark of the merge sort
    /// @param benchmetrics_array Array to storage pointers to BenchMetrics
    /// @return Return Array fill with pointers to BenchMetrics
    BenchMetrics **benchmark_quick_sort(BenchMetrics*[TOTAL_METRICS_POSSIBLES]);


#endif
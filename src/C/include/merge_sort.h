#ifndef MERGE_SORT_H
    #define MERGE_SORT_H

    #include "benchmark.h"



    /// @brief Will apply merge sort algorithm
    /// @param arr This is the array that will be sorted
    /// @param l This is first index of the subarray
    /// @param m This is middle index of the subarray
    /// @param r This is last index of the subarray
    /// @param metrics BenchMetrics to storage BenchMark data
    void merge(long int[], int, int , int, BenchMetrics*);


    /// @brief Recursive merge algorithm to partition array
    /// @param arr This is the array that will be sorted
    /// @param l This is first index of the subarray
    /// @param r This is last index of the subarray
    /// @param metrics BenchMetrics to storage BenchMark data
    void merge_sort_helper(long int[], int, int, BenchMetrics*);


    /// @brief Main Merge sort, it init the sorter process
    /// @param arr This is the array that will be sorted
    /// @param n Arraay size
    /// @param metrics to storage BenchMark data
    void merge_sort(long int[], long int, BenchMetrics*);


    /// @brief Will calculate BenchMark of the merge sort
    /// @param benchmetrics_array Array to storage pointers to BenchMetrics
    /// @return Return Array fill with pointers to BenchMetrics
    BenchMetrics **benchmark_merge_sort(BenchMetrics*[TOTAL_METRICS_POSSIBLES]);

#endif
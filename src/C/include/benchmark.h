#ifndef BENCHMARK_H
#define BENCHMARK_H

    #include <stdio.h>


    // Array sizes
    #define MAX_ALGORITHM_NAME_SIZE    20
    #define MAX_DATA_TYPE_SIZE         20
    #define TOTAL_METRICS_POSSIBLES    16

    // Size numbers
    #define FIRST_SIZE                 1000
    #define SECOND_SIZE                10000
    #define THIRD_SIZE                 100000
    #define FOURTH_SIZE                1000000

    // Data Orders
    #define FIRST_ORDER                 "sorted"
    #define SECOND_ORDER                "reverse_sorted"
    #define THIRD_ORDER                 "random"
    #define FOURTH_ORDER                "many_duplicates"

    // Algorithm's name
    #define BUBBLE_NAME                 "bubble"
    #define MERGE_NAME                  "merge"
    #define QUICK_NAME                  "quick"

    // Path to results
    #define RESULTS_PATH                "..\\..\\results\\benchmark_c.csv"



    /// @brief Struct to storage BenchMark metrics
    typedef struct BenchMetrics
    {
        long int array_size;
        long long int swaps;
        long long int comparations;
        long long int memory_usage;
        double execution_time;
        char algorithm_name[MAX_ALGORITHM_NAME_SIZE];
        char data_type[MAX_DATA_TYPE_SIZE];

    } BenchMetrics;

    /// @brief Will create a new BenchMetrics
    /// @param algorthm_name Name of algorithm
    /// @param data_type Name of data initial order 
    /// @param size Total size of array 
    /// @return BenchMetrics pointer if if everything goes well
    /// @return NULL if an error ocurred
    BenchMetrics *create_BenchMetrics(char[MAX_ALGORITHM_NAME_SIZE], char[MAX_DATA_TYPE_SIZE], long int);

    /// @brief Will generate all data in array
    /// @param arr Array to storage data 
    /// @param size Total size of the array 
    /// @param data_type Initial data order
    void generate_data(long int[], long int, const char*);

    /// @brief Will save BenchMetrics in csv file
    /// @param  file File to write data
    /// @param  metrics Metrics to storage
    /// @return 0 Returns 0 if everything goes well
    /// @return 1 Returns 1 if an error occurred
    short int write_to_csv(FILE*, BenchMetrics*);

    /// @brief Free all array
    /// @param  benchmetrics_array Array with all BenchMetrics storage
    void free_BenchMetrics_array(BenchMetrics*[TOTAL_METRICS_POSSIBLES]);
    
#endif // BENCHMARK_H

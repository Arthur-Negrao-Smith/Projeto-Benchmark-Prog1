#ifndef BENCHMARK_H
#define BENCHMARK_H

    #include <stdio.h>

    #define MAX_ALGORITHM_NAME_SIZE 20
    #define MAX_DATA_TYPE_SIZE 20
    #define TOTAL_METRICS_POSSIBLES 16
    #define FIRST_SIZE 1000
    #define SECOND_SIZE 10000
    #define THIRD_SIZE 100000
    #define FOURTH_SIZE 1000000

    typedef struct BenchMetrics
    {
        long int array_size;
        long long int steps;
        long long int memory_usage;
        double execution_time;
        char algorithm_name[MAX_ALGORITHM_NAME_SIZE];
        char data_type[MAX_DATA_TYPE_SIZE];

    } BenchMetrics;

    BenchMetrics *create_BenchMetrics(char[MAX_ALGORITHM_NAME_SIZE], char[MAX_DATA_TYPE_SIZE], long int);
    void generate_data(long int*, long int, const char*);
    short int write_to_csv(FILE*, BenchMetrics*);
    
#endif // BENCHMARK_H

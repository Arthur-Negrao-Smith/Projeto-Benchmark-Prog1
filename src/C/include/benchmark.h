#ifndef BENCHMARK_H
#define BENCHMARK_H

    #include <stdio.h>

    #define MAX_STRING_SIZE 50

    typedef struct BenchMetrics
    {
        long long int steps;
        long long int memory_usage;
        double execution_time;
        char label[MAX_STRING_SIZE];

    } BenchMetrics;

    BenchMetrics *create_BenchMetrics(char[MAX_STRING_SIZE]);
    void generate_data(long int[], long int, const char*);
    short int write_to_csv(FILE*, BenchMetrics*);
    
#endif // BENCHMARK_H

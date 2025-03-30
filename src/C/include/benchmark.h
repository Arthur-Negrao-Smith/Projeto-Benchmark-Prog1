#ifndef BENCHMARK_H
#define BENCHMARK_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void generate_data(int arr[], int size, const char* data_type);
void test_sort_algorithm(void (*sort_func)(int[], int, int*, int*), 
                        const char *algorithm_name,
                        int sizes[], int num_sizes, 
                        const char *data_types[], int num_types);

#endif // BENCHMARK_H
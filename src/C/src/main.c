#include "benchmark.h"
#include "bubble_sort.h"
#include <stdio.h>

int main()
{
    char label[MAX_STRING_SIZE] = "Teste de BenchMetrics";
    BenchMetrics *metrics = create_BenchMetrics(label);
    printf("%s", metrics->label);

    // Tests
    test_bubble_sort();
    return 0;
}

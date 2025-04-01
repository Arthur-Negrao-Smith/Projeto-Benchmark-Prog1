#include "benchmark.h"
#include "bubble_sort.h"
#include <stdio.h>

int main()
{
    BenchMetrics *metrics = create_BenchMetrics("Teste 1");
    printf("%s", metrics->label);

    // Tests
    test_bubble_sort();
    return 0;
}

# Intern imports
from .data import BenchMetrics

# Extern imports
from typing import FunctionType
import logging
from time import time
import tracemalloc as tmc


def benchmark(func: FunctionType) -> BenchMetrics:
    """
    Decorator to calculate the metrics

    Returns:
        BenchMetrics: Return all metrics calculated
    """
    def wrapper(self, *args):
        
        metrics: BenchMetrics = BenchMetrics()

        tmc.start() # Init calculate memory
        time_start: int = time() # Time of estart program

        # Run function
        function_metrics: BenchMetrics = func(self, *args)
        
        metrics.execution_time = time() - time_start # Collect total time
        metrics.memory_usage = tmc.get_traced_memory() # Collect memory usage
        tmc.stop() # Stop memory calcute

        # Update metrics
        metrics.algorithm_name = function_metrics.algorithm_name
        metrics.data_type = function_metrics.data_type
        metrics.comparations = function_metrics.comparations
        metrics.swaps = function_metrics.swaps
        
        return metrics
    return wrapper

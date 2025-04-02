# Intern imports
from .data import BenchMetrics
from types import FunctionType

# Extern imports
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
        time_start: int = time() # time of estart program

        function_metrics: BenchMetrics = func(self, *args) # function
        
        metrics.execution_time = time() - time_start # Collect total time
        metrics.memory_usage = tmc.get_traced_memory() # collect memory usage
        tmc.stop() # Stop memory calcute

        metrics.label = function_metrics.label
        metrics.comparations = function_metrics.comparations
        metrics.swaps = function_metrics.swaps
        
        return metrics
    return wrapper

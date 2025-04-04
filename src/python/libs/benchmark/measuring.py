import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Intern imports
from src.python.libs.benchmark.data import BenchMetrics

# Extern imports
from types import FunctionType
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
        metrics.list_size = function_metrics.list_size
        metrics.comparations = function_metrics.comparations
        metrics.swaps = function_metrics.swaps
        
        return metrics
    return wrapper

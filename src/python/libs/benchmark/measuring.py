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
        metrics.steps = function_metrics.steps
        
        return metrics
    return wrapper


# To measure the resources
class BenchMeasuring:
    def __init__(self, data: BenchMetrics) -> None:
        self.metrics: BenchMetrics = data

    def increment_step(self) -> None:
        """
        Increments the counter by 1
        """
        self.metrics.steps += 1

    def update_memory_usage(self, memory: int) -> int:
        """
        Updates memory usage in metrics

        Args:
            memory: Total memor usage

        Returns:
            int: 0 if was all ok and -1 if erro ocurs
        """
        if memory <= 0:
            logging.warning("Memória negativa ou igual a 0 tentou ser adicionada às métricas. Não foi atualizado memory_usage")
            return -1
        
        self.metrics.memory_usage = memory
        return 0

    def add_a_label(self, label: str) -> str:
        """
        Add a label in metrics

        Args:
            label (required): Label of metrics
        
        Returns:
            str: Return actual label
        """
        if label == None:
            logging.warning("Tentou-se adicionar um nome None: Label não foi alterada")
            return self.metrics.label
        
        self.metrics.label = label

        return self.metrics.label
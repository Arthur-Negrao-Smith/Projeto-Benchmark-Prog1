# Intern imports
from .data import BenchMatrics
from types import FunctionType

# Extern imports
import logging
from time import time
from tracemalloc import start, stop

def Benchmark(func: FunctionType) -> BenchMatrics:
    def wrapper(*args):
        start() # Init calculate memory


# To measure the resources
class BenchMeasuring:
    def __init__(self, data: BenchMatrics) -> None:
        self.metrics: BenchMatrics = data

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
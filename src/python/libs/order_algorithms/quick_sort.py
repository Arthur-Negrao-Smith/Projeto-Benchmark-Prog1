from os import getcwd
from sys import path, platform

python_path: str = getcwd()
if platform == "win32":
    path.append(f"{python_path}\\src\\python\\libs")
else:
    path.append(f"{python_path}/src/python/libs")


import logging

from basic_elements import ListCreator 
from benchmark.data import BenchMetrics
from benchmark.measuring import benchmark

class MergeSort(ListCreator):
    def __init__(self) -> None:
        super().__init__()
        self.steps: int = 0 # to calculate steps

    @benchmark
    def sort(self, metrics: BenchMetrics) -> BenchMetrics:
        """
        Will sort all number in the list with quick sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            BenchMetrics: All metrics updated
        """
        
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            metrics.label="Erro"
            return metrics
        
        self.merge(self.numbers_list)
        metrics.steps = self.steps # to calculate steps
        return metrics
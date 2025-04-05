import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Intern imports
from src.python.libs.order_algorithms.basic_elements import ListCreator
from src.python.libs.benchmark.data import BenchMetrics, BUBBLE_NAME, SECOND_ORDER
from src.python.libs.benchmark.measuring import benchmark

# Extern imports
import logging
from typing import Union

class BubbleSort(ListCreator):
    def __init__(self) -> None:
        super().__init__()
        self.swaps: int = 0 # Swaps counter
        self.comparations: int = 0 # Comparations counter

    @benchmark
    def benchmarkSort(self, metrics: BenchMetrics) -> Union[BenchMetrics | None]:
        """
        Will sort all number in the list with bubble sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            BenchMetrics: All metrics updated
            None: If list is empty
        """

        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            return None
             
        # Run algorithm
        self.bubbleSort()

        # Update metrics
        metrics.algorithm_name = BUBBLE_NAME
        metrics.data_type = self.data_type
        metrics.list_size = len(self.numbers_list)
        metrics.comparations = self.comparations # Update comparations on metrics
        metrics.swaps = self.swaps # Update swaps on metrics
        return metrics

    def bubbleSort(self) -> None:
        """
        Bubble sort algorithm
        """

        list_size: int = len(self.numbers_list)
        
        for i in range(list_size - 1):
            swaped: bool = False

            for j in range(list_size - 1 - i):
                self.comparations += 1

                if self.numbers_list[j] > self.numbers_list[j+1]:
                    self.swap(j, j+1)
                    swaped = True

            if not swaped:
                break

    def swap(self, a: int, b: int) -> None:
        self.numbers_list[a], self.numbers_list[b] = self.numbers_list[b], self.numbers_list[a]
        self.swaps += 1

if __name__ == "__main__":

    bubble: BubbleSort = BubbleSort()
    bubble.data_generator(1, SECOND_ORDER)

    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics = bubble.benchmarkSort(metrics)
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparations}
          Swaps: {metrics.swaps}
        """)
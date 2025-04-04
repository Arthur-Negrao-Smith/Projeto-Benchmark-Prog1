import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Intern imports
from src.python.libs.order_algorithms.basic_elements import ListCreator
from src.python.libs.benchmark.data import BenchMetrics, BUBBLE_NAME, FIRST_ORDER
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
        metrics.list_size = len(self.numbers_list)
        metrics.comparations = self.comparations # Update comparations on metrics
        metrics.swaps = self.swaps # Update swaps on metrics
        return metrics

    def bubbleSort(self) -> None:
        """
        Bubble sort algorithm
        """

        is_sorted: bool = False
        list_size: int = len(self.numbers_list)
        
        while not is_sorted:
            
            for n in range(list_size):
                   
                self.comparations += 1 # Update steps

                # If n is index of the last element
                if  n == list_size - 1:
                    is_sorted = True
                    break
                
                # Swap values
                elif self.numbers_list[n] > self.numbers_list[n+1]:
                   temp: int = self.numbers_list[n]
                   self.numbers_list[n] = self.numbers_list[n+1]
                   self.numbers_list[n+1] = temp
                   self.swaps += 1 # Update swaps counter
                   break

                # Just ignore
                elif self.numbers_list[n] <= self.numbers_list[n+1]:
                    continue

                # Debug
                else:
                    logging.warning("Comportamento inesperado no Bubble sort")
               

if __name__ == "__main__":
    
    from random import randint

    bubble: BubbleSort = BubbleSort()
    bubble.numbers_list = [randint(0, 100) for c in range(100)]

    bubble.print_list()
    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics.algorithm_name = BUBBLE_NAME
        metrics.data_type = FIRST_ORDER
        metrics = bubble.benchmarkSort(metrics)
        bubble.print_list()
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparations}
          Swaps: {metrics.swaps}
        """)
# Update path to libs
# Update path
import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Extern imports
from typing import Union
import logging

# Intern imports
from src.python.libs.order_algorithms.basic_elements import ListCreator 
from src.python.libs.benchmark.data import BenchMetrics, QUICK_NAME, SECOND_ORDER
from src.python.libs.benchmark.measuring import benchmark

class QuickSort(ListCreator):
    def __init__(self) -> None:
        super().__init__()
        self.comparations: int = 0 # to calculate comparations
        self.swaps: int = 0 # To calculate swaps

    @benchmark
    def benchmarkSort(self, metrics: BenchMetrics) -> Union[BenchMetrics | None]:
        """
        Will sort all number in the list with quick sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            BenchMetrics: All metrics updated
            None: If list is empty
        """
        
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            return None
        
        # Run Algorithm 
        self.numbers_list = self.quickSort(self.numbers_list)
        
        # Update metrics
        metrics.algorithm_name = QUICK_NAME
        metrics.data_type = self.data_type
        metrics.list_size = len(self.numbers_list)
        metrics.comparations = self.comparations # Update comparations on metrics
        metrics.swaps = self.swaps # Update swaps on metrics
        return metrics
    
    def swap(self, numbers_list: list[int], a_index: int, b_index: int) -> None:
        """
        Swap items in the list

        Args: 
            numbers_list (required): List to be swapped
            a_index (required): Index of element to be swapped
            b_index (required): Index of element to be swapped
        """
        temp: int = numbers_list[a_index]
        numbers_list[a_index] = numbers_list[b_index]
        numbers_list[b_index] = temp
        return
    
    
    def quickSort(self, numbers_list: list[int]) -> None:
        less = []
        equal = []
        greater = []

        if len(numbers_list) > 1:
            pivot = numbers_list[0]

            for x in numbers_list:
                self.comparations += 1
                
                if x < pivot:
                    self.swaps += 1
                    less.append(x)
                elif x == pivot:
                    self.swaps += 1
                    self.comparations += 1
                    equal.append(x)
                elif x > pivot:
                    self.swaps += 1
                    self.comparations += 2
                    greater.append(x)

            return self.quickSort(less)+equal+self.quickSort(greater)

        else:  
            return numbers_list

    @benchmark
    def qsortBenchmark(self, metrics: BenchMetrics) -> Union[BenchMetrics | None]:
        """
        Will sort all number in the list with quick sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            BenchMetrics: All metrics updated
        """
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            return None
        
        # Run Algorithm 
        sorted(self.numbers_list)

        # Update metrics
        metrics.comparations = -1 # Update comparations on metrics
        metrics.swaps = -1 # Update swaps on metrics
        return metrics


if __name__ == "__main__":

    quick: QuickSort = QuickSort()
    #quick.data_generator(1, 'sorted')
    print(len(quick.numbers_list))
    from random import randint
    quick.numbers_list = [randint(0, 100) for c in range(1_000)]

    #quick.print_list()
    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics = quick.benchmarkSort(metrics)
        quick.print_list()
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparations}
          Swaps: {metrics.swaps}
        """)
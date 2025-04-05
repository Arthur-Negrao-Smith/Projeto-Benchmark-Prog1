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
        self.quickSort(self.numbers_list)
        
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
        numbers_list[a_index], numbers_list[b_index] = numbers_list[b_index], numbers_list[a_index]
        self.swaps += 1
    
    def quickSort(self, numbers_list: list[int]) -> None:
        # Stack to simulate a recursion
        stack = [(0, len(numbers_list) - 1)]
    
        while stack:
            low, high = stack.pop()
        
            if low < high:
                # It will partition the array
                pivot = self.partition(numbers_list, low, high)
            
                # Stack sublists
                stack.append((low, pivot - 1))  # Left sublist
                stack.append((pivot + 1, high))  # Right sublist 

    def partition(self, numbers_list: list[int], low: int, high: int) -> int:
        pivot = numbers_list[high]
        l = low - 1 # left index
        
        for r in range(low, high): # right index
            self.comparations += 1
            if numbers_list[r] <= pivot:
                l += 1
                self.swap(numbers_list=numbers_list, a_index=l, b_index=r)
                
        self.swap(numbers_list=numbers_list, a_index=l+1, b_index=high) # return pivot to correct position
        return l + 1

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
    quick.data_generator(4, 'random')
    print(len(quick.numbers_list))
    from random import randint
    #quick.numbers_list = [randint(0, 100) for c in range(1_000)]

    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics = quick.benchmarkSort(metrics)
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparations}
          Swaps: {metrics.swaps}
        """)
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

from random import randint

class QuickSort(ListCreator):
    """Class to use Quick sort algorithm"""
    def __init__(self) -> None:
        super().__init__()
        self.comparisons: int = 0 # to calculate comparisons
        self.swaps: int = 0 # To calculate swaps

    @benchmark
    def benchmarkSort(self, metrics: BenchMetrics) -> Union[BenchMetrics | None]:
        """
        Will sort all number in the list with quick sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            Union: It will returns all metrics updated if list is not empty, else returns None
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
        metrics.comparisons = self.comparisons # Update comparisons on metrics
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
        """
        It will sort the list using the quick sort algorithm

        Args:
            numbers_list (required): List with all numbers to sorte
        """

        # Stack to simulate a recursion
        stack: list[int] = [(0, len(numbers_list) - 1)]
    
        while stack:
            left, right = stack.pop()
        
            if left < right:
                # It will partition the array
                pivot = self.partition(numbers_list, left, right)
            
                # Stack sublists
                stack.append((left, pivot - 1))  # Left sublist
                stack.append((pivot + 1, right))  # Right sublist 

    def partition(self, numbers_list: list[int], left: int, right: int) -> int:
        """
        It will partition array and returns lower index

        Args:
            numbers_list (required): List all numbers to partition
            left (required): Lower index of numbers_list
            right (required): Greater index of numbers_list

        Returns:
            int: Lower index of partition numbers_list
        """
        mid = (left + right) // 2
    
        # Getting the three values to compare: the leftmost, the middle, and the rightmost one
        left_value = numbers_list[left]
        middle_value = numbers_list[mid]
        right_value = numbers_list[right]

        # Finding the median of these three values
        # Let's make sure the pivot is the middle value between the first, middle, and last element
        if left_value > middle_value:
            if left_value < right_value:
                pivot_index = left
            elif middle_value > right_value:
                pivot_index = mid
            else:
                pivot_index = right
        else:
            if left_value > right_value:
                pivot_index = left
            elif middle_value < right_value:
                pivot_index = mid
            else:
                pivot_index = right

        # Swap pivot with the last element (right)
        self.swap(numbers_list=numbers_list, a_index=pivot_index, b_index=right)

        pivot = numbers_list[right]  # Pivot is the last element
        l = left - 1  # Left index

        for r in range(left, right):  # Right index
            self.comparisons += 1
            if numbers_list[r] <= pivot:
                l += 1
                self.swap(numbers_list=numbers_list, a_index=l, b_index=r)

        self.swap(numbers_list=numbers_list, a_index=l + 1, b_index=right)  # Returns pivot to correct position
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
        metrics.comparisons = -1 # Update comparisons on metrics
        metrics.swaps = -1 # Update swaps on metrics
        return metrics


if __name__ == "__main__":

    quick: QuickSort = QuickSort()
    quick.data_generator(2, SECOND_ORDER)

    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics = quick.benchmarkSort(metrics)
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparisons}
          Swaps: {metrics.swaps}
        """)
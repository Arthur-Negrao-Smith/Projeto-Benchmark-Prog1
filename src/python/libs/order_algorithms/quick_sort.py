# Update path to libs
from os import getcwd
from basic_elements import update_python_path
current_dir: str = getcwd()
update_python_path(current_dir)

# Extern imports
from typing import Union
import logging

# Inter imports
from basic_elements import ListCreator 
from benchmark.data import BenchMetrics, QUICK_NAME, FIRST_ORDER
from benchmark.measuring import benchmark

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
        self.quickSort(self.numbers_list, 0, len(self.numbers_list) - 1)
        
        # Update metrics
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
    
    def quickSort(self, numbers_list: list[int], left: int, right: int) -> None:
        """
        Quick sort recursive algorithm

        Args:
            numbers_list (required): List wich will be sorted
            left (required): Left index of the list
            right (required): Right index of the list
        """

        if left < right:
            partition_pos: int = self.partition(numbers_list=numbers_list, left=left, right=right) # middle position
            # Recursion of the quick sort
            self.quickSort(numbers_list=numbers_list, left=left, right=partition_pos - 1)
            self.quickSort(numbers_list=numbers_list, left=partition_pos + 1, right=right)

    def partition(self, numbers_list: list[int], left: int, right: int) -> int:
        """
        Sort partition of quicksort

        Args:
            numbers_list (required): List wich will be sorted
            left (required): Left index of the list
            right (required): Right index of the list

        Returns: 
            int: Returns left index in last position of partition
        """
        l: int = left
        r: int = right
        pivot: int = numbers_list[right]


        # To avoid unnecessary increments
        if not (l < r):
            self.comparations += 1
        while l < r:


            # To avoid unnecessary increments
            if not (l < right and numbers_list[l] < pivot):
                self.comparations += 1
            # If left index is less than right index and left element is less than pivot
            while l < right and numbers_list[l] < pivot:
                l += 1
                self.comparations += 1


            # To avoid unnecessary increments
            if not (r > left and numbers_list[r] >= pivot):
                self.comparations += 1
            # If right index is greater than left index and right element is greater than pivot
            while r > left and numbers_list[r] >= pivot:
                r -= 1
                self.comparations += 1

            # If left index is less than right index, then swap them
            if l < r:
                self.swap(numbers_list=numbers_list, a_index=l, b_index=r)
                self.swaps += 1


        # To avoid unnecessary increments
        if not (numbers_list[l] > pivot):
            self.comparations += 1
        # If l element is grates than pivot, then swap then
        if numbers_list[l] > pivot:
            self.swap(numbers_list=numbers_list, a_index=l, b_index=right)
            self.swaps += 1

        return l

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
    
    from random import randint

    quick: QuickSort = QuickSort()
    quick.numbers_list = [randint(0, 100) for c in range(100)]

    quick.print_list()
    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics.algorithm_name = QUICK_NAME
        metrics.data_type = FIRST_ORDER
        metrics = quick.benchmarkSort(metrics, )
        quick.print_list()
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparations}
          Swaps: {metrics.swaps}
        """)
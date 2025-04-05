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
from src.python.libs.benchmark.data import BenchMetrics, MERGE_NAME, SECOND_ORDER
from src.python.libs.benchmark.measuring import benchmark

class MergeSort(ListCreator):
    """Class to use Merge sort algorithm"""
    def __init__(self) -> None:
        super().__init__()
        self.swaps: int = 0 # Swaps counter
        self.comparations: int = 0 # Comparations counter

    @benchmark
    def benchmarkSort(self, metrics: BenchMetrics) -> Union[BenchMetrics | None]:
        """
        Will sort all number in the list with merge sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            Union: It will returns all metrics updated if list is not empty, else returns None
        """
        
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            return None
        
        # Run Algorithm 
        self.mergeSort(self.numbers_list)
        
        # Update metrics
        metrics.algorithm_name = MERGE_NAME
        metrics.data_type = self.data_type
        metrics.list_size = len(self.numbers_list)
        metrics.comparations = self.comparations # Update comparations on metrics
        metrics.swaps = self.swaps # Update swaps on metrics
        return metrics
               

    def mergeSort(self, numbers_list: list[int]) -> None:
        """
        It will sort the list using the recursive merge sort algorithm

        Args: 
            numbers_list (required): List to be sort
        """
        if  len(numbers_list) > 1:
            # Divide the list
            left_list: list[int] = numbers_list[:len(numbers_list)//2]
            right_list: list[int] = numbers_list[len(numbers_list)//2:]

            # Recursion
            self.mergeSort(left_list)
            self.mergeSort(right_list)
        
            l: int = 0 # Left list index
            r: int = 0 # Right list index
            k: int = 0 # Main list index
            
            # To avoid unnecessary increments
            if not (l < len(left_list) and r < len(right_list)):
                self.comparations += 1
            # While not finish left or right list
            while l < len(left_list) and r < len(right_list):
                if left_list[l] < right_list[r]:
                    numbers_list[k] = left_list[l]
                    l += 1
                else:
                    numbers_list[k] = right_list[r]
                    r += 1
                k += 1
                self.swaps += 1
                self.comparations += 1


            # To avoid unnecessary increments
            if not (l < len(left_list)):
                self.comparations += 1
            # Finish append left list
            while l < len(left_list):
                numbers_list[k] = left_list[l]
                self.swaps += 1
                l += 1
                k += 1         
                self.comparations += 1   


            # To avoid unnecessary increments
            if not (r < len(right_list)):
                self.comparations += 1
            # Finish append right list
            while r < len(right_list):
                numbers_list[k] = right_list[r]
                self.swaps += 1
                r += 1
                k += 1            
                self.comparations += 1
    

if __name__ == "__main__":

    merge: MergeSort = MergeSort()
    merge.data_generator(4, SECOND_ORDER)

    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics = merge.benchmarkSort(metrics)
        print(f"""
          Algotithm Name: {metrics.algorithm_name} 
          Data Type: {metrics.data_type}
          List size: {metrics.list_size}
          Execution time: {metrics.execution_time}
          Memory: {metrics.memory_usage}
          Comparations: {metrics.comparations}
          Swaps: {metrics.swaps}
        """)

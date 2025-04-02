# Update path
from os import getcwd
from basic_elements import update_python_path
current_dir: str = getcwd()
update_python_path(current_dir)

# Extern imports
from typing import Union
import logging

# Intern imports
from basic_elements import ListCreator
from benchmark.data import BenchMetrics, MERGE_NAME, FIRST_ORDER
from benchmark.measuring import benchmark

class MergeSort(ListCreator):
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
            BenchMetrics: All metrics updated
            None: If list is empty
        """
        
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            return None
        
        # Run Algorithm 
        self.mergeSort(self.numbers_list)
        
        # Update metrics
        metrics.comparations = self.comparations # Update comparations on metrics
        metrics.swaps = self.swaps # Update swaps on metrics
        return metrics
               

    def mergeSort(self, numbers_list: list[int]) -> None:
        """
        Merge sort recursive algorithm

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
    
    from random import randint

    bubble: MergeSort = MergeSort()
    bubble.numbers_list = [randint(0, 100) for c in range(100)]

    bubble.print_list()
    metrics: BenchMetrics | None = BenchMetrics()
    if (metrics != None):
        metrics.algorithm_name = MERGE_NAME
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

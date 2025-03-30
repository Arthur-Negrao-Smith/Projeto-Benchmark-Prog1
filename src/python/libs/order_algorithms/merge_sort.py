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
    def benchmarkSort(self, metrics: BenchMetrics) -> BenchMetrics:
        """
        Will sort all number in the list with merge sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            BenchMetrics: All metrics updated
        """
        
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            metrics.label="Erro"
            return metrics
        
        self.mergeSort(self.numbers_list)
        metrics.steps = self.steps # to calculate steps
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
            
            # While not finish left or right list
            while l < len(left_list) and r < len(right_list):
                if left_list[l] < right_list[r]:
                    numbers_list[k] = left_list[l]
                    l += 1
                else:
                    numbers_list[k] = right_list[r]
                    r += 1
                k += 1
                self.steps += 1

            # Finish append left list
            while l < len(left_list):
                numbers_list[k] = left_list[l]
                l += 1
                k += 1         
                self.steps += 1   

            # Finish append right list
            while r < len(right_list):
                numbers_list[k] = right_list[r]
                r += 1
                k += 1            
                self.steps += 1
    

if __name__ == "__main__":
    
    from random import randint

    merge: MergeSort = MergeSort()
    merge.numbers_list = [randint(0, 100) for c in range(100)]
    
    merge.print_list()
    metrics: BenchMetrics = BenchMetrics()
    metrics.label = "Teste"
    metrics.steps = 0
    metrics = merge.benchmarkSort(metrics)
    merge.print_list()
    print(f"\nLabel: {metrics.label}, Steps: {metrics.steps}, Memory: {metrics.memory_usage}, Execution time: {metrics.execution_time}")
    



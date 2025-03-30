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

class QuickSort(ListCreator):
    def __init__(self) -> None:
        super().__init__()
        self.steps: int = 0 # to calculate steps

    @benchmark
    def benchmarkSort(self, metrics: BenchMetrics) -> BenchMetrics:
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
        
        self.quickSort(self.numbers_list, 0, len(self.numbers_list) - 1)
        metrics.steps = self.steps # to calculate steps
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
        if left < right:
            partition_pos: int = self.partition(numbers_list=numbers_list, left=left, right=right)
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

        while l < r:

            while l < right and numbers_list[l] < pivot:
                l += 1
                self.steps += 1

            while r > left and numbers_list[r] >= pivot:
                r -= 1
                self.steps += 1

            if l < r:
                self.swap(numbers_list=numbers_list, a_index=l, b_index=r)
                self.steps += 1

        if numbers_list[l] > pivot:
            self.swap(numbers_list=numbers_list, a_index=l, b_index=right)
            self.steps += 1

        return l


if __name__ == "__main__":
    
    from random import randint

    quick: QuickSort = QuickSort()
    quick.numbers_list = [randint(0, 100) for c in range(100)]
    
    quick.print_list()
    metrics: BenchMetrics = BenchMetrics()
    metrics.label = "Teste"
    metrics.steps = 0
    metrics = quick.benchmarkSort(metrics)
    quick.print_list()
    print(f"\nLabel: {metrics.label}, Steps: {metrics.steps}, Memory: {metrics.memory_usage}, Execution time: {metrics.execution_time}")
    
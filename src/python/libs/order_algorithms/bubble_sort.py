from os import getcwd
from sys import path, platform

python_path: str = getcwd()
if platform == "win32":
    path.append(f"{python_path}\\src\\python\\libs")
else:
    path.append(f"{python_path}/src/python/libs")


from basic_elements import ListCreator
from benchmark.data import BenchMetrics
from benchmark.measuring import benchmark

import logging

class BubbleSort(ListCreator):
    def __init__(self) -> None:
        super().__init__()
        self.steps = 0 # Steps counter

    @benchmark
    def benchmarkSort(self, metrics: BenchMetrics) -> BenchMetrics:
        """
        Will sort all number in the list with bubble sort algorithm

        Args:
            metrics (required): Metrics wich will be used to storage data

        Returns: 
            BenchMetrics: All metrics updated
        """

        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            metrics.label="Erro"
            return metrics
        
        self.bubbleSort()
        metrics.steps = self.steps # Update steps on metrics
        return metrics

    def bubbleSort(self) -> None:
        """
        Bubble sort algorithm
        """

        sorted: bool = False
        list_size: int = len(self.numbers_list)
        
        while not sorted:
            
            for n in range(list_size):
                   
                self.steps += 1 # Update steps

                # If n is index of the last element
                if  n == list_size - 1:
                    sorted = True
                    break
                
                # Swap values
                elif self.numbers_list[n] > self.numbers_list[n+1]:
                   temp: int = self.numbers_list[n]
                   self.numbers_list[n] = self.numbers_list[n+1]
                   self.numbers_list[n+1] = temp
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
    metrics: BenchMetrics = BenchMetrics()
    metrics.label = "Teste"
    metrics.steps = 0
    metrics = bubble.benchmarkSort(metrics)
    bubble.print_list()
    print(f"\nLabel: {metrics.label}, Steps: {metrics.steps}, Memory: {metrics.memory_usage}, Execution time: {metrics.execution_time}")
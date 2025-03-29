from os import getcwd
from sys import path, platform

python_path: str = getcwd()
if platform == "win32":
    path.append(f"{python_path}\\src\\python\\libs")
else:
    path.append(f"{python_path}/src/python/libs")

print(f"Aqui está o path: {path}")

from basic_elements import ListCreator
from benchmark.data import BenchMetrics
from benchmark.measuring import benchmark

import logging

class Bubble(ListCreator):
    def __init__(self) -> None:
        super().__init__()

    @benchmark
    def sort(self, metrics: BenchMetrics) -> int:

        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            metrics.label="Erro"
            return metrics
        
        counter: int = 0
        sorted: bool = False
        list_size: int = len(self.numbers_list)

        while not sorted:
            
            for n in range(list_size):
                   
                counter += 1
                if  n == list_size - 1:
                    sorted = True
                    break
               
                elif self.numbers_list[n] > self.numbers_list[n+1]:
                   temp: int = self.numbers_list[n]
                   self.numbers_list[n] = self.numbers_list[n+1]
                   self.numbers_list[n+1] = temp
                   break

                elif self.numbers_list[n] <= self.numbers_list[n+1]:
                    continue

                else:
                    logging.warning("Comportamento inesperado no Bubble sort")
               
        metrics.steps = counter
        return metrics
    

if __name__ == "__main__":
    
    from random import randint
    bubble: Bubble = Bubble()
    bubble.numbers_list = [randint(0, 100) for c in range(100)]

    
    bubble.print_list()
    metrics: BenchMetrics = BenchMetrics()
    metrics.label = "Teste"
    metrics.steps = 0
    metrics = bubble.sort(metrics)
    bubble.print_list()
    print(f"\nLabel: {metrics.label}, Steps: {metrics.steps}, Memory: {metrics.memory_usage}, Execution time: {metrics.execution_time}")
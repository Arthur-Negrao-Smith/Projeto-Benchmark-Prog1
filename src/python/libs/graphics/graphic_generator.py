from os import getcwd
from sys import path, platform

python_path: str = getcwd()
if platform == "win32":
    path.append(f"{python_path}\\src\\python\\libs")
else:
    path.append(f"{python_path}/src/python/libs")


# Constants Columns
ALGORITHM_NAME_COLUMN: str = "Algoritmo"
DATA_TYPE_NAME_COLUMN: str = "Orgem dos Dados"
EXECUTION_TIME_NAME_COLUMN: str = "Tempo de execução"
MEMORY_USAGE_NAME_COLUMN: str = "Memória usada"
COMPARATIONS_NAME_COLUMN: str = "Comparações"
SWAPS_NAME_COLUMN: str = "Trocas"


# Intern imports
from benchmark.data import BenchMetrics, BUBBLE_NAME, MERGE_NAME, QUICK_NAME 

# Extern imports
import logging # To debug
from typing import Union
import matplotlib.pyplot as plt # To show the graphics
import pandas as pd # To create a table


class GraphicData:
    def __init__(self) -> int:
        self._data_dict: dict[str, pd.DataFrame] = dict()

    def __str__(self) -> str:
        return f"{self._data_dict}"

    def insert_data(self, data: BenchMetrics) -> int:
        temp_dataFrame: pd.DataFrame = self.benchMetrics_to_df(data)
        self._data_dict[data.algorithm_name].add(temp_dataFrame)

    def benchMetrics_to_df(self, data: BenchMetrics) -> Union[pd.DataFrame | None]:
        if type(data) == BenchMetrics:
            logging.warning(f"ERRO: benchMetrics_to_df aceita apeans o tipo BenchMetrics. Tipo passado -> {type(data)}")
            return None
        
        temp_dataFrame: pd.DataFrame = pd.DataFrame({
           ALGORITHM_NAME_COLUMN: [data.algorithm_name],
           DATA_TYPE_NAME_COLUMN: [data.data_type],
           EXECUTION_TIME_NAME_COLUMN: [data.execution_time],
           MEMORY_USAGE_NAME_COLUMN: [data.memory_usage],
           COMPARATIONS_NAME_COLUMN: [data.comparations],
           SWAPS_NAME_COLUMN: [data.swaps] 
        })
        return temp_dataFrame
        

class GraphicGenerator:
    def __init__(self) -> None:
        """
        Graphic generator to show results of the project
        """
        self.pdf_path: str = "src/results/pdf"
        self.data_dict: dict[str, BenchMetrics]
    
    def input_data(self, data: BenchMetrics, key: str = "") -> int:
        """
        Will add Benchmark metrics on data_dict

        Args:
            data (required): BenchmarkMetrics wich will be add
            key (required): Str with key to dict
        """
        if key == None or key == "":
            logging.warning("Não está sendo passada nenhuma key no dicionário. Nenhum valor adicionado")
            return -1
            
        self.data_dict[key] = data

    def plot_graphic(self):
        pass

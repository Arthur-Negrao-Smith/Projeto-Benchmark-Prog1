import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


# Constants Columns
ALGORITHM_NAME_COLUMN: str = "Algoritmo"
DATA_TYPE_NAME_COLUMN: str = "Orgem dos Dados"
EXECUTION_TIME_NAME_COLUMN: str = "Tempo de execução"
MEMORY_USAGE_NAME_COLUMN: str = "Memória usada"
COMPARATIONS_NAME_COLUMN: str = "Comparações"
SWAPS_NAME_COLUMN: str = "Trocas"


# Intern imports
from src.python.libs.benchmark.data import BenchMetrics, BUBBLE_NAME, MERGE_NAME, QUICK_NAME 

# Extern imports
import logging # To debug
from typing import Union
import matplotlib.pyplot as plt # To show the graphics
import pandas as pd # To create a table


class GraphicData:
    def __init__(self) -> int:
        self._data_dict: dict[str, pd.DataFrame] = {
            BUBBLE_NAME: pd.DataFrame(),
            MERGE_NAME: pd.DataFrame(),
            QUICK_NAME: pd.DataFrame()
            }

    def __str__(self) -> str:
        return f"{self._data_dict}"

    def insert_data(self, data: BenchMetrics) -> int:
        temp_dataFrame: pd.DataFrame = self.benchMetrics_to_df(data)
        self._data_dict[data.algorithm_name].add(temp_dataFrame)

    def benchMetrics_to_df(self, data: BenchMetrics) -> Union[pd.DataFrame | None]:
        if type(data) == type(BenchMetrics):
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

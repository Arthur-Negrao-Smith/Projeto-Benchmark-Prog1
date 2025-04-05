import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


# Constants Columns
ALGORITHM_NAME_COLUMN: str = "Algoritmo"
DATA_TYPE_NAME_COLUMN: str = "Ordem dos Dados"
LIST_SIZE: str = "Tamanho da Lista"
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
        self._data_dict: dict[str, Union[pd.DataFrame | None]] = {
            BUBBLE_NAME: None,
            MERGE_NAME: None,
            QUICK_NAME: None
            }

    def __str__(self) -> str:
        return f"{self._data_dict}"

    def insert_data(self, data: BenchMetrics) -> int:
        temp_dataFrame: pd.DataFrame = self.benchMetrics_to_df(data)
        if type(self._data_dict[data.algorithm_name]) != type(None):
            self._data_dict[data.algorithm_name] = pd.concat([self._data_dict[data.algorithm_name], temp_dataFrame])
            return 0
        else:
            self._data_dict[data.algorithm_name] = temp_dataFrame
            return 1

    def benchMetrics_to_df(self, data: BenchMetrics) -> Union[pd.DataFrame | None]:
        """
        Will convert BenchMetrics to pandas Data Frame

        Args:
            data (required): BenchMetrics to convert data

        Returns:
            None: It will return None if the data is not of type pd.DataFrame
            pd.DataFrame: It will return pandas DataFrame with all BenchMetrics
        """
        if type(data) == type(BenchMetrics):
            logging.warning(f"ERRO: benchMetrics_to_df aceita apeans o tipo BenchMetrics. Tipo passado -> {type(data)}")
            return None
        
        temp_dataFrame: pd.DataFrame = pd.DataFrame({
           ALGORITHM_NAME_COLUMN: [data.algorithm_name],
           DATA_TYPE_NAME_COLUMN: [data.data_type],
           LIST_SIZE: [data.list_size],
           EXECUTION_TIME_NAME_COLUMN: [data.execution_time],
           MEMORY_USAGE_NAME_COLUMN: [data.memory_usage[1] - data.memory_usage[0]],
           COMPARATIONS_NAME_COLUMN: [data.comparations],
           SWAPS_NAME_COLUMN: [data.swaps] 
        })
        return temp_dataFrame
    
    def save_as_csv(self, path: str) -> int:
        """
        It will convert GraphicData to a csv file

        Args:
            path (required): Path to storage data

        Returns:
            int: It will return 0 if was all very well, and will return 1 if path is not of type str
        """
        if type(path) != str:
            return 1

        for key, value in zip(self._data_dict.keys(), self._data_dict.values()):
            if value is not None:
                value.to_csv(f"{path}/{key}-python.csv", mode="a", index=False)

        return 0
            
        

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

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
from src.python.libs.benchmark.data import (BenchMetrics, 
                                            BUBBLE_NAME, MERGE_NAME, QUICK_NAME, 
                                            FIRST_SIZE, SECOND_SIZE, THIRD_SIZE, FOURTH_SIZE,
                                            FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER) 

# Extern imports
import logging # To debug
from typing import Union, Optional
import pandas as pd # To create a table


class TableData:
    """
    Dict with all algorithms data storaged
    """
    def __init__(self) -> int:
        self._data_dict: dict[str, Union[pd.DataFrame | None]] = {
            BUBBLE_NAME: None,
            MERGE_NAME: None,
            QUICK_NAME: None
            }

    def __str__(self) -> str:
        return f"{self._data_dict}"
    
    def __getitem__(self, index: int) -> Union[pd.DataFrame, None]:
        return self._data_dict[index]

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
    
    def save_as_csv(self, path: str, algorithm_to_save: Optional[str] = None) -> int:
        """
        It will convert TableData to a csv file

        Args:
            path (required): Path to storage data
            algortihm_to_save (optional): Specifies the algorithm to be save

        Returns:
            int: It will return 0 if was all very well. It will return 1 if path is not of type str and will return 2 if name of algorithm in algorithm_to_save not exist
        """
        if type(path) != str:
            return 1
        
        if algorithm_to_save is not None and algorithm_to_save not in [BUBBLE_NAME, MERGE_NAME, QUICK_NAME]:
            return 2

        if algorithm_to_save is None:
            for key, value in zip(self._data_dict.keys(), self._data_dict.values()):
                if value is not None:
                    value.to_csv(f"{path}/{key}-python.csv", mode="a", index=False)
        else:
            self._data_dict[algorithm_to_save].to_csv(f"{path}/{algorithm_to_save}-python.csv", mode="a", index=False)

        return 0
    
    def read_csv(self, path: str, language: str = "python", algorithm_name: Optional[str] = None) -> int:
        """
        It will convert csv file to TableData

        Args:
            path (required): Path to storage data
            language (optional): Language to collect data, python is default
            algortihm_name (optional): Specifies the algorithm to be collect

        Returns:
            int: It will return 0 if was all very well. It will return 1 if path is not of type str and will return 2 if name of algorithm in algorithm_name not exist
        """

        if type(path) != str:
            return 1
        
        if algorithm_name is not None and algorithm_name not in [BUBBLE_NAME, MERGE_NAME, QUICK_NAME]:
            return 2
            
        if algorithm_name is None:
            for key in self._data_dict.keys():      
                self._data_dict[key] = pd.read_csv(f"{path}/{key}-{language}.csv")
        else:
            self._data_dict[algorithm_name] = pd.read_csv(f"{path}/{algorithm_name}-{language}.csv")

        return 0
        


if __name__ == "__main__":
    table_data: TableData = TableData()

    size: int = FOURTH_SIZE
    order: str = FIRST_ORDER
    algorithm_name: str = MERGE_NAME
    print_table: bool = False

    table_data.read_csv("src/results/data", algorithm_name=algorithm_name)
    df: pd.DataFrame = table_data[algorithm_name]

    df['Tempo de execução'] = pd.to_numeric(df["Tempo de execução"], errors='coerce')
    df['Tamanho da Lista'] = pd.to_numeric(df["Tamanho da Lista"], errors='coerce')
    df['Comparações'] = pd.to_numeric(df["Comparações"], errors='coerce')
    df['Trocas'] = pd.to_numeric(df["Trocas"], errors='coerce')
    df['Memória usada'] = pd.to_numeric(df["Memória usada"], errors='coerce')

    if print_table:
        print(table_data._data_dict[algorithm_name])

    print("Algoritmo:", algorithm_name)
    print("Ordenação da list:", order)
    print("Tamanho da lista:", size)
    print("Tempo de execução:", df[(df['Ordem dos Dados'] == order) & (df['Tamanho da Lista'] == size)]['Tempo de execução'].median())
    print("Memória usada:", df[(df['Ordem dos Dados'] == order) & (df['Tamanho da Lista'] == size)]['Memória usada'].median())
    print("Comparações:", df[(df['Ordem dos Dados'] == order) & (df['Tamanho da Lista'] == size)]['Comparações'].median())
    print("Trocas:", df[(df['Ordem dos Dados'] == order) & (df['Tamanho da Lista'] == size)]['Trocas'].median())
# Changing python path one dir above
from os import chdir
chdir('..')

# Intern imports
from benchmark.data import BenchMetrics

# Extern imports
import logging # To debug
import matplotlib.pyplot as plt # To show the graphics

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
            return
            
        self.data_dict[key] = data

    def plot_graphic(self):
        pass

from .basic_elements import ListCreator

import logging

class Bubble(ListCreator):
    def __init__(self) -> None:
        super().__init__()

    def sort(self) -> int:
        if len(self.numbers_list) == 0:
            logging.warning("Lista de números está vazia. Impossível ordenar")
            return 1
        


        
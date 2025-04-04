import os
import sys

current_dir: str = os.path.abspath(os.curdir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import logging
from random import randint


from src.python.libs.benchmark.data import (
    FIRST_SIZE, SECOND_SIZE, THIRD_SIZE, FOURTH_SIZE,
    FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER,
    REPEATER_FACTOR, ITEMNS_PER_LINE
)

class ListCreator:
    def __init__(self) -> None:
        """
        Base to order algorithms
        """
        self.numbers_list: list[int] = list()
        self._MIN_NUMBER: int = 0
        self._MAX_NUMBER: int = 1_000_000
        self._SIZES: dict[int, int] = {
            1: FIRST_SIZE,
            2: SECOND_SIZE,
            3: THIRD_SIZE,
            4: FOURTH_SIZE
        }

    def data_generator(self, size: int, data_type: str) -> int:
        """
        Generate the numbers list

        Args:
            size (required): Int with size: 1, 2, 3 or 4
            data_type (required): Str with data order

        Returns:
            int: Return 0 if all of, 1 if value out of range, 2 if value isn't type int, 3 if data_type doesn't correct
        """
        if type(size) != int:
            logging.warning(f"Opção inválida: size = {size}. O tipo do parâmetro size deve ser int.")
            return 2
        
        if size < 1 or size > 4:
            logging.warning(f"Opção inválida: size = {size}. O valor do parâmetro size não está dentro do intervalo definido.")
            return 1

        if data_type == FIRST_ORDER:
            self.numbers_list = [i for i in range(0, self._SIZES[size])]

        elif data_type == SECOND_ORDER:
            self.numbers_list = [i for i in range(self._SIZES[size]-1, -1, -1)]
        
        elif data_type == THIRD_ORDER:
            self.numbers_list = [randint(self._MIN_NUMBER, self._MAX_NUMBER) for n in range(self._SIZES[size])]
        
        elif data_type == FOURTH_ORDER:
            self.numbers_list = [randint(self._MIN_NUMBER, self._MAX_NUMBER) % REPEATER_FACTOR for c in range(self._SIZES[size])]

        else:
            logging.warning("Opção inválida: Valor de data_type fora das opções possíveis")
            return 3
        
        return 0
    
    def print_list(self) -> None:
        """
        Print all numbers list
        """
        print("\n[ " , end="")
        for c, number in enumerate(self.numbers_list):
            
            if ((c % ITEMNS_PER_LINE != 0) and c < len(self.numbers_list) - 1) or c == 0:
                print(f"{number}, ", end="")

            elif c < len(self.numbers_list) - 1:
                print(f"\n{number}, ", end="")

            else:
                print(f"{number} ]")

# Tests
if __name__ == "__main__":
    listcreator: ListCreator = ListCreator()

    assert listcreator.data_generator(1, FIRST_ORDER)   == 0
    assert listcreator.data_generator(0, SECOND_ORDER)   == 1
    assert listcreator.data_generator("5", THIRD_ORDER) == 2


    listcreator.data_generator(1, FIRST_ORDER)
    assert len(listcreator.numbers_list) == FIRST_SIZE

    listcreator.data_generator(2, SECOND_ORDER)
    assert len(listcreator.numbers_list) == SECOND_SIZE

    listcreator.data_generator(3, THIRD_ORDER)
    assert len(listcreator.numbers_list) == THIRD_SIZE

    listcreator.data_generator(4, FOURTH_ORDER)
    assert len(listcreator.numbers_list) == FOURTH_SIZE
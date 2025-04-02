import logging
from random import randint

from sys import path, platform

def update_python_path(current_dir: str) -> None:
    """
    Will append libs of the project

    Args:
        current_dir (required): Acquired string by os.getcwd()
    """
    if platform == "win32":
        python_path: str = f"{current_dir}\\src\\python\\libs"
        if python_path not in current_dir:
            path.append(python_path)
    else:
        python_path: str = f"{current_dir}/src/python/libs"
        if python_path not in current_dir:
            path.append(f"{current_dir}/src/python/libs")

from os import getcwd
current_dir: str = getcwd()
update_python_path(current_dir)

class ListCreator:
    def __init__(self) -> None:
        """
        Base to order algorithms
        """
        self.numbers_list: list[int] = list()
        self._MIN_NUMBER: int = 0
        self._MAX_NUMBER: int = 1_000_000
        self._OPTIONS: dict[int, int] = {
            1: 1_000,
            2: 10_000,
            3: 100_000,
            4: 1_000_000
        }

    def random_generator(self, option: int) -> int:
        """
        Generate the numbers list

        Args:
            option (required): Int with option: 1, 2, 3 or 4

        Returns:
            int: Return 0 if all of, 1 if value out of range and 2 if value isn't type int
        """
        if type(option) != int:
            logging.warning(f"Opção inválida: option = {option}. O tipo do parâmetro option deve ser int.")
            return 2
        
        if option < 1 or option > 4:
            logging.warning(f"Opção inválida: option = {option}. O valor do parâmetro option não está dentro do intervalo definido.")
            return 1

        self.numbers_list = [randint(self._MIN_NUMBER, self._MAX_NUMBER) for n in range(self._OPTIONS[option])]
        return 0
    
    def print_list(self) -> None:
        """
        Print all numbers list
        """
        print("\n[ " , end="")
        for c, number in enumerate(self.numbers_list):
            if ((c % 20!= 0) and c < len(self.numbers_list) - 1) or c == 0:
                print(f"{number}, ", end="")
            elif c < len(self.numbers_list) - 1:
                print(f"\n{number}, ", end="")
            else:
                print(f"{number} ]")

# Tests
if __name__ == "__main__":
    listcreator: ListCreator = ListCreator()

    assert listcreator.random_generator(1) == 0
    assert listcreator.random_generator(0) == 1
    assert listcreator.random_generator("5") == 2

    listcreator.random_generator(1)
    assert len(listcreator.numbers_list) == 1_000
    listcreator.print_list()

    listcreator.random_generator(2)
    assert len(listcreator.numbers_list) == 10_000

    listcreator.random_generator(3)
    assert len(listcreator.numbers_list) == 100_000

    listcreator.random_generator(4)
    assert len(listcreator.numbers_list) == 1_000_000
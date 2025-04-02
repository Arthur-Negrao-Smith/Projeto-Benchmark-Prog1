# Algorith's Names 
BUBBLE_NAME: str = "bubble"
MERGE_NAME: str = "merge"
QUICK_NAME: str = "quick"

# Data Types Order
FIRST_ORDER: str = "sorted"
SECOND_ORDER: str = "reverse_sorted"
THIRD_ORDER: str = "random"
FOURTH_ORDER: str = "many_duplicates"


# Definig metrics
class BenchMetrics:
    """
    Class to storage data of simulation
    """
    memory_usage: tuple[int]
    execution_time: float
    comparations: int
    swaps: int
    algorithm_name: str
    data_type: str

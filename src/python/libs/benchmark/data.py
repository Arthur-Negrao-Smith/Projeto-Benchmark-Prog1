# Algorith's Names 
BUBBLE_NAME:         str =      "bubble"
MERGE_NAME:          str =      "merge"
QUICK_NAME:          str =      "quick"

# Data Types Order
FIRST_ORDER:         str =      "sorted"
SECOND_ORDER:        str =      "reverse_sorted"
THIRD_ORDER:         str =      "random"
FOURTH_ORDER:        str =      "many_duplicates"

# Sizes of list
FIRST_SIZE:          int =      1_000
SECOND_SIZE:         int =      10_000
THIRD_SIZE:          int =      100_000
FOURTH_SIZE:         int =      1_000_000

# Options
REPEATER_FACTOR:     int =      100
ITEMNS_PER_LINE:     int =      20

# Languages
PYTHON_LANG:         str =      "python"
C_LANG:              str =      "c"


# Definig metrics
class BenchMetrics:
    """
    Class to storage data of simulation
    """
    memory_usage:        tuple[int]
    execution_time:      float
    comparations:        int
    swaps:               int
    list_size:           int
    algorithm_name:      str
    data_type:           str

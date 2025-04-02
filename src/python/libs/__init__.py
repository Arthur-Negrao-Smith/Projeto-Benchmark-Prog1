from benchmark.data import BenchMetrics, BUBBLE_NAME, MERGE_NAME, QUICK_NAME, FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER
from benchmark.measuring import benchmark

from graphics.graphic_generator import GraphicData, GraphicGenerator

from order_algorithms.bubble_sort import BubbleSort
from order_algorithms.merge_sort import MergeSort
from order_algorithms.quick_sort import QuickSort
from order_algorithms.basic_elements import ListCreator, update_python_path
import math
from sort import bubble_sort


def radians_to_degrees(radians):
    degrees = radians * 180 / math.pi
    return degrees


if __name__ == '__main__':
    print(bubble_sort([3, 16, 22, 32, 1, 46, 23, 154, 45, 3, 2, 1]))

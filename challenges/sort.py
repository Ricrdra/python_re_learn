from time import sleep
from utils.Console import Colors
from utils.Printer import get_colored_list


def bubble_sort(unordered_list):
    for i in range(len(unordered_list)):
        for j in range(len(unordered_list) - i):

            if j == len(unordered_list) - i - 1:
                continue

            print('Checking', get_colored_list(unordered_list, Colors.OKCYAN, j, j + 1))
            sleep(0.4)
            if unordered_list[j] > unordered_list[j + 1]:
                print('Ordering', get_colored_list(unordered_list, Colors.OKGREEN, j, j + 1))
                unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]
                sleep(0.8)

    return unordered_list

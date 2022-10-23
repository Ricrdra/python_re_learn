from utils.Console import Colors


def get_colored_list(list_to_print, color, *kwargs):
    text = '['
    for i in range(len(list_to_print)):
        if i in kwargs:
            text += f"{color}{list_to_print[i]}{Colors.ENDC}"
        else:
            text += f"{list_to_print[i]}"

        if i != range(len(list_to_print) - 1):
            text += ','

    text += ']'
    return text

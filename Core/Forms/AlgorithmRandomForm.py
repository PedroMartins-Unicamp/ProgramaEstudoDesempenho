from fileinput import filename
from Core.Algorithms.Sorting import CountingSort, IterativeSort, RecursiveSort
from Core.ExecController import ExecController
from Core.Resources import path_utils
import os


clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def header(data):
    clear()
    for x in data:
        print(x)
    print()


def algorithm_random_form(lists_path: str) -> list:
    data = ["-Algorithm Random Form-"]
    header(data)
    
    paths = {}
    x = 1
    for path in path_utils.list_directories(lists_path):
        paths[x] = lists_path+path+"/"
        x += 1
    x = 1
    
    print(f"Lists: ")
    for key, value in paths.items():
        print(f"{key} - {value.split('/')[-2]}")
    print()
    
    try:
        x = int(input("Which list to order: \n> "))
        target = paths[x]
    except ValueError as e:
        print(f"Invalid option: {e}")
        exit()
    except IndexError as e:
        print(f"Invalid option: {e}")
        exit()
    except KeyError as e:
        print(f"Invalid option: {e}")
        exit()
    data.append(f"List: {target.split('/')[-2]}")
    
    lists = {}
    x = 1
    for file in path_utils.list_files(target):
        if '[' and ']' in file:
            lists[x] = file
            x += 1
    x = 1

    header(data)

    algorithms = {
        1: IterativeSort.bubble_sort,
        2: IterativeSort.selection_sort,
        3: IterativeSort.insertion_sort,
        4: IterativeSort.shell_sort,
        5: IterativeSort.iterative_quick_sort,
        6: RecursiveSort.merge_sort,
        7: RecursiveSort.quick_sort,
        8: CountingSort.counting_sort
    }

    for key, value in algorithms.items():
        print(f"{key} - {value.__name__}")
    print()

    try:
        x = int(input("Which function: \n> "))
        sort_method = algorithms[x]
    except ValueError as e:
        print(f"Invalid option: {e}")
        exit()
    except IndexError as e:
        print(f"Invalid option: {e}")
        exit()
    except KeyError as e:
        print(f"Invalid option: {e}")
        exit()
    data.append(f"Algorithm: {sort_method.__name__}")

    header(data)

    while True:
        result_filename = input("Result filename (will follow \"[Result]{filename}.txt\"): \n> ")
        
        if f"[Result]{result_filename}.txt" in path_utils.list_files("./Results/Random/"):
            print("File already exists.")
            continue
        
        break
    data.append(f"Result file: {result_filename}")

    header(data)
    
    original_lists = []
    for key, value in lists.items():
        original_lists.append(path_utils.get_list(target+value))
    
    target_model = "Random"

    return [ExecController(original_lists, target_model, sort_method), result_filename]

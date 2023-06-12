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


def algorithm_default_form(list_path: str) -> list:
    data = ["-Algorithm Default Form-"]
    header(data)

    lists = {}
    x = 1
    for file in path_utils.list_files(list_path):
        if '[' and ']' in file:
            lists[x] = file
            x += 1
    x = 1

    print(f"Lists: ")
    for key, value in lists.items():
        print(f"{key} - {value}")
    print()
    
    try:
        x = int(input("Which list to order: \n> "))
        target = lists[x]
    except ValueError as e:
        print(f"Invalid option: {e}")
        exit()
    except IndexError as e:
        print(f"Invalid option: {e}")
        exit()
    except KeyError as e:
        print(f"Invalid option: {e}")
        exit()
    data.append(f"List: {target}")

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
    
    
    try:
        repetitions = int(input("How many times: \n> "))
        if repetitions <= 0:
            raise ValueError
    except ValueError as e:
        print(f"Repetitions quantity must be an positive integer higher than 0: {e}")
        exit()
    data.append(f"Repetitions: {repetitions}")

    header(data)


    while True:
        result_filename = input("Result filename (will follow \"[Result]{filename}.txt\"): \n> ")
        
        if f"[Results]{result_filename}.txt" in path_utils.list_files("./Results/Ordered/")+path_utils.list_files("./Results/Reverse/"):
            print("File already exists.")
            continue
        
        break
    data.append(f"Result file: {result_filename}")

    header(data)
            
  
    original_lst = path_utils.get_list(list_path+target)
    target_model = target[target.index('[')+1:target.index(']')]

    return [ExecController(original_lst, target_model, sort_method, repetitions), result_filename]

from Core.ExecContext import ExecContext
from Core.Forms.AlgorithmDefaultForm import algorithm_default_form
from Core.Forms.AlgorithmRandomForm import algorithm_random_form
import os
import sys

sys.setrecursionlimit(1_000_000_000)

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    print("EXECUTION TIME")

    choice = 0
    print("List types: ")
    print("1 - Ordered")
    print("2 - Reverse")
    print("3 - Random")
    while(1):
        try:
            choice = int(input("Which list type: "))
            if choice not in [1, 2, 3]:
                print("Error: Invalid option.")
                choice = 0
                continue
            break
        except ValueError as e:
            print(f"Selection must be an positive integer whom matches an given option: {e}")
            exit()
                
    result = None
    if choice == 1: # Ordered
        lists_path = "./Lists/Ordered/"
        result = algorithm_default_form(lists_path)

    elif choice == 2: # Reverse
        lists_path = "./Lists/Reverse/"
        result = algorithm_default_form(lists_path)
    
    elif choice == 3: # Random
        lists_path = "./Lists/Random/"
        result = algorithm_random_form(lists_path)
        
        
    with ExecContext(result[0], result[1]) as exec:
        exec.run()


if __name__ == "__main__":
    main()

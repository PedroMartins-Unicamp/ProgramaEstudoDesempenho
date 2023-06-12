from Core.Resources.path_utils import list_files
import os
from random import shuffle
import argparse


def _validate_args(str: str, a: int, b: int, listtype: str) -> None:
    try:
        a, b = int(a), int(b)
    except ValueError as e:
        print("Invalid argument values: ", e)
        exit()

    for file in list_files('.'):
        if f"[{listtype}]{str}.txt" == file:
            print("File with this name already exists.")
            exit()

def _store_list(filename: str, array: list, listtype: str, filepath: str=None) -> None:
    if filepath is None:
        filepath = f'Lists/{listtype}/[{listtype}]{filename}.txt'
        
    with open(filepath, 'w+') as file:
        for x in array:
            file.write(f"{x},")


def create_ordered_list(listname: str, a: int, b: int=None, listpath: str=None) -> None: 
    start, end = None, None
    
    if b != None:
        start, end = a, b
    else:
        start, end = 0, a
    
    _validate_args(listname, start, end, "Ordered")
    start, end = int(start), int(end)
    
    if start > end:
        print("Start-point needs to be lower than end-point.")
        exit()
    
    lst = list(x for x in range(start, end+1))

    if listpath is None:
        _store_list(listname, lst, "Ordered")
    else: 
        _store_list(listname, lst, "Ordered", filepath=listpath)

def create_reverse_list(listname: str, a: int, b: int=None, listpath: str=None) -> None: 
    start, end = None, None
    
    if b != None:
        start, end = a, b
    else:
        start, end = a, 0
    
    _validate_args(listname, start, end, "Reverse")
    start, end = int(start), int(end)
    
    if start < end:
        print("Start-point needs to be lower than end-point.")
        exit()
    
    lst = list(x for x in range(start, end-1, -1))
    
    if listpath is None:
        _store_list(listname, lst, "Reverse")
    else: 
        _store_list(listname, lst, "Reverse", filepath=listpath)

def create_random_list(listname: str, a: int, b: int=None, listpath: str=None) -> None: 
    start, end = None, None
    
    if b != None:
        start, end = a, b
    else:
        start, end = 0, a
    
    _validate_args(listname, start, end, "Random")
    start, end = int(start), int(end)

    if start > end:
        print("Start-point needs to be higher than end-point.")
        exit()

    lst = list(x for x in range(start, end+1))
    shuffle(lst)

    if listpath is None:
        _store_list(listname, lst, "Random")
    else: 
        _store_list(listname, lst, "Random", filepath=listpath)


def main():
    parser = argparse.ArgumentParser(description="Create a numerical list on a external .txt file.")

    parser.add_argument('-f', "--filename", type=str, help="['ListType']{filename}.txt. REQUIRED", required=True)
    parser.add_argument('-t', "--type", type=str, help="List type: 'o' for Ordered, 'r' for Reverse or 'rd' for random. REQUIRED", required=True)
    parser.add_argument('-a', "--a_point", type=int, help="Number point for the list. Start-point for Ordered or Random, end-point for Reverse. Opposite if it is the only given point. REQUIRED", required=True)
    parser.add_argument('-b', "--b_point", type=int, help="Number point for the list. End-point for Ordered or Random, start-point for Reverse. OPTIONAL, equals 0 by default.")
    parser.add_argument('-q', "--quantity", type=int, help="Select a the amount of lists variations to be created in the directory, having their filenames variyng by '[Random]{filename}({count}).txt'. OPTIONAL, although only available in case of Random list type")
    

    args = parser.parse_args()
    
    listtype, filename = None, args.filename
    if args.type.lower() == 'o': listtype = "Ordered"
    elif args.type.lower() == 'r': listtype = 'Reverse'
    elif args.type.lower() == "rd": listtype = "Random"
    
    
    filepath = f"Lists/{listtype}/[{listtype}]{filename}.txt"

    if args.type == 'o':
        create_ordered_list(args.filename, args.a_point, args.b_point,listpath=filepath)
    elif args.type == 'r':
        create_reverse_list(args.filename, args.a_point, args.b_point, listpath=filepath)
    elif args.type == 'rd':
        if args.quantity == None:
            create_random_list(args.filename, args.a_point, args.b_point, listpath=filepath)
        elif args.quantity > 0:
            os.mkdir(f"Lists/Random/{filename}")
            for i in range(1, args.quantity+1):     
                filepath = f"Lists/{listtype}/{filename}/[{listtype}]{filename}({i}).txt"
                create_random_list(args.filename, args.a_point, args.b_point, listpath=filepath)
        else:
            raise argparse.ArgumentError("Not valid quantity value. Only integer numbers higher than 0 are allowed.")
    else:
        raise argparse.ArgumentError("Not valid list type, try: 'o' for ordered, 'r' for reverse or 'rd' for random.")


if __name__ == '__main__':
    main()

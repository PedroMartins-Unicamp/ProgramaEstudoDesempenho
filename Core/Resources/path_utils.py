import os


def generate_id():
    """Generate an id and verify in the id_list.py file if this id is available."""
    filepath = './Controllers/resources/id_list.txt'
    with open(filepath, 'r+') as file:
        ids = [int(x) for x in file.readlines()[2:]]
        id = ids.pop() + 1
        file.write(f"\n{id}")
    return id


def get_results_list(filepath: str) -> list:
    with open(filepath, 'r+') as file:
        lines = file.readlines()[1:]
        results = list(float(line[line.index(']')+1:]) for line in lines)
        
        return results


def get_list(filepath: str) -> list:
    with open(filepath, 'r') as file:
        file.seek(0)
        lst = [int(x) for x in filter(None, file.read().split(','))]
        return lst


def list_files(dirpath) -> list:
    files = []
    for n in os.listdir(path=dirpath):
        if os.path.isfile(dirpath+n):
            files.append(n)
    return files

def list_directories(dirpath) -> list:
    dirs = []
    for n in os.listdir(path=dirpath):
        if not os.path.isfile(dirpath+n):
            dirs.append(n)
    return dirs


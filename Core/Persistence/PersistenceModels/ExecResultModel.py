from Core.ExecController import ExecController
from datetime import date
from collections import namedtuple

def result_text(exec_controller: ExecController) -> str:
    result = exec_controller
    txt = f"""Algorithm:{result.algorithm.__name__}
Date:{result.date.day}/{result.date.month}/{result.date.year}
Repetitions:{result.repetitions}
ListModel:{result.target_model}
ListSize:{result.target_size}

ExecTimes:

"""
    # result is a list with instances of the Result namedtuple, described below:
    # Result = namedtuple("Result", ["test_number", "exec_time"])
    for res in result.results:
        txt = txt+f"[{res.test_number}]{res.exec_time:.4f}s\n"
        
    if not result.successfully_executed:
        txt += "INTERRUPTED EXECUTION\n"
        
    txt += '\n'
    if len(result.results) == 0:
        txt += "Min:0\n"
        txt += "Max:0\n\n"
        txt += "Results_Average:0"
    else: 
        txt += f"Min:{min([x.exec_time for x in result.results]):.4f}s\n"
        txt += f"Max:{max([x.exec_time for x in result.results]):.4f}s\n\n"
        txt += f"Results_Average:{sum([x.exec_time for x in result.results])/len(result.results):.4f}\n\n"
    
    if result.successfully_executed:
        txt += "SUCCESSFULLY EXECUTED"

    return txt

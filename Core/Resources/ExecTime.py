import time

def time_count(func) -> str:
    def wrapper(*args, **kwargs) -> str: 
        
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = (end_time - start_time)
        
        return exec_time
    
    return wrapper

@time_count
def get_time(algorithm, array):
    algorithm(array)

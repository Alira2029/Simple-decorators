def timeit(func):
    import time
    
    def wrapper(*args, **kwargs):
        print('Start execution')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        print(f'Execution time: {exec_time} sec')  
        return result
    return wrapper 

@timeit
def only_str(list):
    result = [element for element in list if type(element) == str]    
    return result 
    
info = [23, 'names', 'password', 45, 10, 'figure']    

print(only_str(info))  

import pickle
from helper_functions import get_fraction, merge_sets



def get_solutions(task_id:int, queue, lock, file_path:str, order1_sets:list[list[set[int]]], ranges:list[tuple[int]], check_set:set[int] = set(), sol:list[int] = []) -> None:
    
    len_sol = len(sol)
    
    if len_sol == len(ranges):
        
        progress = get_fraction(sol, ranges)
        
        queue.put((task_id, progress))
        
        global_solutions = []
        
        with lock:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
                global_solutions = data["solutions"]

        if sol not in global_solutions:
            global_solutions.append(sol)
            
        data["solutions"] = global_solutions
        
        message = f"Process {sol[0]+1} found: {sol}"
        
        message = message + " "*(90 - len(message)) + "total found: " + str(len(global_solutions))
        
        print("\n\033[K\n\033[K", message,  "\033[F\033[F" , sep="", end = "\r")
        
        with lock:
            with open(file_path, 'wb') as file:
                pickle.dump(data, file)

        return

    start, end = ranges[len_sol]

    for i, brick_set in enumerate(order1_sets[len_sol][start:end]):
        merged = merge_sets(brick_set,check_set)
        if merged:
            get_solutions(task_id, queue, lock, file_path, order1_sets, ranges, merged, sol + [start+i])


    if len_sol == 0:
        
        queue.put((task_id, 1))

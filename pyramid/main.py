import time
import os
import pickle
from multiprocessing import Pool, Manager
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn
from pyramid.graph import Graph
from pyramid.brick import Brick
from pyramid.processing import process_solutions
from pyramid.preprocessing import initialize

# only unique solutions with first brick only in symmetry area
# automatically optimize brick order (shuffle and testing)
# postprocessing with pickled solutions
# render solutions


def get_solutions(graph:Graph,bricks:list[Brick],num_processes:int = os.cpu_count()) -> None:
    
    start_time = time.time()
 
    with Manager() as manager:
     
        queue = manager.Queue()
        
        argument_list = initialize(graph, bricks, num_processes, queue)
  
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeElapsedColumn(),
        ) as progress:
      
            task_progress = {}
   
            for task_id in range(num_processes):
       
                task_description = f"Process {task_id + 1}"
                task_progress[task_id] = progress.add_task(
                    task_description, total=1)
                
            with Pool(num_processes) as pool:
                
                results = []
                
                for i in range(len(argument_list)):
                    result = pool.apply_async(process_solutions, argument_list[i])
                    results.append(result)
                
                while any(not progress.tasks[task_id].finished for task_id in task_progress):
                    
                    while not queue.empty():
                        queue_element = queue.get()
                        
                        if type(queue_element) == tuple:
                            
                            if type(queue_element[0]) == int:
                                
                                task_id, progress_amount = queue_element
                                progress.update(task_progress[task_id],completed=progress_amount)
                            
                            elif type(queue_element[0]) == str:
                                
                                file_path, sol = queue_element
                                
                                global_solutions = []
        
                                with open(file_path, 'rb') as file:
                                    data = pickle.load(file)
                                    global_solutions = data["solutions"]

                                if sol not in global_solutions:
                                    global_solutions.append(sol)
                                    
                                data["solutions"] = global_solutions

                                with open(file_path, 'wb') as file:
                                    pickle.dump(data, file)
                        
                        else:
                            print("Process", queue_element[0]+1, "had an exception:")
                            raise queue_element[1]
                                                  
                        
    print("\n\n\n\nTook:", round((time.time() - start_time)/60, 2), "min\n")
    
    print("Finished!\n")

def get_configurations(file_path):
    
    with open(file_path, "rb") as file:
            data: dict = pickle.load(file)
            graph: Graph = data["graph"]
            bricks: list[Brick] = data["bricks"]
            order1_sets: list[list[set[int]]] = data["order1_sets"]
            solutions: list[list[int]] = data["solutions"]
            
    configurations = []
            
    for sol in solutions:
        configuration = {}
        for i, index in enumerate(sol):
            for node_id in order1_sets[i][index]:
                configuration[node_id] = bricks[i].id
        configurations.append(configuration)
        
    return configurations
            

def render_configuration(graph: Graph, configuration: dict[int,int]):
    
    #get max coordinates and scale accordingly
    
    #get renderer
    
    #for node in configuration
        #create object of sphere in nodes pos of color 
        
    #for node in configuration
        #for neighbor of node
            #create object of line between node and neighbor
            
    #open view window of rendered objects
    
    pass
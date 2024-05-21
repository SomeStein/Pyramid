import time
import os
from multiprocessing import Pool, Manager
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn
from pyramid import pyramid, bricks
from graph import Graph
from brick import Brick
from processing import get_solutions
from preprocessing import initialize

# GIT!
# hardcoded stuff (test with different graphs and bricks)
# only unique solutions with first brick only in symmetry area
# automatically optimize brick order (shuffle and testing)
# postprocessing with pickled solutions
# render solutions


def main(graph:Graph,bricks:list[Brick],num_processes:int = os.cpu_count()) -> None:
    
    start_time = time.time()
 
    with Manager() as manager:
     
        queue = manager.Queue()
        
        lock = manager.Lock()
        
        argument_list = initialize(graph, bricks, num_processes, queue, lock)
  
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
                    result = pool.apply_async(get_solutions, argument_list[i])
                    results.append(result)
                
                while any(not progress.tasks[task_id].finished for task_id in task_progress):
                    
                    if time.time() - start_time >= 60*60:
                        
                        try:
                            for result in results:
                                result.get()
                                
                        except Exception as e:
                            raise e
                    
                    while not queue.empty():
                        with lock:
                            task_id, progress_amount = queue.get()
                            progress.update(task_progress[task_id],completed=progress_amount)
                        
    print("\n\n\n\nTook:", round((time.time() - start_time)/60, 2), "min\n")
    
    print("Finished!\n")


if __name__ == "__main__":
    main(pyramid,bricks)

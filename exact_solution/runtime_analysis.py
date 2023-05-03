import time
import solution

import multiprocessing

def compute(i):
    graph = dict([(x, {x+1, x-1}) for x in range(1, i)])
    graph[0]={i,1}
    graph[i]={0, i-1}
    start = time.perf_counter()
    solution.min_coloring(graph)
    end = time.perf_counter()
    runtime = end-start
    print(f'{len(graph)},{runtime}')

if __name__ == '__main__':
    print('|V|,truntime (s)')
    
    for i in range(1, 12):
        processes = []
        for _ in range(5):
            process = multiprocessing.Process(target=compute, name=f'{i}', args=(i,))
            process.start()
            processes.append(process)
        for process in processes:
            process.join()



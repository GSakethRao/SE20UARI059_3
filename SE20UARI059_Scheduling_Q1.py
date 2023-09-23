#!/usr/bin/env python
# coding: utf-8

# In[11]:


processes = ['P1', 'P2', 'P3', 'P4']

arrival_time = [0, 4, 5, 6]
burst_time = [24, 3, 3, 12]
priority = [3, 1, 4, 2]

def firstcomefirstserve(arrival_time, burst_time):
    n = len(arrival_time)
    wt = [0] * n
    tat = [0] * n
    comp_time = 0
    
    for i in range(n):
        if comp_time < arrival_time[i]:
            comp_time = arrival_time[i]
            
        comp_time += burst_time[i]
        tat[i] = comp_time - arrival_time[i]
        wt[i] = tat[i] - burst_time[i]
        
    return wt, tat

def priority_scheduling(arrival_time, burst_time, priority):
    jobs = sorted(list(zip(arrival_time, burst_time, priority)), key=lambda x: x[2])
    return fcfs([j[0] for j in jobs], [j[1] for j in jobs])


def shortjobfirst(arrival_time, burst_time):
    jobs = sorted(list(zip(arrival_time, burst_time)), key=lambda x: x[1])
    return fcfs([j[0] for j in jobs], [j[1] for j in jobs])


def round_robin(arrival_time, burst_time, quantum):
    n = len(arrival_time)
    remaining_time = burst_time.copy()
    wt = [0] * n
    tat = [0] * n
    time = 0
    
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                
                if remaining_time[i] > quantum:
                    time = time + quantum
                    remaining_time[i] -= quantum
                    
                else:
                    time += remaining_time[i]
                    wt[i] = time - burst_time[i]
                    remaining_time[i] = 0
        if done:
            break
            
    for i in range(n):
        tat[i] = burst_time[i] + wt[i] 
    return wt, tat

def average(lst):
    return sum(lst) / len(lst)

algorithms = {
    'FCFS': firstcomefirstserve,
    'SJF': shortjobfirst,
    'PS': priority_scheduling,
    'RR': lambda at, bt: round_robin(at, bt, 4)
}

results = {}

for name, algo in algorithms.items():
    wt, tat = algo(arrival_time, burst_time) if name != 'PS' else algo(arrival_time, burst_time, priority)
    avg_wt = average(wt)
    avg_tat = average(tat)
    
    results[name] = (avg_wt, avg_tat)
    print(f'{name} - Avg Waiting Time: {avg_wt}, Avg Turnaround Time: {avg_tat}')

best_algo = min(results, key=results.get)


print(f"\n The best algorithm based on avg waiting time and avg turnaround time is with least average turn around time is: {best_algo}")


# In[ ]:





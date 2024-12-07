# FCFS sucks yo
def calc_turnaround_time(completion_time, arrival_time):
    # amount of time  to execute a particular process : Completion Time - AT
    return [completion_time[i] - arrival_time[i] for i in range(len(arrival_time))]

def calc_waiting_time(turnaround_time, burst_time):
    # wait time is basically how much time process waits in ready queue :
    # Turnaround Time (total time to process) - Burst Time (actual processing) =  waiting time
    # turnaround time = at + bt + waiting time of previous
    return [turnaround_time[i] - burst_time[i] for i in range(len(burst_time))]


def avg_time(processes, n, arrival_time, burst_time):
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # calc compeltion time
    for i in range(n):
        if i == 0: completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            completion_time[i] = max(completion_time[i-1], arrival_time[i]) + burst_time[i]

    turnaround_time = calc_turnaround_time(completion_time, arrival_time)
    waiting_time = calc_waiting_time(turnaround_time, burst_time)
    total_wt = sum(waiting_time)
    total_tat = sum(turnaround_time)
    print("Processs | Arrival | Burst | Waiting | Turnaround")
    for i in range(n):
        print(
            f"{processes[i]}      | {arrival_time[i]}      | {burst_time[i]}   | {waiting_time[i]}      | {turnaround_time[i]}")
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")


def main():
    n = int(input("Enter number of processes : "))
    processes = []
    at = []
    bt = []
    for i in range(n):
        pid = f"P{i+1}"
        arrival = int(input(f"Enter arrival time of {pid} : "))
        burst = int(input(f"Enter burst time of {pid} : "))
        processes.append(pid)
        at.append(arrival)
        bt.append(burst)
    # sort on at
    sortedMethod = sorted(range(n), key=lambda k: at[k])
    sorted_processes = [processes[i] for i in sortedMethod]
    sorted_at = [at[i] for i in sortedMethod]
    sorted_bt = [bt[i] for i in sortedMethod]
    avg_time(sorted_processes, n, sorted_at, sorted_bt)

main()

# Non Preemptive Attempt

# Better to create class for process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time


def calc_wt(processes):
    n = len(processes)

    waiting_time = [0] * n
    completion_time = [0] * n

    # Calculate completion time
    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i].arrival_time + \
                processes[i].burst_time
        else:
            # The next process starts after the previous one completes or when it arrives
            completion_time[i] = max(
                completion_time[i - 1], processes[i].arrival_time) + processes[i].burst_time

    # Calculate waiting time using TAT and BT
    for i in range(n):
        tat = completion_time[i] - processes[i].arrival_time
        waiting_time[i] = tat - processes[i].burst_time

    return waiting_time, completion_time


def sjf(processes):
    # Sort based on Arrival Time and then Burst Time
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

    waiting_times, completion_times = calc_wt(processes)

    total_waiting_time = sum(waiting_times)
    total_turnaround_time = sum(
        completion_times[i] - processes[i].arrival_time for i in range(len(processes)))

    print("Process | Arrival | Burst | Waiting | Turnaround")
    for i in range(len(processes)):
        turnaround_time = completion_times[i] - processes[i].arrival_time
        print(f"{processes[i].pid}      | {processes[i].arrival_time}      | {processes[i].burst_time}   | {waiting_times[i]}      | {turnaround_time}")

    print(f"\nAverage Waiting Time: {total_waiting_time / len(processes):.2f}")
    print(
        f"Average Turnaround Time: {total_turnaround_time / len(processes):.2f}")


def main():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        process_id = f"P{i+1}"
        arrival = int(input(f"Enter arrival time of {process_id}: "))
        burst = int(input(f"Enter burst time of {process_id}: "))

        processes.append(Process(process_id, arrival, burst))

    sjf(processes)


#main()

# Preemptive Solution : shortest remaining time first scheduling


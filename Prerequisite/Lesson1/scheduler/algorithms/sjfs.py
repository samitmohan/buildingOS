# Non Preemptive Attempt


# Better to create class for process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time  # Remaining time for preemption


def calc_wt(processes):
    n = len(processes)

    waiting_time = [0] * n
    completion_time = [0] * n

    # Calculate completion time
    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i].arrival_time + processes[i].burst_time
        else:
            # The next process starts after the previous one completes or when it arrives
            completion_time[i] = (
                max(completion_time[i - 1], processes[i].arrival_time)
                + processes[i].burst_time
            )

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
        completion_times[i] - processes[i].arrival_time for i in range(len(processes))
    )

    print("Process | Arrival | Burst | Waiting | Turnaround")
    for i in range(len(processes)):
        turnaround_time = completion_times[i] - processes[i].arrival_time
        print(
            f"{processes[i].pid}      | {processes[i].arrival_time}      | {processes[i].burst_time}   | {waiting_times[i]}      | {turnaround_time}"
        )

    print(f"\nAverage Waiting Time: {total_waiting_time / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_turnaround_time / len(processes):.2f}")


# Preemptive Solution : shortest remaining time first scheduling


def sjf_preemptive(processes):
    n = len(processes)
    time, completed = 0, 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    while completed < n:  # While there are processes to complete
        idx = -1
        min_rem_time = float("inf")

        # Find process with smallest remaining time that has arrived
        for i in range(n):
            if processes[i].arrival_time <= time and processes[i].remaining_time > 0:
                if processes[i].remaining_time < min_rem_time:
                    min_rem_time = processes[i].remaining_time
                    idx = i

        if idx != -1:  # If a process is found to execute
            # Execute for one time unit
            processes[idx].remaining_time -= 1
            time += 1

            # If the process is completed
            if processes[idx].remaining_time == 0:
                completed += 1
                completion_time[idx] = time
                turnaround_time[idx] = (
                    completion_time[idx] - processes[idx].arrival_time
                )
                waiting_time[idx] = turnaround_time[idx] - processes[idx].burst_time

        else:
            time += 1  # Increment time if no process is ready to execute

    return waiting_time, turnaround_time


def main():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        process_id = f"P{i+1}"
        arrival = int(input(f"Enter arrival time of {process_id}: "))
        burst = int(input(f"Enter burst time of {process_id}: "))

        processes.append(Process(process_id, arrival, burst))

    sjf(processes)

    # Preemptive

    # waiting_times, turnaround_times = sjf_preemptive(processes)

    # print("\nProcess | Arrival | Burst | Waiting | Turnaround")
    # for i in range(n):
    #     print(
    #         f"{processes[i].pid}      | {processes[i].arrival_time}      | {processes[i].burst_time}   | {waiting_times[i]}      | {turnaround_times[i]}"
    #     )

    # average_waiting_time = sum(waiting_times) / n
    # average_turnaround_time = sum(turnaround_times) / n

    # print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    # print(f"Average Turnaround Time: {average_turnaround_time:.2f}")


# main()

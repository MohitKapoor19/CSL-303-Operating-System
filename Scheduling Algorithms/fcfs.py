class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

# Function to perform FCFS scheduling
def fcfs_scheduling(processes):
    n = len(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    gantt_chart = []

    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # CPU idle until process arrives

        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

        gantt_chart.append((process.pid, current_time, process.completion_time))
        current_time = process.completion_time

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    return gantt_chart, avg_waiting_time, avg_turnaround_time

def main():
    # User input for process IDs, burst times, and arrival times
    process_ids = list(map(int, input("Enter process IDs as space-separated values: ").split()))
    burst_times = list(map(int, input("Enter burst times as space-separated values: ").split()))
    arrival_times = list(map(int, input("Enter arrival times as space-separated values: ").split()))
    
    n = len(process_ids)
    processes = [Process(process_ids[i], burst_times[i], arrival_times[i]) for i in range(n)]

    # Perform FCFS scheduling
    gantt_chart, avg_waiting_time, avg_turnaround_time = fcfs_scheduling(processes)

    # Output Gantt Chart
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: Start time = {entry[1]}, End time = {entry[2]}")

    # Output average waiting time and turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

if __name__ == "__main__":
    main()

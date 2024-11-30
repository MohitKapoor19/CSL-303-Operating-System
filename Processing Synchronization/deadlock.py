def is_safe_state(processes, available, max_demand, allocation):
    num_processes = len(processes)
    num_resources = len(available)

    # Calculate the need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]

    # Initialize work (available resources) and finish flags
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        allocated = False
        for i in range(num_processes):
            if not finish[i]:
                # Check if need <= work
                if all(need[i][j] <= work[j] for j in range(num_resources)):
                    # This process can be satisfied
                    for j in range(num_resources):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    allocated = True
                    break
        if not allocated:
            break  # No allocation was possible

    if len(safe_sequence) == num_processes:
        return True, safe_sequence
    else:
        return False, []


# Input
if __name__ == "__main__":
    # Number of processes and resources
    processes = [0, 1, 2, 3, 4]  # Process IDs
    available = [3, 3, 2]  # Available instances of each resource type
    max_demand = [
        [7, 5, 3],  # Maximum demand for process 0
        [3, 2, 2],  # Maximum demand for process 1
        [9, 0, 2],  # Maximum demand for process 2
        [2, 2, 2],  # Maximum demand for process 3
        [4, 3, 3],  # Maximum demand for process 4
    ]
    allocation = [
        [0, 1, 0],  # Currently allocated resources for process 0
        [2, 0, 0],  # Currently allocated resources for process 1
        [3, 0, 2],  # Currently allocated resources for process 2
        [2, 1, 1],  # Currently allocated resources for process 3
        [0, 0, 2],  # Currently allocated resources for process 4
    ]

    # Run Banker's Algorithm
    safe, safe_sequence = is_safe_state(processes, available, max_demand, allocation)

    # Output
    if safe:
        print("The system is in a safe state.")
        print("Safe sequence:", safe_sequence)
    else:
        print("The system is not in a safe state.")

import threading
import time

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Semaphores
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]
mutex = threading.Semaphore(1)  # Used to prevent deadlock (optional optimization)

def philosopher(philosopher_id):
    left_fork = philosopher_id
    right_fork = (philosopher_id + 1) % NUM_PHILOSOPHERS

    while True:
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(1)  # Simulate thinking

        # Pick up forks
        mutex.acquire()
        print(f"Philosopher {philosopher_id} is hungry.")
        forks[left_fork].acquire()  # Pick up left fork
        print(f"Philosopher {philosopher_id} picked up left fork {left_fork}.")
        forks[right_fork].acquire()  # Pick up right fork
        print(f"Philosopher {philosopher_id} picked up right fork {right_fork}.")
        mutex.release()

        # Eating
        print(f"Philosopher {philosopher_id} is eating.")
        time.sleep(2)  # Simulate eating

        # Put down forks
        forks[left_fork].release()  # Put down left fork
        print(f"Philosopher {philosopher_id} put down left fork {left_fork}.")
        forks[right_fork].release()  # Put down right fork
        print(f"Philosopher {philosopher_id} put down right fork {right_fork}.")

        # Back to thinking
        print(f"Philosopher {philosopher_id} is back to thinking.")

# Main function
if __name__ == "__main__":
    philosophers = []

    # Create philosopher threads
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        philosophers.append(t)

    # Start all threads
    for t in philosophers:
        t.start()

    # Wait for all threads to complete (in this case, they run indefinitely)
    for t in philosophers:
        t.join()

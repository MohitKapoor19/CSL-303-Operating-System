import threading
import time

# Shared variables
read_count = 0
shared_data = 0

# Semaphores
read_count_mutex = threading.Semaphore(1)  # Protects read_count
resource = threading.Semaphore(1)         # Protects the shared resource

def reader(reader_id):
    global read_count
    # Reader's entry section
    read_count_mutex.acquire()
    read_count += 1
    if read_count == 1:
        resource.acquire()  # First reader locks the resource
    read_count_mutex.release()

    # Reading section
    print(f"Reader {reader_id} is reading the shared data: {shared_data}")
    time.sleep(1)  # Simulate reading time

    # Reader's exit section
    read_count_mutex.acquire()
    read_count -= 1
    if read_count == 0:
        resource.release()  # Last reader unlocks the resource
    read_count_mutex.release()

def writer(writer_id):
    global shared_data
    # Writer's entry section
    resource.acquire()

    # Writing section
    shared_data += 1
    print(f"Writer {writer_id} is writing the shared data: {shared_data}")
    time.sleep(1)  # Simulate writing time

    # Writer's exit section
    resource.release()

# Main function
if __name__ == "__main__":
    num_readers = 3
    num_writers = 2

    threads = []

    # Create reader threads
    for i in range(1, num_readers + 1):
        t = threading.Thread(target=reader, args=(i,))
        threads.append(t)

    # Create writer threads
    for i in range(1, num_writers + 1):
        t = threading.Thread(target=writer, args=(i,))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

def fifo(page_sequence, frame_count):
    frames = []
    page_faults = 0
    for page in page_sequence:
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0)  # Remove the oldest page
                frames.append(page)
            page_faults += 1
        print(f"Page: {page} | Frames: {frames}")
    return page_faults


def lru(page_sequence, frame_count):
    frames = []
    page_faults = 0
    for page in page_sequence:
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Remove the least recently used page
                least_recent = min(frames, key=lambda x: page_sequence[:page_sequence.index(page)].count(x))
                frames.remove(least_recent)
                frames.append(page)
            page_faults += 1
        else:
            # Update the recently used order
            frames.remove(page)
            frames.append(page)
        print(f"Page: {page} | Frames: {frames}")
    return page_faults


def optimal(page_sequence, frame_count):
    frames = []
    page_faults = 0
    for i, page in enumerate(page_sequence):
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Find the page not needed for the longest time in the future
                future = page_sequence[i + 1:]
                indices = {frame: future.index(frame) if frame in future else float('inf') for frame in frames}
                to_replace = max(indices, key=indices.get)
                frames.remove(to_replace)
                frames.append(page)
            page_faults += 1
        print(f"Page: {page} | Frames: {frames}")
    return page_faults


if __name__ == "__main__":
    # Input page sequence and frame count
    page_sequence = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_count = 3

    print("FIFO Page Replacement:")
    fifo_faults = fifo(page_sequence, frame_count)
    print(f"Total Page Faults (FIFO): {fifo_faults}\n")

    print("LRU Page Replacement:")
    lru_faults = lru(page_sequence, frame_count)
    print(f"Total Page Faults (LRU): {lru_faults}\n")

    print("Optimal Page Replacement:")
    optimal_faults = optimal(page_sequence, frame_count)
    print(f"Total Page Faults (Optimal): {optimal_faults}\n")

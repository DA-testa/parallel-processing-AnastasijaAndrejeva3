import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)

    jobs = [(t, i) for i, t in enumerate(data)]
    output = []

    while jobs:
        t, i = jobs.pop(0)

        finish_time, thread = heapq.heappop(threads)
        start_time = max(finish_time, t)
        finish_time = start_time + t
        output.append((thread, start_time))

        heapq.heappush(threads, (finish_time, thread))

        while jobs and threads:
            t, i = jobs.pop(0)
            finish_time, thread = heapq.heappop(threads)
            start_time = max(finish_time, t)
            finish_time = start_time + t
            output.append((thread, start_time))
            heapq.heappush(threads, (finish_time, thread))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread, time in result:
        print(thread, time)

if __name__ == "__main__":
    main()

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    start = [0] * m

    jobs = [(t, i) for i, t in enumerate(data)]
    for i in range(n, m+n):
        time, job = heapq.heappop(threads)
        output.append((job, start[job]))
        heapq.heappush(threads, (time + data[job], job))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for couple in result:
        print(couple[0], couple[1])

if __name__ == "__main__":
    main()

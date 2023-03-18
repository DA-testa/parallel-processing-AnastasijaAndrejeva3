import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)
    start = [0] * m

    for i in range(m):
        time, job = heapq.heappop(threads)
        output.append((job, start[job]))
        start[job] += data
        heapq.heappush(threads, (start[job], job))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for couple in result:
        print(couple[0], couple[1])

if __name__ == "__main__":
    main()

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)

    for i, j in range(data):
        time, job = heapq.heappop(threads)
        output.append((job, time)
        heapq.heappush(threads, time + j, job)

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i, j in result:
        print(i,j)

if __name__ == "__main__":
    main()

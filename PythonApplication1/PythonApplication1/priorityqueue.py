import heapq as q
import sys

input = sys.stdin.readline
front = []
end = []

N = int(input().strip())
mid = int(input().strip())
print(mid)

for i in range(2,N+1):
    k = int(input().strip())

    if k < mid:
        q.heappush(front, -k)

        if i%2 == 0:
            q.heappush(end, mid)
            mid = -q.heappop(front)

    else:
        q.heappush(end, k)

        if i%2==1:
            q.heappush(front, -mid)
            mid = q.heappop(end)
        
    print(mid)

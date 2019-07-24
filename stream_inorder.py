import heapq

nums = [3, 2, 5, 4, 1]
heapq.heapify(nums)
mi = 1
while True:
    try:
        if heapq.heappop(nums) == mi:
            print(mi)
            mi += 1
    except:
        continue

import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        heap=[-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if y!=x:
                heapq.heappush(heap,-(y-x))
        return -heap[0] if heap else 0
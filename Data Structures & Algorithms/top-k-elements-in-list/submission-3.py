class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
        
        pq = []
        for a, b in hash.items():
            pq.append((-b, a))
        heapq.heapify(pq)

        res = []
        for a in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
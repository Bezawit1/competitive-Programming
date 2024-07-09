class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k :
            curr = heapq.heappop(piles)
            curr = curr//2
            heapq.heappush(piles , curr)
            k-=1
        return -sum(piles)
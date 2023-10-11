class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n=len(cost)
        cost.sort()
        sum =0
        for i in range(n):
            if i%3 != n%3:
                sum+=cost[i]

        return sum 
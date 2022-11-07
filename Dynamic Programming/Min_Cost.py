class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costArr = [cost[0],cost[1]]
        for i in range (2,len(cost)):
            nextCost = cost[i]
            if costArr[i-2] >= costArr[i-1]:
                nextCost += costArr[i-1]
            else:
                nextCost += costArr[i-2]
            costArr.append(nextCost)
        if costArr[len(costArr)-2] < costArr[len(costArr)-1]:
            return costArr[len(costArr)-2]
        return costArr[len(costArr)-1]
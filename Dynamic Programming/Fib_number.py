class Solution:
    def climbStairs(self, n: int) -> int:
        storage = [1,2]
        if n > 2:
            for i in range(2,n):
                storage.append(storage[i-1] + storage[i-2])
        return storage[n-1]
           
        
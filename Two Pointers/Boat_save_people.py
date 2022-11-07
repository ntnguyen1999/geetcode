class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        firstCounter = 0
        lastCounter = len(people)-1
        count = 0
        while (firstCounter != lastCounter) and (lastCounter != firstCounter + 1):
            if people[firstCounter] + people[lastCounter] > limit:
                count += 1
                lastCounter -= 1
            else: 
                count += 1
                firstCounter += 1 
                lastCounter -= 1
        if (firstCounter != lastCounter) and (people[firstCounter] + people[lastCounter] > limit):
            count += 2
        else: count += 1
        return count    
        
            
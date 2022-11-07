class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if flowerbed == [1]:
            return n == 0;
        elif flowerbed == [0]:
            return n <= 1;
        else:
            for i in range(len(flowerbed)):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        count += 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
            return count >= n
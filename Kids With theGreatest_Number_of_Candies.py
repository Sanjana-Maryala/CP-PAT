class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcand=max(candies)
        res=[]
        for i in candies:
            if i + extraCandies >= maxcand:
                res.append(True)
            else:
                res.append(False)
        return res      
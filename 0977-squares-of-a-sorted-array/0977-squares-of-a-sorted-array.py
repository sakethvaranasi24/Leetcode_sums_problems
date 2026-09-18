class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        p1 = 0
        p2 = len(nums) - 1
        arr = []

        while p1 <= p2:
            arr.append(nums[p1] ** 2)
            p1 += 1

        arr.sort()

        return arr
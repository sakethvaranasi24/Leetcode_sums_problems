class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        p1 = 0
        p2 = 1
        count = 0

        while p2 < len(nums):
            if p1 == p2:
                p2 += 1
                continue
            diff = nums[p2] - nums[p1]

            if diff == k:
                count += 1

                value1 = nums[p1] 
                value2 = nums[p2]

                while p1 < len(nums) and nums[p1] == value1:
                    p1 += 1
                while p2 < len(nums) and nums[p2] == value2:
                    p2 += 1
            elif diff < k:
                p2 += 1
            else:
                p1 += 1

        return count



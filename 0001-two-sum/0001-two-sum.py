class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []

        for i in range(len(nums)):
            arr.append([nums[i], i])

        arr.sort()

        p1 = 0
        p2 = len(arr) - 1

        while p1 < p2:
            if arr[p1][0] + arr[p2][0] == target:
                return [arr[p1][1], arr[p2][1]]

            elif arr[p1][0] + arr[p2][0] < target:
                p1 += 1

            else:
                p2 -= 1
            
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

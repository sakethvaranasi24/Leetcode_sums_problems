class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        used = [False] * len(nums2)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and used[j] == False:
                    result.append(nums1[i])
                    used[j] = True
                    break

        return result
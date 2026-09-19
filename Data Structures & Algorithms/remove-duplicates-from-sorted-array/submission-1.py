class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = list(set(nums))
        nums2.sort()
        k = len(nums2)

        for i in range(k):
            nums[i] = nums2[i]
        return k
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)

        if n==1:
            return nums[0]

        for num in nums:
            if num in count:
                count[num] += 1
                if count[num] > (n/2):
                    return num
            else:
                count[num] = 1

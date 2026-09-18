class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        inital = 0
        final = len(nums)-1

        for i in range(len(nums)):
            while inital<final:
                if nums[inital]>nums[final]:
                    tmp = nums[final]
                    nums[final] = nums[inital]
                    nums[inital] = tmp
                final -= 1
            inital += 1
            final = len(nums)-1

        return nums
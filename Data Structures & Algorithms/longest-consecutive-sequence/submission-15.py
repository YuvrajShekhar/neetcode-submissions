class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        run_sum = 1
        nums.sort()

        if not nums:
            return 0

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                run_sum +=1
            elif nums[i+1] == nums[i]:
                run_sum = run_sum
            else:
                output = max(output,run_sum)
                run_sum = 1
        
        return max(output,run_sum)
    
    [-1,-1,0,]
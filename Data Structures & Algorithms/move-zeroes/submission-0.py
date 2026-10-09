class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        output = []
        count = 0
        for num in nums:
            if num==0:
                count+=1
            else:
                output.append(num)

        for i in range(count):
            output.append(0)

        for i in range(len(nums)):
            nums[i] = output[i]

        print(output)

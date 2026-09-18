class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        output = []
        n = len(nums)/3
        if n<1:
            return list(set(nums))
        for num in nums:
            if num in count:
                count[num] += 1
                if count[num]>n and num not in output:
                    output.append(num)
            else:
                count[num] = 1

        return output
        
        
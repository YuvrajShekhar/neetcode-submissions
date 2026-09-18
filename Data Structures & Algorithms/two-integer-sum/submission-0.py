class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, num in enumerate(nums):
            store[num] = i

        for i, num in enumerate(nums):
            diff = target - num 
            if diff in store and store[diff]!=i:
                return [i,store[diff]]

        return []
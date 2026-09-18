class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dup = set(nums)
        # print(len(nums_dup))
        if (len(nums)==len(nums_dup)):
            return False
        return True

        
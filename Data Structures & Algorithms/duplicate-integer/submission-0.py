class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dup = set()
        for i in nums:
            if i in nums_dup:
                return True
            nums_dup.add(i)

        return False

        
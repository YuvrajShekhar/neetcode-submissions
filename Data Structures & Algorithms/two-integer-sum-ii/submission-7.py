class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0 
        second = len(numbers)-1
        check_sum = 0

        while first<second:
            check_sum = numbers[first] + numbers[second]
            if check_sum==target:
                return [first+1,second+1]
            if check_sum>target:
                second-=1
            if check_sum<target:
                first+=1

        return []

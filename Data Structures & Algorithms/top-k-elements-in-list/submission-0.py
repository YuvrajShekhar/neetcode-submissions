class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        out = []

        for num in nums:
            count[num] = 0

        for num in nums:
            count[num] = 1 + count[num]

        for num,value in count.items():
            res.append([num,value])

        res.sort(key=lambda x:x[1], reverse=True)

        for i in range(k):
            out.append(res[i][0])

        return out

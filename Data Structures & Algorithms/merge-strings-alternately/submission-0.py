class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        start = 0
        output = ""
        if len(word1)>len(word2):
            tmp = word1
        else:
            tmp = word2

        loop_len = min(len(word1),len(word2))
        loop_len_max = max(len(word1),len(word2))

        for i in range(loop_len):
            output += word1[start]
            output += word2[start]
            start += 1

        if len(word1)==len(word2):
            return output

        for i in range(loop_len,loop_len_max):
            output += tmp[i]

        return output

        
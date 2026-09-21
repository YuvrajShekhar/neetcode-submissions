class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        tsum = 0
        for ops in operations:
            if(ops=="+"):
                tmp = int(output[-1]) + int(output[-2]) 
                output.append(tmp)
            elif(ops=="C"):
                output.pop()
            elif(ops=="D"):
                tmp = int(output[-1]) * 2
                output.append(tmp)
            else:
                output.append(int(ops))

        for ele in output:
            tsum+=ele

        return tsum
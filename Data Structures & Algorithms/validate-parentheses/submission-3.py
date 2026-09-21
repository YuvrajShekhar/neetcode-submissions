class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        close = {"(":")",'{' : '}', '[' : ']'}
        for bra in s:
            print(check)
            if not check:
                check.append(bra)
            elif check[-1] in close and close[check[-1]] == bra:
                check.pop()
            else:
                check.append(bra)

        if check:
            return False
        else:
            return True

            
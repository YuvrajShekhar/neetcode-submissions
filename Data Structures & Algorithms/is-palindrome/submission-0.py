class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            # Skip non-alphanumeric characters from the left
            while start < end and not s[start].isalnum():
                start += 1

            # Skip non-alphanumeric characters from the right
            while start < end and not s[end].isalnum():
                end -= 1

            # Compare characters case-insensitively
            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True
# Problem Link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isAlphaNumeric(self, c):
        return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')

    # Time = O(n) memory = O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isAlphaNumeric(s[l]) and l < r:
                l += 1
            while not self.isAlphaNumeric(s[r]) and r > l:
                if r < 0:
                    return False
                r -= 1

            if l > r:
                return False

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True


# More Pythonic version
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        modified = ''.join(char.lower() for char in s if char.isalnum())
        return modified == modified[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(".,"))

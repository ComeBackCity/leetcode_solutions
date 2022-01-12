# Problem Link: https://leetcode.com/problems/roman-to-integer/

class Solution2:
    def __init__(self):
        self.value_map = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        length = len(s)
        num = 0
        i = 0
        for _ in range(length):
            key = s[i] + s[i+1] if i+1 <= length-1 else None
            if i >= length:
                break
            elif key is not None and key in self.value_map:
                num += self.value_map[key]
                i += 2
            else:
                num += self.value_map[s[i]]
                i += 1

        return num


if __name__ == "__main__":
    solution = Solution2()
    result = solution.romanToInt('III')
    print(result)

class Solution(object):
    def isValid(self, s):
        stack = []

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        if len(s) % 2 != 0:
            return False

        for char in s:
            if brackets.get(char) is not None:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char not in brackets.values():
                    return False
                if char != brackets[stack.pop()]: 
                    return False

        return len(stack) == 0

def main(row, want):
    s = Solution()
    res = s.isValid(row)
    if res != want:
        print("mismatch wanted {} and got {}, input: {}".format(want, res, row))

if __name__ == "__main__":
    tests = [
        ["()", True],
        ["()[]{}", True],
        ["(]", False],
        ["([])", True],
        ["([)]", False],
        ["([}}])", False]
    ]
    for test in tests:
        main(test[0], test[1])

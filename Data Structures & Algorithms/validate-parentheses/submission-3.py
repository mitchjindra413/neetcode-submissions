class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        key = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in key:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if prev != key[char]:
                    return False

        return not stack
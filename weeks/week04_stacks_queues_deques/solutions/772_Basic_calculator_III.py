class Solution:
    def calculate(self, s: str) -> int:
        def helper(idx):
            stack = []
            num = 0
            op = '+'

            while idx < len(s):
                char = s[idx]

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num, idx = helper(idx + 1)

                if (not char.isdigit() and char != ' ') or idx == len(s) - 1:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(int(stack.pop() / num))
                    op = char
                    num = 0

                if char == ')':
                    break

                idx += 1

            return sum(stack), idx

        result, _ = helper(0)
        return result
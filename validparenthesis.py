def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:

            # If opening bracket, push
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            else:
                # If stack empty → invalid
                if len(stack) == 0:
                    return False

                top = stack.pop()

                # Check matching
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0
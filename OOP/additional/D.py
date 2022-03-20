class RPN:
    def __init__(self, s: str):
        self.s = s

    def check(self) -> bool:
        if "(" in self.s:
            return True
        return False

    def postfix(self) -> str:
        if not self.check():
            return self.s

        priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}

        stack = []
        output = []

        for ch in self.s.split():
            if ch.isalnum() or ch == " ":
                output.append(ch)
            elif ch == "(":
                stack.append(ch)
            elif ch == ")":
                top = stack.pop()
                while top != "(":
                    output.append(top)
                    top = stack.pop()
            else:
                while (
                    stack
                    and stack[-1] != "("
                    and priority[ch] <= priority[stack[-1]]
                ):
                    output.append(stack.pop())
                stack.append(ch)
        while stack:
            output.append(stack.pop())
        self.s = " ".join(output)
        return " ".join(output)

    def calculate(self) -> float:
        if self.check():
            self.postfix()

        opers = self.s.split()
        opers = list(map(lambda x: int(x) if x.isdigit() else x, opers))

        stack = []
        for exp in opers:
            if type(exp) == str:
                b = stack.pop()
                a = stack.pop()
                if exp == "+":
                    stack.append(a + b)
                elif exp == "-":
                    stack.append(a - b)
                elif exp == "*":
                    stack.append(a * b)
                else:
                    stack.append(a / b)
            else:
                stack.append(exp)

        return float(stack[0])

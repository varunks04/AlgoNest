"""Expression helpers based on stack operations."""

from typing import List

_PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def _is_operator(token: str) -> bool:
    return token in _PRECEDENCE


def valid_parentheses(text: str) -> bool:
    """Validate bracket sequence for (), {}, []."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: List[str] = []

    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack


def infix_to_postfix(expression: str) -> str:
    """Convert space-separated infix expression to postfix."""
    output: List[str] = []
    stack: List[str] = []

    for token in expression.split():
        if token.isnumeric():
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()
        elif _is_operator(token):
            while (
                stack
                and stack[-1] != "("
                and _PRECEDENCE.get(stack[-1], 0) >= _PRECEDENCE[token]
            ):
                output.append(stack.pop())
            stack.append(token)
        else:
            raise ValueError(f"Invalid token: {token}")

    while stack:
        top = stack.pop()
        if top == "(":
            raise ValueError("Mismatched parentheses")
        output.append(top)

    return " ".join(output)


def evaluate_postfix(expression: str) -> float:
    """Evaluate space-separated postfix expression."""
    stack: List[float] = []

    for token in expression.split():
        if token.isnumeric():
            stack.append(float(token))
            continue
        if len(stack) < 2:
            raise ValueError("Invalid postfix expression")
        right = stack.pop()
        left = stack.pop()

        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        elif token == "/":
            if right == 0:
                raise ZeroDivisionError("division by zero")
            stack.append(left / right)
        elif token == "^":
            stack.append(left**right)
        else:
            raise ValueError(f"Unsupported operator: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]

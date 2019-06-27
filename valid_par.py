def is_valid(paren):
    "Returns if the set of parenthesis is valid."
    stack = []
    for i in paren:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    return False


if __name__ == "__main__":
    while True:
        p = input("Enter the parenthesis:")
        print(is_valid(p))

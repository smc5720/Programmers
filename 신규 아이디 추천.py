def solution(new_id):
    stack = []
    
    for i in new_id:
        if "A" <= i and i <= "Z":
            stack.append(str(i).lower())
        else:
            stack.append(i)
    
    tmp = stack[:]
    stack = []

    for i in tmp:
        if i == "-" or i == "_" or i == ".":
            stack.append(i)
        elif "a" <= i and i <= "z":
            stack.append(i)
        elif "0" <= i and i <= "9":
            stack.append(i)

    tmp = stack[:]
    stack = []
    state = False

    for i in tmp:
        if i == ".":
            if state == False:
                state = True
                stack.append(i)
        else:
            state = False
            stack.append(i)

    if stack and stack[0] == ".":
        stack.pop(0)
    
    if stack and stack[-1] == ".":
        stack.pop()

    if not stack:
        stack.append("a")

    if len(stack) >= 16:
        stack = stack[:15]
    
    if stack[-1] == ".":
        stack.pop()

    while len(stack) <= 2:
        stack.append(stack[-1])

    return "".join(stack)
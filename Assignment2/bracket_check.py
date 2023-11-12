from Stack import Stack


# input: str
# output: is_error : boolean
# output: location : int

def bracket_check(str):
    is_error = False
    location = []
    stack = Stack()

    for i in range(len(str)):
        s = str[i]
        if s == '(' or s == '[' or s == '{':
            stack.push((s, i))
        elif s == ')' or s == ']' or s == '}':
            if not stack.isEmpty():
                p, p_position = stack.pop()
            else:
                is_error = True
                location.append(i)
                continue

            if not ((p == '(' and s == ')') or (p == '[' and s == ']') or (p == '{' and s == '}')):
                is_error = True
                location.append(i)

    while not stack.isEmpty():
        p, p_position = stack.pop()
        is_error = True
        location.append(p_position)

    return is_error, location

test_string = '{ (Hello) } ]'
isError, locations = bracket_check(test_string)
print(f'Error: {isError}')
print('Location: ', locations)

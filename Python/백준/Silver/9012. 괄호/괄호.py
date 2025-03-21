import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().strip()
    stack = []
    is_vps = True

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if stack:
        is_vps = False

    print("YES" if is_vps else "NO")
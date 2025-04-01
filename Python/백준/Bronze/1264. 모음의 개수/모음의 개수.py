while True:
    line = input()
    if line == '#':
        break
    count = 0
    for char in line:
        if char.lower() in 'aeiou':
            count += 1
    print(count)

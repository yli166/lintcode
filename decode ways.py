def num(s):
    if s[0] == '' or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2 and s[:] > '27':
        return 1
    if len(s) == 2 and s[:] < '10':
        return 1
    if len(s) == 2 and s[:] < '27':
        return 2
    if len(s) > 1 and s[-1] == '0':
        if s[-2] == '0' or s[-2] > '2':
            return 0
        else:
            return num(s[:-1])
    if len(s) > 1 and s[-2:] > '27':
        return num(s[:-1])
    if len(s) > 1 and s[-2:] < '10':
        return num(s[:-1])
    return num(s[:-1]) + num(s[:-2])

test = num('12')

print(test)
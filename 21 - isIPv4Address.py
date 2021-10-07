def isIPv4Address(inputString):
    s = inputString.split('.')
    for i in s:
        if i == '00':
            return False
        elif i.startswith('0') and len(i) > 1:
            return False
        if not i.isdecimal():
            return False
    num = [int(x) for x in s]
    cond = max(num) <= 255 and min(num) >= 0 and len(num) == 4
    
    return cond

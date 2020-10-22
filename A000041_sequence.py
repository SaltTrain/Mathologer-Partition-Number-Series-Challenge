
def subsub_pattern(i):
    n = i-1
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n%2 == 0:
        return subsub_pattern(i-2) + 1
    if n%2 != 0:
        return subsub_pattern(i-2) + 2

def sub_pattern(i):
    n = i-1
    if n == 0:
        return 1
    return sub_pattern(n) + subsub_pattern(n)

def pattern(i,data={}):
    ans = 0
    indexes = []
    n = i-1

    if n in(0,1):
        return 1
        
    if i in data:
        return data[i]

    for j in range(1,i):
        indexes.append(sub_pattern(j))

    flip = False
    for j in range(0,len(indexes),2):
        if indexes[j] < i:
            if flip:
                ans -= pattern(i-indexes[j], data)
                if (j+1) < len(indexes):
                    ans -= pattern(i - indexes[j+1], data)
                flip = False
            else:
                ans += pattern(i - indexes[j], data)
                if (j+1) < len(indexes):
                    ans += pattern(i - indexes[j+1], data)
                flip = True
    return ans

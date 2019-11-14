def r(lis):
    if len(lis) == 0:
        return []
    else:
        return r(lis[1:]) + [lis[0]]

l = [1,2,3,4,5]
print(r(l))
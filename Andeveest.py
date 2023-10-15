n = int(input())
array = [0 for x in range(201)]

for i in range (0,n) :
    args = input().split()
    f = str(args[0])
    y = int(args[1])
    if f == '+':
        pick = array[y]
        array.pop(y)
        array.insert(y, pick +1)
    elif f == '?':
        print(array[y])

# another format
# n = int(input())
# a = [0 for i in range(201)]
# for i in range(n):
#     b = input().split()
#     if b[0] == '+':
#         a[int(b[1])] += 1
#     if b[0] == '?':
#         print(a[int(b[1])])

# example delete () for ?
# 6
# + 1
# (?) 1
# + 200
# (?) 2
# + 200
# (?) 200

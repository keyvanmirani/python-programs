n = int(input())
array = []

for i in range (1,n+1) :
    args = input().split()
    f = str(args[0])
    y = int(args[1])
    x = int(args[2]) if len(args) > 2 else ''
    if f == '+':
        array.insert(y - 1, x)
    elif f == '-':
        array.pop(y - 1)
    if array:
        print(*array)
    else:
        print("EMPTY")

# 7
# + 1 1
# + 2 3
# + 2 10
# + 4 5
# + 2 100
# - 2
# - 2
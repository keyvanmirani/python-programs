n, m = map(int, input().split())

array1 = [[int(i) for i in input().split()[:n]] for i in range (n)]
array2 = [[int(i) for i in input().split()[:2]] for i in range (m)]

sum = 0
for i in range (0 , m) :
    x = array2[i][0]
    y = array2[i][1]
    sum += array1[x - 1][y - 1]

print(sum)

# 3 3
# 1 50 66
# 72 1 12
# 91 29 1
# 1 3
# 2 3
# 3 1
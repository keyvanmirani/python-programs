n, m = map(int, input().split())

f_list = [[int(j) for j in input().split()[:m]] for i in range(n)]
s_list = [[int(j) for j in input().split()[:m]] for i in range(n)]

result = [[f_list[i][j] + s_list[i][j]  for j in range
(len(f_list[0]))] for i in range(len(f_list))]

for i in result:
    for j in i:
        print(j, end=" ")
    print()


# 2 3
# 1 2 3
# 4 5 6
# 2 3 4
# 5 6 7
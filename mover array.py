n, x = map(int ,input().split())
mover_array = list(map(int, input().split()))
mover_array = mover_array[:n]

for i in range (0, x):
    spliter = mover_array.pop()
    mover_array[:0] = [spliter]

print(*mover_array)
# 4 1
# 1 2 3 4
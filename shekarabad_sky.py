n,m = map(int, input().split())
count = 0

for i in range (n):
    array = [str(n) for n in input()[:m]]
    for j in array:
       if j == "*":
          count += 1

print(count)

# for input * remove (
# 5 1
# .
# o
# .
# o
# (*
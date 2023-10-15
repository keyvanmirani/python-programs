N = int(input())
input_array = [int(i) for i in input().split()[:N]]
c_array = [0 for x in range(101)]
default_min = 100
res = 0

for i in range (N):
    c_array[input_array[i]] += 1

for i in range(len(c_array)):
    if c_array[i] !=0 and c_array[i] < default_min:
        default_min = c_array[i]
        res = i

print(res)

#5
# 1 1 2 3 4

#4
# 1 1 2 2
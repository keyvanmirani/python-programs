n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in range(n):
    print(f"{arr1[i] + arr2[i]}", end = ' ')
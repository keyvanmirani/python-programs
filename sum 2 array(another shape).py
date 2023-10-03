value = int(input())
first_list = [int(value) for value in input().split()]
second_list = [int(value) for value in input().split()]
first_list = first_list[:value+1]
second_list = second_list[:value+1]
sum_array = []
for i in range(0, len(first_list)):
    sum = first_list[i] + second_list[i]
    sum_array.append(sum)

print(*sum_array)
value = int(input())
first_list = [str(value) for value in input()[:value]]
second_list = [str(value) for value in input()[:value]]
sum = 0
for i in range(0, len(first_list)):
    if first_list[i] != second_list[i]:
        sum =+ 1

print(sum)


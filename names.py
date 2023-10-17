n = int(input())
list = []

#remove duplicate character in list
def remove_duplicate (list):
    result = [] 
    [result.append(x) for x in list if x not in result] 
    return result
#maximum length in list
def get_length_of_longest_list(list):
    return max(len(x) for x in list)
#input for user
for i in range (n) :
    name = [str(x) for x in input()]
    name2 = remove_duplicate(name)
    list.append(name2)


print(get_length_of_longest_list(list))

#another solution
# n = int(input())
# list = []

# #remove duplicate character in list
# def remove_duplicate (list):
#     result = [] 
#     [result.append(x) for x in list if x not in result] 
#     return result
# #maximum length in list
# def get_length_of_longest_list(list):
#     return max(lst, key=len)
# or use this code :)
#     # longest = list[0] if list else None
#     # for x in list:
#     #     if len(x) > len(longest):
#     #         longest = x
#     # return longest

# #input for user
# for i in range (n) :
#     name = [str(x) for x in input()]
#     name2 = remove_duplicate(name)
#     list.append(name2)


# print(get_length_of_longest_list(list))


# 4
# ali
# karim
# abbas
# mohammad

# 5
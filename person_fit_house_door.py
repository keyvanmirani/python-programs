#input person and house door (person first)
house_width, house_height = map(int, input().split())
person_width, person_height = map(int, input().split())

#calculate can cross or not
if  (house_width >= person_width and house_height >= person_height) :
    print("yes")
else :
    print("no")

print (house_width >= person_width and house_height >= person_height)
print(person_width, person_height,house_width, house_height)
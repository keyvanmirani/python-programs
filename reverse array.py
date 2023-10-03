list = []
i = 0
while  True : 
    n = int(input())
    if n != 0 :
        list.append(n)
        i += 1
    else :
        break

while i > 0 :
    print(list.pop())
    i -= 1

#another shape
arraye_moratab = list()
while True:
    vorodi = int(input())
    if(vorodi == 0):
        break;
    arraye_moratab.append(vorodi)
    
for i in  arraye_moratab[::-1]:
    print(i)
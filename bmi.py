weight = int(input())
height = float(input())

height_rounded = format(height,".2f")

def bmi (weight , height_rounded ):
    bmi = weight / (float(height_rounded)**2)
    if bmi <= 18.4:
        print(format(bmi,".2f"),"\nUnderweight")
    elif bmi <= 24.9:
        print(format(bmi,".2f"),"\nNormal")
    elif bmi <= 29.9:
        print(format(bmi,".2f"),"\nOverweight")
    else:
        print(format(bmi,".2f"),"\nObese")
    

print(bmi(weight, height_rounded))
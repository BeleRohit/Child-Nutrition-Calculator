name = input("Enter the name of the child ")
age = int(input("Enter the age of the child in years "))
gender = input("Enter the gender of the child ")
Height = int(input("Enter the height of the child in inches "))
Weight = int(input("enter the weight of the children in lbs(pounds) "))
print('________________________________________________________________________')

def BMI():
    BMI = Weight / (Height ** 2) * 703
    print(BMI)
    if BMI < 16:
        return "Severely Underweight"
    elif 16 <= BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Healthy"
    elif 25 <= BMI < 30:
        return "Overweight"
    elif BMI >= 30:
        return "Obese"

print('________________________________________________________________________')

if (0 < age < 2):
    print("Minimum calories required daily for the child is", 800)
elif (2 < age < 4):
    print("Minimum calories required daily for the child is", 1400)
elif (4 < age < 8):
    print("Minimum calories required daily for the child is", 1800)
print('________________________________________________________________________')

print("Enter the quantities of the following items in grams")
milk = int(input("milk "))
egg = int(input("egg "))
rice = int(input("rice "))
lentils = int(input("lentils "))
vegetable = int(input("vegetables "))
meat = int(input("meat "))
totalCalorie = milk * 1 + egg * 1.55 + rice * 1.3 + lentils * 1.13 + vegetable * 0.85 + meat * 1.43
print(totalCalorie)
print('________________________________________________________________________')
a=''
if 0<age<=2:
    if(totalCalorie<=800):
        a='underNourished'
    else:
        a='Nourished'
elif(2<age<=4):
    if(totalCalorie<=1400):
        a='underNourished'
    else:
        a = 'Nourished'
elif 4<age<=8:
    if (totalCalorie <= 1800):
        a = 'underNourished'
    else:
        a = 'Nourished'

print('________________________________________________________________________')
print("Name:",name)
print("Age:",age)
print("Gender:",gender)
print("Weight:",Weight)
print("Height:",Height)
print("BMI :",BMI())
print("Total Calories eaten:",totalCalorie)
print("is nourished:",a)





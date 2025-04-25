weight = float(input("your weight in kg"))
height = float(input("your height in meter"))
bmi = weight / (height**2)
if bmi > 30:
    category = "obese"
elif bmi < 18.5:
    category = "underweight"
else:
    category = "normal"
print("your bmi is" + str(bmi) + ", you are " + category) 
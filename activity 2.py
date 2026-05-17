height = float(input("Enter ur height in cm:"))
weight = float(input("Enter ur weight in kg:"))
BMI = weight / (height/100)**2
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("Ur underweight")
elif BMI <= 24.9:
    print("Ur overweight")
elif BMI <= 34.9:
    print("Ur severly overweight")
elif BMI <= 39.9:
    print("Ur obese")
else:
    print("Ur severly obese")

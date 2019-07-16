weight = float(input("Nhập cân nặng của bạn (theo đơn vị kg) "))
height = float(input("Nhập chiều cao của bạn (theo đơn vị cm) "))
BMI = weight / height / height *100*100
if BMI <= 15:
    print('Very severely underweight') 
elif 15 < BMI <= 16:
    print('Severely underweight')
elif 16 < BMI <= 18.5:
    print('Underweight')
elif 18.5 < BMI <= 25:
    print('Normal (Healthy weight)')
elif 25 < BMI <= 30:
    print('Overweight')
elif 30 < BMI <= 35:
    print('Moderately obese')
elif 35 < BMI <= 40:
    print('Severely obese')
else:
    print('Very severely obese')
print('Your BMI is ',BMI)
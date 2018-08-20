h = int(input ("What is your height (cm)?"))
w = int(input ("What is your weight (kg)?"))
h_m = h/100
BMI = w / (h_m*h_m)
print ("BMI: ", BMI)
if BMI <16:
    print ("Severly underweight")
elif BMI <= 18.5:
    print ("Underweight")
elif BMI <= 25:
    print ("Normal")
elif BMI <= 30:
    print ("overweight")
else:
    print ("obese")
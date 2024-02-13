weight=int(input("Input weight:"))
height=float(input("Input height:"))
BMI= int(weight/(height*height))
print("Your BMI is", BMI)
if BMI >=30:
    print("Sorry but you're overweight!")
elif BMI >=18:
    print("You are good to go >=<")
else:
    print("You are underweight!")
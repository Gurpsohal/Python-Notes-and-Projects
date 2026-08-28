weight = float(input("Please enter your weight"))
unit = input("Please share the unit K or L").lower()
unit_desired = input("What unit are you intendign to convert to? K or L").lower()

if unit == "k" and unit_desired == "l":
    calc = weight * 2.205
    r_calc = round(calc,2)
    print (f'You weight in LBS is {r_calc}')
elif unit == "l" and unit_desired == "k":
    calc = weight/2.205
    r_calc = round(calc,2)
    print (f'Your weight in kg is {r_calc}')
elif unit == unit_desired:
    print("You already have your desired out come")
else:
    print("Please select a recognized unit")
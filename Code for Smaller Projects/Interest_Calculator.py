principle =0 
rate = 0
time = 0

while True:
    principle = float(input("What is your principal amount?"))
    if principle <= 0:
        print("Please pick a valid principal amount")
    else:
        break

while True:
    rate = float(input("What is your interest rate?"))
    if rate <= 0: 
        print ("Please pick a valid interest rate, as a whole")
    else: 
        break

while True:
    time = int(input("What is the time period you own the loan?"))
    if time <= 0:
        print("Pick a valid time block (Years)")
    else:
        break


total_amount = principle*pow((1+rate/100),time)

print(f" Balance after {time} years: ${total_amount:.2f}")
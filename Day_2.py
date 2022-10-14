print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = (percent / 100) * total
bill = total + tip
each_bill = "{:.2f}".format(bill / people)

print(f"Each person should pay: ${each_bill}")

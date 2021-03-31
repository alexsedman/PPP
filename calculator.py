import os
portfolio = float(0)
invested = 0
counter = 0

print("Starting date: 2021")
month = int(input("How many months passed? "))

while counter != month:
    counter += 1
    if counter == 1:
        portfolio = round(portfolio + 1000.0, 2)
        invested += 1000
    else:
        portfolio = round(portfolio + 100.0, 2)
        invested += 100
    portfolio = round(portfolio * 1.02, 2)
    print("Month " + str(counter) + " portfolio value: " + str(portfolio))
    print("Month " + str(counter) + " amount invested: " + str(invested))

print("Portfolio Value: " + str(portfolio))
print("Amount Invested: " + str(invested))
profit = round(portfolio - invested, 2)
print("Profit: " + str(profit))
input("Press enter to continue")

#(counter - 1) % 12 == 0

import os
portfolio = 0
invested = 0
counter = 0

print("Starting date: 2021")
month = input("How many months past? ")

while counter != month:
    if (month - 1) % 12 == 0 or month == 1:
        portfolio += 1000
        invested += 1000
    else:
        portfolio += 100
        invested += 100
    portfolio *= 1.02
    counter += 1

print("Portfolio Value: " + portfolio)
print("Amount Invested: " + invested)
profit = portfolio - invested
print("Profit: " + profit)
os.system("pause")

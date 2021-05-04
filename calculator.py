portfolio = 0
invested = 0
counter = 0

print("Starting date: 2021")
print("Initial investment: 1100")
print("Monthly investment: 100")
print("Interest: 1.02")
month = int(input("How many months passed? "))

while counter != month:
    counter += 1
    if counter == 1:
        portfolio += 1100
        invested += 1000
    else:
        portfolio += 100
        invested += 100
    portfolio *= 1.02
    portfolio = int(portfolio)
    print("Month " + str(counter) + " portfolio value: " + str(portfolio))

print("Portfolio Value: " + str(portfolio))
print("Amount Invested: " + str(invested))
profit = portfolio - invested
print("Profit: " + str(profit))
input("Press enter to continue... ")

"""4. Write a program which accept principle, rate and time from user and print the simple interest. The formula to calculate simple interest is: simple interest = principle x rate x time / 100 """
principle = float(input("Enter principle amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time(years): "))

simple_interest= principle*rate*time/100

print("Simple interest of ",principle," over a time period of",time,"years is",simple_interest)


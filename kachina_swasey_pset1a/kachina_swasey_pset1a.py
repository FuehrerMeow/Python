
#total_cost = float(input("Please enter the total cost of your dream home: "))
#annual_salary = float(input("Please enter your salary: "))
#portion_saved = float(input("How much do you want to save annually: "))
total_cost = 95000
annual_salary = 83700
portion_saved = 6833.33
portion_down = (total_cost*.25)
current_savings = 0
monthly_salary = (annual_salary/12)
interest_rate = .04

# use +=, or = current savings + 1
months = 1

while current_savings < portion_down:
    current_savings += current_savings * (.4 / 12)
    current_savings += portion_saved
    months += months + 1

print("It will take", months, "months")

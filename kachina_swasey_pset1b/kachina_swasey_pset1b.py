

total_cost = float(input("Please enter the total cost of your dream home: "))
annual_salary = float(input("Please enter your salary: "))
portion_saved = float(input("How much do you want to save annually: "))
semi_annual_raise = float(input("Please enter your raise as a decimal: "))
portion_down = (total_cost*.25)
current_savings = 0
monthly_salary = (annual_salary/12)
interest_rate = .04
portion_saved_monthly = monthly_salary*portion_saved
# use +=, or = current savings + 1
months = 0 # months = 1 gave the wrong info to pycharm (off by 1 error)

while current_savings < portion_down:
    current_savings = current_savings + (current_savings*(0.04/12)) + portion_saved_monthly
    if months != 0 and months %6 == 0: # added months not = 0 to this line
        annual_salary = annual_salary + (annual_salary*semi_annual_raise)
        monthly_salary = annual_salary / 12
        portion_saved_monthly = monthly_salary*portion_saved
    months = months + 1
print("It will take", months, "months")

# Test Case 2
# Enter your starting annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .1
# Enter the cost of your dream home: 800000
# Enter the semiannual raise, as a decimal: .03
# Number of months: 159
#
# Test Case 3
# Enter your starting annual salary: 75000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 1500000
# Enter the semiannual raise, as a decimal: .05
# Number of months: 261
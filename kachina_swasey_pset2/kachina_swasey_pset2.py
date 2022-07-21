
# • Your semi-annual raise is .07 (7%)
# • Your investments have an annual return of 0.04 (4%)
# • The down payment is 0.25 (25%) of the cost of the house
# • The cost of the house that you are saving for is $500,000.

# You are now going to try to find the best rate of savings to achieve a down payment on a
# $500,000 house in 36 months. Since hitting this exactly is a challenge, we simply want
# your savings to be within $100 of the required down payment.

# Write a program to calculate the best savings rate, as a function of your
# starting salary. You should use bisection search to help you do this efficiently. You
# should keep track of the number of steps it takes your bisections search to finish.

# Enter the starting salary: 80000
# Best savings rate: 0.4135 -- 0.4138
# Steps in bisection search: 11

# Enter the starting salary: 150000
# Best savings rate: 0.2206 -- 0.2204
# Steps in bisection search: 9 -- 12

# Enter the starting salary: 10000
# It is not possible to pay the down payment in three years.


base_annual_salary = float(input('What is your annual salary: '))

portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
total_cost = 500000
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
months = 36
current_savings = 0.0
error = 100

uppermost_bound = 10000
upper_bound = uppermost_bound
lower_bound = 0
portion_saved = (upper_bound + lower_bound) // 2
steps = 0

while abs(current_savings - down_payment) > error:
    steps += 1
    current_savings = 0.0
    annual_salary = base_annual_salary
    monthly_salary = annual_salary / 12
    monthly_deposit = monthly_salary * (portion_saved / 10000)
    for month in range(1, months + 1):
        current_savings *= 1 + monthly_rate_of_return
        current_savings += monthly_deposit

        if month % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)
    prev_portion_saved = portion_saved
    if current_savings > down_payment:
        upper_bound = portion_saved
    else:
        lower_bound = portion_saved
# if the solution is outside of the search space on the upper_bound bound, lower_bound
# will eventually equal the inital upper_bound value. However, if we use integer
# division, lower_bound will be one less than upper_bound. As such, we round the average
# of upper_bound and lower_bound and cast to an int so that lower_bound and upper_bound will converge
# completely if the solution is outside of the search space on the upper_bound
# bound
# if portion_saved is no longer changing, our search space is no longer
# changing (because the search value is outside the search space), so we
# break to stop an infinite loop

    portion_saved = int(round((upper_bound + lower_bound) / 2))

    if prev_portion_saved == portion_saved:
        break

if prev_portion_saved == portion_saved and portion_saved == uppermost_bound:
    print('It is impossible to achieve the down payment in three years.')
else:
    print('Best savings rate:', portion_saved / 10000)
    print('Steps in search:', steps)
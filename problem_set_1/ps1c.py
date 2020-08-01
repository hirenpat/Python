#ps1c

starting_salary = float(input('Enter the starting salary: '))
saving_rate = 0

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25*total_cost
monthly_salary = starting_salary/12
r = 0.04

number_of_months = 0
total_salary = 0

while number_of_months < 36:
    if number_of_months % 6 == 0:
        monthly_salary = monthly_salary + (monthly_salary*semi_annual_raise)
    total_salary = total_salary + monthly_salary
    number_of_months += 1

# print('Total salary: ', total_salary)
# print('portion down payment: ', portion_down_payment)

high = 100
low = 0
mid = int((high + low) / 2)

Steps_in_bisection_search = 0

total_saving = (total_salary * (mid/100))

if total_salary < portion_down_payment:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs(portion_down_payment - total_saving) > 100:

        Steps_in_bisection_search += 1

        if portion_down_payment < total_saving:
            high = mid
        else:
            low = mid

        mid = ((high + low) / 2)
        total_saving = (total_salary * (mid/100))

    saving_rate = mid
    print('Steps in bisection search: ', Steps_in_bisection_search)
    print('Best savings rate: ', saving_rate/100)

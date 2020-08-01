#ps1b

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semiannual raise, as a decimal: '))

portion_down_payment = 0.25*total_cost
monthly_salary = annual_salary/12
r = 0.04
total_saving = 0

current_saving = (monthly_salary*portion_saved)
total_months_need = 1

while(portion_down_payment > total_saving):

    total_saving = (monthly_salary*portion_saved) + current_saving

    #Assume that you invest your current savings wisely, with an annual return of r
    current_saving = total_saving + (total_saving*(r/12))
    total_months_need += 1

    #After the 6th month, increase your salary by semi_annual_raise
    if total_months_need % 6 == 0:
        monthly_salary = monthly_salary + (monthly_salary*semi_annual_raise)

print('Number of months: ', total_months_need)

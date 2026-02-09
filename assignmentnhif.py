# Store gross salary in a variable
gross_salary = 45000   # You can change this value

# Determine monthly contribution
if gross_salary >= 99999:
    contribution = gross_salary * 0.20   # 20%
elif gross_salary <= 99998 and 50000:
    contribution = gross_salary * 0.10  # 15%
elif gross_salary <= 49999 and 30000:
    contribution = gross_salary * 0.10   # 10%
elif gross_salary <=29999 and 25000:
    contribution = gross_salary * 0.85 # 8.5%
elif gross_salary <=24999 and 20000:
    contribution = gross_salary * 0.75 # 7.5%
elif gross_salary <=19999 and 15000:
    contribution = gross_salary * 0.6 # 6%
elif gross_salary <=14999 and 12000:
    contribution = gross_salary * 0.5 # 5%
elif gross_salary <=11999 and 8000:
    contribution = gross_salary * 0.4 # 4%
elif gross_salary <=7999 and 6000:
    contribution = gross_salary * 0.3 # 3%
elif gross_salary <=5999:
    contribution = gross_salary * 0.15 # 1.5%
else:
    contribution = gross_salary * 0.20   # 20%

# Display results
print("Gross Salary:", gross_salary)
print("Monthly Contribution:", contribution)
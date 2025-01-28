#Here we have the condition of non progressivity

print("Good morning, how can I help you with calculating your Net Salary?")

try:
    # Inputs used
    salary_gross = input("Input your gross salary: ")
    salary_gross = int(salary_gross)
    number_children = input("How many kids do you have? ")
    number_children = int(number_children)

    rate_tax = 0

    # The base tax rate
    if salary_gross < 1000:
        rate_tax = 0.10
    elif salary_gross < 2000:
        rate_tax = 0.12
    elif salary_gross < 4000:
        rate_tax = 0.14
    else:
        rate_tax = 0.18

    # Calculating the tax cut based on the number of children
    if salary_gross < 2000:
        taxx_cut = number_children * 0.01
    if salary_gross > 2000:
        taxx_cut = number_children * 0.005

    # Ensuring the tax cut does not make the tax rate negative
    rate_tax -= taxx_cut
    if rate_tax < 0:
        rate_tax = 0

    # Calculating the net salary
    net_salary = salary_gross * (1 - rate_tax)

    print("Your net salary is: ", round(net_salary, 2))

except ValueError:
    print("Invalid input. Please type your gross salary numerically and the number of kids you have.")
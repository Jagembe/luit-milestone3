# Salary calculator
hours = float(input("How many hours did you work last month? "))
rate = float(input("What is your hourly rate? "))
salary = (hours * rate * 12)
print("Last month, you earned", hours * rate,"dollars. Your yearly salary before taxes is", salary,"dollars.")
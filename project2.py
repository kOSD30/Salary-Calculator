print('=== Калькулятор зарплаты ===')

salary = float(input('Введите почасовую ставку: '))
hours_worked = float(input('Введите сколько часов вы отработали: '))
tax_free = 550

before_tax = salary * hours_worked
after_tax1 = before_tax * 0.895
after_tax2 = tax_free + (after_tax1 - tax_free) * 0.77

print(f'Зарплата до уплаты налогов: {before_tax:.2f}$')
print(f'Зарплата после уплаты налогов: {after_tax2:.2f}$')
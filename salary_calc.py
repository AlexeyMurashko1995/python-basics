count_workers = int(input('Введите количество сотрудников, работающих в Вашей компании: '))
total_seniors = 0
total_salary = 0

for worker in range(1, count_workers + 1):
    salary = int(input(f'Введите зарплату сотрудника №{worker}: '))
    total_salary += salary
    if salary >= 10000:
        total_seniors += 1

print(f'Расходы на зарплаты в этом месяце: {total_salary}.')
print(f'Старших сотрудников в компании: {total_seniors}.')
print(f'Средняя зарплата сотрудника: {total_salary / count_workers}.')

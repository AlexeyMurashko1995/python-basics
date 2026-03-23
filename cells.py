boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
results_list = []
if boys > 2 * girls or girls > boys * 3:
    print('Решения не найдено.')
elif boys >= girls:
    k = boys - girls
    for bgb in range (k):
        results_list.append('BGB')
    for bg in range (girls - k):
        results_list.append('BG')
else: 
    k = girls - boys
    for gbg in range (k):
        results_list.append('GBG')
    for gb in range (boys - k):
        results_list.append('GB')
final_answer = ''.join(results_list)
print(final_answer)
    
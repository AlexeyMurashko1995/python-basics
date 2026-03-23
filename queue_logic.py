# Get input from the user
boys = int(input('Enter the number of boys: '))
girls = int(input('Enter the number of girls: '))

results_list = []

# Check if a solution is possible (Business logic)
if boys > 2 * girls or girls > boys * 2:
    print('No solution found.')
    
elif boys >= girls:
    # If there are more boys, we use BGB as a base unit
    diff = boys - girls
    for _ in range(diff):
        results_list.append('BGB')
    for _ in range(girls - diff):
        results_list.append('BG')
        
else: 
    # If there are more girls, we use GBG as a base unit
    diff = girls - boys
    for _ in range(diff):
        results_list.append('GBG')
    for _ in range(boys - diff):
        results_list.append('GB')

# Join all parts into a single string and output
final_answer = ''.join(results_list)
print(final_answer)
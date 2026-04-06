lower_bound = 0
upper_bound = 4

target_danger_level = float(input('Enter the maximum allowed danger level: '))

while (upper_bound - lower_bound) > 0.0001:
    mid_point = (upper_bound + lower_bound) / 2
    current_danger_level = (mid_point ** 3) - (3 * (mid_point ** 2)) - (12 * mid_point) + 10

    if target_danger_level > current_danger_level:
        upper_bound = mid_point
    else:
        lower_bound = mid_point

print(f"\nThe required safe depth is approximately: {mid_point:.4f}")
print('*' * 30)
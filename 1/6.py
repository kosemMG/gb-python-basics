distance = float(input('Enter the distance an athlete ran at the first day: '))
interest_distance = float(input('Enter the distance you are interested in: '))

day = 1

while distance < interest_distance:
    distance = distance * 1.1
    day += 1

print(f'An athlete will achieve his goal (not less than {interest_distance:0.1f} km) on the {day} day.')

rating = [7, 5, 3, 3, 2]

new_value = int(input('Please, enter a natural number: '))

rating_length = len(rating)

for i, number in enumerate(rating):
    if new_value > number:
        rating.insert(i, new_value)
        break

if len(rating) == rating_length:    # if the list wasn't changed
    rating.append(new_value)

print(f'New rating: {rating}')

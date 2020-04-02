time = int(input('Please, enter time in seconds: '))

hh = time // 3600
mm = time // 60 - hh * 60
ss = time % 60

print(f'The formatted time is {hh:02}:{mm:02}:{ss:02}')

import io
import os

def get_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    with io.open(os.path.join(script_dir, 'Day1Data.txt'), "r") as file:
        return [line.strip() for line in file.readlines()]
data = get_data()


spinCounter: int = 0
dial: int = 50
zeros = 0

for line in data:
    initDial = dial
    move = int(line[1:])

    if line[0] == 'R':
        dial = (dial + move) % 100
    else:
        dial = (dial - move) % 100

    if dial == 0: zeros += 1
    print(f'{initDial} - {line} - {dial}')
    spinCounter += 1

print(spinCounter)
print(zeros)





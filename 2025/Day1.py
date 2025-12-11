import io
import os

def get_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    with io.open(os.path.join(script_dir, 'Day1Data.txt'), "r") as file:
        return [line.strip() for line in file.readlines()]
data = get_data()


spinCounter = 0
dialPos = 50
zeros = 0

for spin in data:
    initPos = dialPos

    if dialPos == 0: zeros += 1
    num = int(spin[1:3])

    if spin[0] == 'R':
        if dialPos + num > 99:
            dialPos = 0 + (99 - num)
        else:
            dialPos += num
    else:
        if dialPos - num < 0:
            dialPos = 99 - num
        else:
            dialPos -= num
    
    print(f'{initPos} - {spin} - {dialPos}')
    spinCounter += 1

print(spinCounter)
print(zeros)
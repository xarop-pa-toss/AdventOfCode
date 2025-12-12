from pathlib import Path
import math

data: list[str] = (lambda: Path(__file__).with_name('Day1Data.txt').read_text(encoding="utf-8").splitlines())()
spinCounter: int = 0
dial: int = 50
zeroes: int = 0

# Part 1
for line in data:
    initDial = dial
    move = int(line[1:])

    if line[0] == 'R':
        dial = (dial + move) % 100
    else:
        dial = (dial - move) % 100

    if dial == 0: zeroes += 1
    spinCounter += 1

    print(f'{initDial} - {line} - {dial}')
    spinCounter += 1

print('Part 1 zeros: ' + str(zeroes))

print('')
print('--- PART 2 ---')
# Part 2
# Situations where dial will touch 0
# 1 - Ends on 0
# 2 - Crosses 0 going right or left
#   If we think of 0 as a multiple of 100, we can move from dialPos to dialPos +/- move and check for multiples of 100 in a straight line
dial: int = 50
zeroes: int = 0

for line in data:
    move = int(line[1:])

    if line[0] == 'R':
        end_pos: int = dial + move
        multiples_of_100: int = math.floor(end_pos / 100) - math.floor(dial / 100)
        
        dial = (end_pos) % 100
        zeroes += multiples_of_100
    else:
        end_pos: int = dial - move
        multiples_of_100: int = math.floor(dial / 100) - math.floor(end_pos / 100)
        
        dial = (end_pos) % 100
        zeroes += multiples_of_100

print(zeroes)
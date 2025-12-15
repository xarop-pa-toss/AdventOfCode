from pathlib import Path
import math

data: list[str] = (lambda: Path(__file__).with_name('Day1Part2TestData.txt').read_text(encoding="utf-8").splitlines())()

# Part 1
dial: int = 100000050
zeroes: int = 0

for line in data:
    initDial = dial
    move = int(line[1:])
    mult = 1 if line[0] == 'R' else -1

    end_pos = dial + mult * move
    dial = end_pos % 100

    if dial == 0:
        zeroes += 1

    print(f'Rotating {line[0]} by {move}, dial now at {dial}')

print('Part 1 zeros: ' + str(zeroes))

print('')
print('--- PART 2 ---')

# Part 2: count times the dial hits 0 while moving along the straight line
dial: int = 50
zeroes: int = 0

for line in data:
    initDial = dial
    move = int(line[1:])
    mult = 1 if line[0] == 'R' else -1

    end_pos = dial + mult * move

    if mult == 1:
        multiples_of_100 = math.floor(end_pos / 100) - math.floor(dial / 100)
    else:
        multiples_of_100 = math.floor(dial / 100) - math.floor(end_pos / 100)

    dial = end_pos % 100
    if dial == 0 and (end_pos > 100 or end_pos < 0):
        multiples_of_100 += 1
    zeroes += multiples_of_100

    print(f'Rotating {line[0]} by {move}, dial now at {dial}')

print(zeroes)
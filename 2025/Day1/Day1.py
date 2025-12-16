from pathlib import Path
import math

data: list[str] = (lambda: Path(__file__).with_name('Day1Data.txt').read_text(encoding="utf-8").splitlines())()

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
dial: int = 50
zeroes: int = 0

for line in data:
    initDial = dial
    move = int(line[1:])
    mult = 1 if line[0] == 'R' else -1

    # step by step simulation
    for _ in range(move):
        dial += mult
        if (dial % 100) == 0:
            zeroes += 1

    dial = dial % 100
    print(f'Rotating {line[0]} by {move}, dial now at {dial}')

print(zeroes)
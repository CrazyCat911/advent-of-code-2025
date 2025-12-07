### INPUT PROCESSING ###
with open("3/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = [list(bank) for bank in plaintext_input.strip().split("\n")]

### THE CODE ###

def get_joltage(bank: list[str]) -> int:
    first_digit = max(bank[:-1], key=lambda v: int(v))
    first_digit_location = bank.index(first_digit)

    next_digit = max(bank[first_digit_location + 1:])

    return int(first_digit + next_digit)


total_joltage = 0

for bank in formatted_input:
    total_joltage += get_joltage(bank)

print(total_joltage)
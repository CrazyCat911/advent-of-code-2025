### INPUT PROCESSING ###
with open("3/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = [list(bank) for bank in plaintext_input.strip().split("\n")]

### THE CODE ###
def get_joltage(bank: list[str], batteries: int = 2) -> int:
    digits = []
    remainder = bank

    for i in range(batteries):
        digit = max(remainder[:-((batteries - 1) - len(digits))] if -((batteries - 1) - len(digits)) != 0 else remainder, key=int)
        digit_location = remainder.index(digit)
        remainder = remainder[digit_location + 1:]
        digits.append(digit)
        print(digit)

    return int("".join(digits))


total_joltage = 0

for bank in formatted_input:
    total_joltage += get_joltage(bank, 12)

print(total_joltage)
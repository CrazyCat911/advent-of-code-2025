### INPUT PROCESSING ###
with open("1/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = plaintext_input.strip().split("\n")

### THE CODE ###
dial_location = 50
password_count = 0

for instruction in formatted_input:
    distance = int(instruction[1:])

    if instruction.startswith("R"):
        dial_location += distance
    elif instruction.startswith("L"):
        dial_location -= distance
    else:
        raise Exception(f"invalid instruction: {instruction}")

    dial_location %= 100

    if dial_location == 0:
        password_count += 1

print(password_count)
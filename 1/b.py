### INPUT PROCESSING ###
with open("1/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = plaintext_input.strip().split("\n")

### THE CODE ###
dial_location = 50
password_count = 0

for instruction in formatted_input:
    distance = int(instruction[1:])
    direction = None

    if instruction.startswith("R"):
        direction = 1
    elif instruction.startswith("L"):
        direction = -1
    else:
        raise Exception(f"invalid instruction: {instruction}")

    for i in range(distance):
        dial_location += direction
        dial_location %= 100

        if dial_location == 0:
            password_count += 1

print(password_count)
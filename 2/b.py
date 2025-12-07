### INPUT PROCESSING ###
with open("2/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = [[int(v) for v in v.split("-")] for v in plaintext_input.strip().split(",")]

### THE CODE ###
def id_invalid(id):
    number_as_str = str(number)

    return number_as_str in (number_as_str + number_as_str)[1:-1]

total_invalid = 0

for id_range in formatted_input:
    for number in range(id_range[0], id_range[1] + 1):
        if id_invalid(number):
            total_invalid += number

print(total_invalid)
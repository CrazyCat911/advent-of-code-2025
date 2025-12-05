### INPUT PROCESSING ###
with open("2/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = [[int(v) for v in v.split("-")] for v in plaintext_input.strip().split(",")]

### THE CODE ###

total_invalid = 0

for id_range in formatted_input:
    for number in range(id_range[0], id_range[1] + 1):
        number_as_str = str(number)
        number_len = len(number_as_str)
        
        if number_len % 2 != 0:
            continue

        if number_as_str[:(number_len//2)] == number_as_str[(number_len//2):]:
            total_invalid += number

print(total_invalid)
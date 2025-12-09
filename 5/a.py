### INPUT PROCESSING ###
with open("5/input.dat", "r") as f:
    plaintext_input = f.read()

plaintext_ranges, plaintext_ids = plaintext_input.strip().split("\n\n")
ingredient_ranges = [[int(v) for v in rg.split("-")] for rg in plaintext_ranges.split("\n")]
ingredient_ids = [int(v) for v in plaintext_ids.split("\n")]

### THE CODE ###

total = 0

for ingredient_id in ingredient_ids:
    for start, end in ingredient_ranges:
        if start <= ingredient_id <= end:
            total += 1
            break

print(total)
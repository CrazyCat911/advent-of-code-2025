### INPUT PROCESSING ###
with open("5/input.dat", "r") as f:
    plaintext_input = f.read()

plaintext_ranges, plaintext_ids = plaintext_input.strip().split("\n\n")
ingredient_ranges = [[int(v) for v in rg.split("-")] for rg in plaintext_ranges.split("\n")]
ingredient_ids = [int(v) for v in plaintext_ids.split("\n")]

### THE CODE ###

ranges = sorted(ingredient_ranges)
merged = []
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = start, end

merged.append((cur_start, cur_end))

total = sum((end - start + 1) for start, end in merged)
print(total)
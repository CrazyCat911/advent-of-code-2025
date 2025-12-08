### INPUT PROCESSING ###
with open("4/input.dat", "r") as f:
    plaintext_input = f.read()

formatted_input = [list(row) for row in plaintext_input.strip().split("\n")]

### THE CODE ###

def get_adj(grid: list[list[str]], location: tuple[int, int]) -> list[str]:
    x, y = location
    
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]
    
    output = []
    
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        
        if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
            continue
        
        output.append(grid[new_y][new_x])
    
    return output

total = 0

for y, row in enumerate(formatted_input):
    for x, obj in enumerate(row):
        if obj != "@":
            continue
        
        if get_adj(formatted_input, (x, y)).count("@") < 4:
            total += 1

print(total)
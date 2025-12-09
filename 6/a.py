### INPUT PROCESSING ###
with open("6/input.dat", "r") as f:
    plaintext_input = f.read()

operators = [v for v in plaintext_input.strip().split("\n")[-1].split(" ") if v]
numbers = [[int(v) for v in row.split(" ") if v] for row in plaintext_input.strip().split("\n")[:-1]]

### THE CODE ###

grand_total = 0

for q, op in enumerate(operators):
    question_answer = numbers[0][q]
    
    if op == "+":
        for number in numbers[1:]:
            question_answer += number[q]
    elif op == "*":
        for number in numbers[1:]:
            question_answer *= number[q]
    
    grand_total += question_answer

print(grand_total)
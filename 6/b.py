with open("6/input.dat") as f:
    table = [list(line.strip('\n'))[::-1] for line in f]

operators = ''.join(table[-1]).split()
table = [''.join(t).strip() for t in zip(*table[:-1])]
table = [s.split('|') for s in '|'.join(table).split('||')]

grand_total = 0

for i in range(len(table)):
    question_answer = int(table[i][0])
    
    if operators[i] == "+":
        for num in table[i][1:]:
            question_answer += int(num)
    elif operators[i] == "*":
        for num in table[i][1:]:
            question_answer *= int(num)
    
    print(operators[i].join(table[i]))
    grand_total += question_answer

print(grand_total)
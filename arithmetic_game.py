import random
from typing import Dict, List
from time import time

operators = {0: '+', 1: '-', 2: '*', 3: '//'}
levels = {1: 10, 2: 20, 3: 40, 4: 80}


def generate_and_check(level: int, levels: Dict, operators: Dict) -> bool:
    op1 = random.randint(0, levels[level])
    op2 = random.randint(0, levels[level])
    op_num = random.randint(0, 3)
    op = operators[op_num]
    print(op1, op, op2)
    result = int(input("Result:"))
    if op == '+':
        return result == op1 + op2
    elif op == '-':
        return result == op1 - op2
    elif op == '*':
        return result == op1 * op2
    else:
        return result == op1 // op2


def length_game():
    streak = 0
    n = int(input("Input your level:"))
    while generate_and_check(n, levels, operators):
        streak += 1
        print("Great job! You now have a streak of " + str(streak) + " correct answers!")


def speed_game(k: int):
    t = time()
    s = 0
    n = int(input("Input your level:"))
    while generate_and_check(n, levels, operators) and s < k:
        s += 1
        print("Great job! Keep going, only " + str(k - s) + " to go!")
    if s == k:
        tf = time()
        print("Great job! You answered " + str(k) + " questions correctly in " + str(int(tf-t)) + " seconds.")


speed_game(5)

from random import randint
from time import time

operators = {0: '+', 1: '-', 2: '*', 3: '//'}
levels = {1: 10, 2: 20, 3: 40, 4: 80}


def generate_and_check(level: int) -> bool:
    op1 = randint(0, levels[level])
    op2 = randint(0, levels[level])
    op_num = randint(0, 3)
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


# Make list and give final score like a test.
def length_game(k: int):
    streak = 0
    n = int(input("Input your level:"))
    for i in range(k):
        streak += generate_and_check(n)
    print("Great job! You have a streak of " + str(streak) + " correct answers!")


# Useless as we need /commands to answer
def speed_game(k: int):
    t = time()
    s = 0
    n = int(input("Input your level:"))
    while generate_and_check(n) and s < k:
        s += 1
        print("Great job! Keep going, only " + str(k - s) + " to go!")
    if s == k:
        tf = time()
        print("Great job! You answered " + str(k) + " questions correctly in " + str(int(tf - t)) + " seconds.")

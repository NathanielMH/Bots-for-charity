# 10*10 grid, 1 de 2, 2 de 3, 1 de 4, 1 de 5
# Fix difficulty
# Change 1 and 0 in grid by emojis
# Check for boats when you put a new one

D = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
g = [["W" for i in range(10)] for i in range(10)]
grid_id = [["W" for i in range(10)] for i in range(10)]
id_n = 0
lives = [2, 3, 3, 4, 5]


def new_boat(grid, k, orientation, y, x, id_num, grid_id):
    if orientation not in ['H', 'V']:
        print("Error orientation")
    elif x + k > 10 and orientation == "V":
        print("Error size")
    elif y + k > 10 and orientation == "H":
        print("Error size")
    else:
        if orientation == 'HOR':
            for j in range(k):
                if grid[x][y + j] == "B":
                    print("Error occupied")
                grid[x][y + j] = "B"
                grid_id[x][y + j] = id_num

        else:
            for j in range(k):
                if grid[x + j][y] == "B":
                    print("Error occupied")
                grid[x + j][y] = "B"
                grid_id[x + j][y] = id_num


def move(grid, y, x, grid_id, lives):
    if x > 9 or y > 9:
        print("Error wrong position")
    elif grid[x][y] == "B":
        grid[x][y] = "H"
        lives[grid_id[x][y]] -= 1
        if lives[grid_id[x][y]] == 0:
            return "SUNK"
        else:
            return "HIT"
    else:
        return "MISS"


def play(grid, grid_id, lives):
    m = "HIT"
    while m == "HIT" or m == "SUNK":
        x = int(input("x = "))
        y = int(input("y = "))
        m = move(g, x, y, grid_id, lives)
        if lives == [0, 0, 0, 0, 0]:
            print("You win!")
        else:
            print(m)


for i in range(10):
    print(g[i])

for i in range(1):
    o = input("Orientation (H or V): ")
    x = int(input("x = "))
    y = int(input("y = "))
    new_boat(g, 2, o, x, y, id_n, grid_id)
    id_n += 1
for i in range(10):
    print(g[i])

for i in range(2):
    o = input("Orientation (H or V): ")
    x = int(input("x = "))
    y = int(input("y = "))
    new_boat(g, 3, o, x, y, id_n, grid_id)
    id_n += 1
for i in range(10):
    print(g[i])
for i in range(1):
    o = input("Orientation (H or V): ")
    x = int(input("x = "))
    y = int(input("y = "))
    new_boat(g, 4, o, x, y, id_n, grid_id)
    id_n += 1
for i in range(10):
    print(g[i])
for i in range(1):
    o = input("Orientation (H or V): ")
    x = int(input("x = "))
    y = int(input("y = "))
    new_boat(g, 5, o, x, y, id_n, grid_id)
    id_n += 1
for i in range(10):
    print(g[i])

m = "HIT"
while m == "HIT" or m == "SUNK":
    x = int(input("x = "))
    y = int(input("y = "))
    m = move(g, x, y, grid_id, lives)
    print(m)

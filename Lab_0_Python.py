import random

SIZE = 5
SHIPS = [2, 1, 1]

def create_board():
    return [["~"] * SIZE for _ in range(SIZE)]

def place_ship(board, size, symbol, auto=True):
    placed = False
    while not placed:
        if auto:
            d = random.choice(["b", "n"])
            r, c = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        else:
            r = int(input(f"Рядок для {size}-палубного (0-4): "))
            c = int(input(f"Стовпець для {size}-палубного (0-4): "))
            d = "b" if size == 1 else input("Напрямок (b-вбік, n-вниз): ").strip().lower()
        if d == "b" and c+size <= SIZE and all(board[r][c+i] == "~" for i in range(size)):
            for i in range(size): board[r][c+i] = symbol; placed = True
        elif d == "n" and r+size <= SIZE and all(board[r+i][c] == "~" for i in range(size)):
            for i in range(size): board[r+i][c] = symbol; placed = True
        else:
            if not auto: print("Помилка! Спробуйте ще.")

def print_boards(my, comp):
    print("\n   Ваше поле:           Поле комп'ютера:")
    print("   " + " ".join(map(str, range(SIZE))) + "          " + " ".join(map(str, range(SIZE))))
    for i in range(SIZE):
        print(f"{i} | {' '.join(my[i])} |    {i} | {' '.join(x if x!='S' else '~' for x in comp[i])} |")

def shoot(board, r, c, symbol):
    if board[r][c] == symbol: board[r][c] = "X"; return True
    if board[r][c] == "~": board[r][c] = "O"
    return False

# Ініціалізація
comp_board, my_board = create_board(), create_board()
for s in SHIPS: place_ship(comp_board, s, "S", auto=True)

choice = input("Розстановка кораблів: 1-ручна, 2-авто: ")
for s in SHIPS: place_ship(my_board, s, "s", auto=(choice!="1"))

comp_hp = player_hp = sum(SHIPS)
comp_shots = []

while player_hp > 0 and comp_hp > 0:
    print_boards(my_board, comp_board)

    # Хід гравця
    while True:
        try:
            r, c = int(input("Ваш постріл рядок (0-4): ")), int(input("Стовпець (0-4): "))
            if 0 <= r < SIZE and 0 <= c < SIZE and comp_board[r][c] not in ["X","O"]: break
        except: pass
        print("Некоректно, спробуйте ще.")
    if shoot(comp_board, r, c, "S"): print("Влучив!"); comp_hp -= 1
    else: print("Промах!")

    if comp_hp == 0: break

    # Хід комп'ютера
    while True:
        cr, cc = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        if (cr, cc) not in comp_shots: comp_shots.append((cr, cc)); break
    print(f"Комп'ютер стріляє в {cr},{cc}")
    if shoot(my_board, cr, cc, "s"): print("Комп'ютер влучив!"); player_hp -= 1
    else: print("Комп'ютер промахнувся!")

print_boards(my_board, comp_board)
print("Ви перемогли!" if comp_hp == 0 else "Комп'ютер переміг.")
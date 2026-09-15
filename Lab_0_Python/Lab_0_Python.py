import random

comp_board = [["~"] * 5 for _ in range(5)]
my_board = [["~"] * 5 for _ in range(5)]

for size in list((2, 1, 1)):
    placed = False
    while not placed:
        d = random.choice(["b", "n"])
        r, c = random.randint(0, 4), random.randint(0, 4)
        
        if d == "b" and c + size <= 5 and "S" not in comp_board[r][c : c + size]:
            for i in range(size):
                comp_board[r][c + i] = "S"
            placed = True
        elif (
            d == "n"
            and r + size <= 5
            and all(comp_board[r + i][c] != "S" for i in range(size))
        ):
            for i in range(size):
                comp_board[r + i][c] = "S"
            placed = True

print("=== МОРСЬКИЙ БІЙ ===")
print("Оберіть спосіб розстановки ваших кораблів:")
print("1 - Вручну")
print("2 - Автоматично")

choice = ""
while choice not in ["1", "2"]:
    choice = input("Ваш вибір (1 або 2): ").strip()

if choice == "1":
   
    print("\n=== РОЗСТАНОВКА КОРАБЛІВ ГРАВЦЯ ===")
    for size in list((2, 1, 1)):
        placed = False
        while not placed:
            try:
                user_r = int(input(f"\nРядок для {size}-палубного (1-5): "))
                user_c = int(input(f"Стовпець для {size}-палубного (1-5): "))
                
                if not (1 <= user_r <= 5 and 1 <= user_c <= 5):
                    print("Будь ласка, вводьте цифри строго від 1 до 5!")
                    continue
                    
                r = user_r - 1
                c = user_c - 1
                
                d = "b" if size == 1 else input("Напрямок (b - вбік, n - вниз): ").strip().lower()

                if d == "b" and c + size <= 5 and "s" not in my_board[r][c : c + size] and my_board[r][c] == "~":

                    for i in range(size):
                        my_board[r][c + i] = "s"
                    placed = True
                elif (
                    d == "n"
                    and r + size <= 5
                    and all(my_board[r + i][c] != "s" for i in range(size))
                ):
                    for i in range(size):
                        my_board[r + i][c] = "s"
                    placed = True
                else:
                    print("Помилка! Корабель не влазить або перетинається.")
            except ValueError:
                print("Введіть коректне число!")
else:

    for size in list((2, 1, 1)):
        placed = False
        while not placed:
            d = random.choice(["b", "n"])
            r, c = random.randint(0, 4), random.randint(0, 4)
            
            if d == "b" and c + size <= 5 and "s" not in my_board[r][c : c + size]:
                for i in range(size):
                    my_board[r][c + i] = "s"
                placed = True
            elif (
                d == "n"
                and r + size <= 5
                and all(my_board[r + i][c] != "s" for i in range(size))
            ):
                for i in range(size):
                    my_board[r + i][c] = "s"
                placed = True
    print("\nВаші кораблі розставлено автоматично.")

comp_shots = []
player_hp = comp_hp = 4

while player_hp > 0 and comp_hp > 0:
     
    print("\n    Ваше поле:                Поле комп'ютера:")
    print("    1 2 3 4 5                 1 2 3 4 5")
    print("  -----------               -----------")
    for i in range(5):
        my_row = " ".join(my_board[i])
        comp_row = " ".join(comp_board[i]).replace("S", "~")
        print(f"{i+1} | {my_row} |           {i+1} | {comp_row} |")

    while True:
        try:
            user_sr = int(input("\nВаш постріл. Рядок (1-5): "))
            user_sc = int(input("Стовпець (1-5): "))
            
            if not (1 <= user_sr <= 5 and 1 <= user_sc <= 5):
                print("Будь ласка, введіть цифри строго від 1 до 5!")
                continue
                
            sr = user_sr - 1
            sc = user_sc - 1
            
            if comp_board[sr][sc] in ["X", "O"]:
                print("Ви сюди вже стріляли! Спробуйте іншу клітинку.")
                continue
                
            break
        except ValueError:
            print("Ви нічого не ввели або ввели букву! Спробуйте ще раз.")

    if comp_board[sr][sc] == "S":
        print("Влучив!")
        comp_board[sr][sc] = "X"
        comp_hp -= 1
    else:
        print("Промах!")
        comp_board[sr][sc] = "O"

    if comp_hp == 0:
        break

    while True:
        cr, cc = random.randint(0, 4), random.randint(0, 4)
        if (cr, cc) not in comp_shots:
            comp_shots.append((cr, cc))
            break

    print(f"\nКомп'ютер стріляє в рядок {cr + 1}, стовпець {cc + 1}")
    
    if my_board[cr][cc] == "s":
        print("Комп'ютер влучив!")
        my_board[cr][cc] = "X"
        player_hp -= 1
    else:
        print("Комп'ютер промахнувся!")
        my_board[cr][cc] = "O"

print("\n=== ГРУ ЗАВЕРШЕНО ===")
print("    Ваше поле:                Поле комп'ютера:")
print("    1 2 3 4 5                 1 2 3 4 5")
print("  -----------               -----------")
for i in range(5):
    my_row = " ".join(my_board[i])
    comp_row = " ".join(comp_board[i])  
    print(f"{i+1} | {my_row} |           {i+1} | {comp_row} |")

if comp_hp == 0:
    print("\nВи перемогли!")
else:
    print("\nКомп'ютер переміг.")

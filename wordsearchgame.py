import random
import os
import sys
from colorama import init, Fore, Style

# ===== INITIALIZE COLORAMA =====
init(convert=True)

# ================= COLORS =================
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL

LEFT_PADDING = 60
LEFT_SPACING = 30

# ================= CLEAR SCREEN =================
def clear_screen():
    sys.stdout.flush()
    os.system("cls")

# ================= WELCOME =================
def welcome_screen():
    clear_screen()
    print(GREEN + BOLD)
    print("""
                                      ########################################################################
                                      # __      _____ _    ___ ___  __  __ ___   _____ ___    _____ _  _ ___ #
                                      # \\ \\    / / __| |  / __/ _ \\|  \\/  | __| |_   _/ _ \\  |_   _| || | __|#
                                      #  \\ \\/\\/ /| _|| |_| (_| (_) | |\\/| | _|    | || (_) |   | | | __ | _| #
                                      #   \\_/\\_/ |___|____\\___\\___/|_|  |_|___|   |_| \\___/    |_| |_||_|___|#
                                      #                 \\ \\    / / _ \\| _ \\   \\                              #
                                      #                  \\ \\/\\/ / (_) |   / |) |                             #
                                      #      ___ ___   _  \\_/\\_/_\\___/|_|_\\___/   _   __  __ ___             #
                                      #     / __| __| /_\\ | _ \\/ __| || |  / __| /_\\ |  \\/  | __|            #
                                      #     \\__ \\ _| / _ \\|   / (__| __ | | (_ |/ _ \\| |\\/| | _|             #
                                      #     |___/___/_/ \\_\\_|_\\\\___|_| |_|  \\___/_/ \\_\\_|  |_|___|            #
                                      #                                                                      #
                                      ########################################################################
""")
    print(RESET)

# ================= GRID =================
def generate_grid(rows, cols, words):
    grid = [["" for _ in range(cols)] for _ in range(rows)]

    for word in words:
        placed = False
        while not placed:
            r = random.randint(0, rows - 1)
            c = random.randint(0, cols - len(word))
            if all(grid[r][c + i] in ("", word[i]) for i in range(len(word))):
                for i in range(len(word)):
                    grid[r][c + i] = word[i]
                placed = True

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "":
                grid[i][j] = random.choice(letters)

    return grid

def display_grid(grid, found_positions):
    for i in range(len(grid)):
        print(" " * LEFT_SPACING, end="")
        for j in range(len(grid[0])):
            if (i, j) in found_positions:
                print(RED + grid[i][j] + RESET, end="  ")
            else:
                print(grid[i][j], end="  ")
        print()

# ================= SEARCH =================
def search_word(grid, word):
    for r in range(len(grid)):
        row = "".join(grid[r])
        if word in row:
            start = row.index(word)
            return [(r, start + i) for i in range(len(word))]
    return []

# ================= GAME =================
def play_game(rows, cols, words, hint):
    grid = generate_grid(rows, cols, words)
    found_words = []
    found_positions = []

    while len(found_words) < len(words):
        clear_screen()

        print("{:>78}".format(CYAN + "HINT: " + hint + RESET + "\n"))
        display_grid(grid, found_positions)

        user_word = input("\n" + " " * LEFT_SPACING +
                          GREEN + "Enter word: " + RESET).upper()

        if user_word in words and user_word not in found_words:
            pos = search_word(grid, user_word)
            if pos:
                found_words.append(user_word)
                found_positions.extend(pos)

    clear_screen()
    display_grid(grid, found_positions)
    print("\n" + GREEN + BOLD + " " * LEFT_PADDING +
          "🎉 CONGRATULATIONS! YOU FOUND ALL WORDS 🎉" + RESET)

    input("\n" + " " * LEFT_PADDING + "Press Enter to return to menu...")

# ================= MODES =================
def play_once():
    play_game(
        20, 30,
        ["INDIA", "PAKISTAN", "USA", "COMBODIA", "JAPAN", "CANADA", "CHINA"],
        "COUNTRIES (7)"
    )

def play_levels():
    while True:
        clear_screen()
        print(" " * LEFT_PADDING + RED + "1. Level 1 (3 Words)" + RESET)
        print(" " * LEFT_PADDING + GREEN + "2. Level 2 (5 Words)" + RESET)
        print(" " * LEFT_PADDING + CYAN + "3. Level 3 (10 Words)" + RESET)
        print(" " * LEFT_PADDING + Fore.MAGENTA + "4. Back" + RESET + "\n")

        choice = input(" " * LEFT_PADDING + BOLD + "Choose level: " + RESET)

        if choice == '1':
            play_game(10, 15, ["CAT", "DOG", "LION"], "ANIMALS (3)")
        elif choice == '2':
            play_game(15, 15,
                      ["APPLE", "MANGO", "GRAPE", "BANANA", "ORANGE"],
                      "FRUITS (5)")
        elif choice == '3':
            play_game(
                20, 30,
                ["INDIA", "USA", "CANADA", "JAPAN", "CHINA",
                 "PAKISTAN", "RUSSIA", "ITALY", "SPAIN", "NEPAL"],
                "COUNTRIES (10)"
            )
        elif choice == '4':
            break

# ================= MAIN =================
def main():
    while True:
        welcome_screen()
        print(" " * LEFT_PADDING + RED + "1. Play Once" + RESET)
        print(" " * LEFT_PADDING + CYAN + "2. Play With Levels" + RESET)
        print(" " * LEFT_PADDING + Fore.MAGENTA + "3. Exit" + RESET + "\n")

        choice = input(" " * LEFT_PADDING + BOLD + "Enter choice: " + RESET)

        if choice == '1':
            play_once()
        elif choice == '2':
            play_levels()
        elif choice == '3':
            clear_screen()
            print("{:>90}".format(GREEN + "Thank you for playing!" + RESET))
            break

main()

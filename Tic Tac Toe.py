import random

board = [
    "", "", "",
    "", "", "",
    "", "", "",
]

def print_board():
    print(f"Current Board:\n{board[0]} | {board[1]} | {board[2]}\n-----\n{board[3]} | {board[4]} | {board[5]}\n-----\n{board[6]} | {board[7]} | {board[8]}")

print_board()

def player_move():
    while True:
        print("Choose a square (1-9): ")

        try:
            move = int(input())
        except ValueError:
            print("Please enter a number between 1 and 9!")
            continue

        if move < 1 or move > 9:
            print("Please enter a number between 1 and 9!")
            continue

        if board[move - 1] == "":
            board[move - 1] = "X"
            print_board()
            return
        else:
            print("That square is already taken!")
            continue


def computer_move():

    if board[0] == "X" and board[1] == "X" and board[2] == "":
        board[2] = "O"
        print_board()
        return

    if board[0] == "X" and board[2] == "X" and board[1] == "":
        board[1] = "O"
        print_board()
        return

    if board[1] == "X" and board[2] == "X" and board[0] == "":
        board[0] = "O"
        print_board()
        return

    if board[3] == "X" and board[4] == "X" and board[5] == "":
        board[5] = "O"
        print_board()
        return

    if board[3] == "X" and board[5] == "X" and board[4] == "":
        board[4] = "O"
        print_board()
        return

    if board[4] == "X" and board[5] == "X" and board[3] == "":
        board[3] = "O"
        print_board()
        return

    if board[6] == "X" and board[7] == "X" and board[8] == "":
        board[8] = "O"
        print_board()
        return

    if board[6] == "X" and board[8] == "X" and board[7] == "":
        board[7] = "O"
        print_board()
        return

    if board[7] == "X" and board[8] == "X" and board[6] == "":
        board[6] = "O"
        print_board()
        return

    if board[0] == "X" and board[3] == "X" and board[6] == "":
        board[6] = "O"
        print_board()
        return

    if board[0] == "X" and board[6] == "X" and board[3] == "":
        board[3] = "O"
        print_board()
        return

    if board[3] == "X" and board[6] == "X" and board[0] == "":
        board[0] = "O"
        print_board()
        return

    if board[1] == "X" and board[4] == "X" and board[7] == "":
        board[7] = "O"
        print_board()
        return

    if board[1] == "X" and board[7] == "X" and board[4] == "":
        board[4] = "O"
        print_board()
        return

    if board[4] == "X" and board[7] == "X" and board[1] == "":
        board[1] = "O"
        print_board()
        return

    if board[2] == "X" and board[5] == "X" and board[8] == "":
        board[8] = "O"
        print_board()
        return

    if board[2] == "X" and board[8] == "X" and board[5] == "":
        board[5] = "O"
        print_board()
        return

    if board[5] == "X" and board[8] == "X" and board[2] == "":
        board[2] = "O"
        print_board()
        return

    if board[0] == "X" and board[4] == "X" and board[8] == "":
        board[8] = "O"
        print_board()
        return

    if board[0] == "X" and board[8] == "X" and board[4] == "":
        board[4] = "O"
        print_board()
        return

    if board[4] == "X" and board[8] == "X" and board[0] == "":
        board[0] = "O"
        print_board()
        return

    if board[2] == "X" and board[4] == "X" and board[6] == "":
        board[6] = "O"
        print_board()
        return

    if board[2] == "X" and board[6] == "X" and board[4] == "":
        board[4] = "O"
        print_board()
        return

    if board[4] == "X" and board[6] == "X" and board[2] == "":
        board[2] = "O"
        print_board()
        return

    while True:
        computer_move = random.randint(1, 9)

        if board[computer_move - 1] == "":
            board[computer_move - 1] = "O"
            print_board()
            return


def win_check():
    if board[0] == board[1] == board[2] != "":
        return True

    if board[3] == board[4] == board[5] != "":
        return True

    if board[6] == board[7] == board[8] != "":
        return True

    if board[0] == board[3] == board[6] != "":
        return True

    if board[1] == board[4] == board[7] != "":
        return True

    if board[2] == board[5] == board[8] != "":
        return True

    if board[0] == board[4] == board[8] != "":
        return True

    if board[2] == board[4] == board[6] != "":
        return True

    return False


while True:
    player_move()

    if win_check():
        print("You win!")
        break

    if "" not in board:
        print("It's a tie!")
        break

    computer_move()

    if win_check():
        print("Computer wins!")
        break

    if "" not in board:
        print("It's a tie!")
        break
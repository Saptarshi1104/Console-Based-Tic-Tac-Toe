#Project Tic Tac Toe

list_of_values = ["1","2","3","4","5","6","7","8","9"]
value = "X"
print(f"{list_of_values[0]}\t|\t{list_of_values[1]}\t|\t{list_of_values[2]}\n{list_of_values[3]}\t|\t{list_of_values[4]}\t|\t{list_of_values[5]}\n{list_of_values[6]}\t|\t{list_of_values[7]}\t|\t{list_of_values[8]}\n")

for i in range(0,9):
    input_square = input("Enter the square number where you want to enter your mark: ")

    try:
        integer_square = int(input_square)
    except(ValueError):
        print("Invalid Number")
        break

    integer_square = int(input_square)

    if list_of_values[0] == "X" and integer_square - 1 == 0:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[1] == "X" and integer_square - 1 == 1:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[2] == "X" and integer_square - 1 == 2:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[3] == "X" and integer_square - 1 == 3:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[4] == "X" and integer_square - 1 == 4:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[5] == "X" and integer_square - 1 == 5:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[6] == "X" and integer_square - 1 == 6:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[7] == "X" and integer_square - 1 == 7:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[8] == "X" and integer_square - 1 == 8:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[0] == "O" and integer_square - 1 == 0:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[1] == "O" and integer_square - 1 == 1:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[2] == "O" and integer_square - 1 == 2:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[3] == "O" and integer_square - 1 == 3:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[4] == "O" and integer_square - 1 == 4:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[5] == "O" and integer_square - 1 == 5:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[6] == "O" and integer_square - 1 == 6:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[7] == "O" and integer_square - 1 == 7:
        print("You can't use the same square twice, please retry")
        break
    elif list_of_values[8] == "O" and integer_square - 1 == 8:
        print("You can't use the same square twice, please retry")
        break

    try:
        list_of_values[integer_square-1] = value
    except(IndexError):
        print("Invalid Number")
        break

    list_of_values[integer_square-1] = value
    print(f"{list_of_values[0]}\t|\t{list_of_values[1]}\t|\t{list_of_values[2]}\n{list_of_values[3]}\t|\t{list_of_values[4]}\t|\t{list_of_values[5]}\n{list_of_values[6]}\t|\t{list_of_values[7]}\t|\t{list_of_values[8]}\n")
    
    if value == "X": 
        value = "O"
    elif value == "O":
        value = "X"

    if list_of_values[0] == "X" and list_of_values[1] == "X" and list_of_values[2] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[3] == "X" and list_of_values[4] == "X" and list_of_values[5] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[6] == "X" and list_of_values[7] == "X" and list_of_values[8] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[0] == "X" and list_of_values[3] == "X" and list_of_values[6] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[1] == "X" and list_of_values[4] == "X" and list_of_values[7] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[2] == "X" and list_of_values[5] == "X" and list_of_values[8] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[0] == "X" and list_of_values[4] == "X" and list_of_values[8] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[2] == "X" and list_of_values[4] == "X" and list_of_values[6] == "X":
        print("Hurray! X has won the match!")
        break
    elif list_of_values[0] == "O" and list_of_values[1] == "O" and list_of_values[2] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[3] == "O" and list_of_values[4] == "O" and list_of_values[5] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[6] == "O" and list_of_values[7] == "O" and list_of_values[8] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[0] == "O" and list_of_values[3] == "O" and list_of_values[6] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[1] == "O" and list_of_values[4] == "O" and list_of_values[7] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[2] == "O" and list_of_values[5] == "O" and list_of_values[8] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[0] == "O" and list_of_values[4] == "O" and list_of_values[8] == "O":
        print("Hurray! O has won the match!")
        break
    elif list_of_values[2] == "O" and list_of_values[4] == "O" and list_of_values[6] == "O":
        print("Hurray! O has won the match!")
        break
    elif (list_of_values[0] == "X" or list_of_values[0] == "O") and (list_of_values[1] == "X" or list_of_values[1] == "O") and (list_of_values[2] == "X" or list_of_values[2] == "O") and  (list_of_values[3] == "X" or list_of_values[3] == "O") and  (list_of_values[4] == "X" or list_of_values[4] == "O") and  (list_of_values[5] == "X" or list_of_values[5] == "O") and  (list_of_values[6] == "X" or list_of_values[6] == "O") and  (list_of_values[7] == "X" or list_of_values[7] == "O") and (list_of_values[8] == "X" or list_of_values[8] == "O"):
        print("The match has ended in a draw")
        break
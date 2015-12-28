
"""
README
AUTHORS: Katherine Lee and Lizzie Siegle

Our version of Battleship is a game between the user and the computer.
The computer places five different ships (aircraft carrier, battleship,
destroyer, submarine, and patrol boat) randomly on the board and gives the
user a chance to guess. Each time the user hits a ship, the 'O' will turn into
an 'X'. Each time the user hits open water, the 'O' will turn into a 'Y'. The
game is over when the user has found all of the boats. The user must guess
the placement of all of the ships within 150 guesses. 

This, in relation to the Battleship board game, is only half the game. The
computer does not, in turn, guess ships placed by the user.

KNOWN BUGS:
The ships have a tendency to overlap. If ships overlap, the game will not
terminate properly because termination is based on the number of hits on the
board (17 hits).

TROUBLESHOOTING:
The except statements at the bottom of the code are conditions for the user.
They allow the user to continue playing even if they input wrong types for
their guesses OR if they do not input anything.

INSTRUCTIONS:
To start the program, just have to run module.

To play, the user must first input a specific column, beginning with A all the
way through J. Then, the user must input a row number between 1 and 10. The
board will replicate, with an 'X' or a 'Y', depending on whether or not the
user has hit a ship. If the user has hit all of the ships, the computer will
print "Game Over." without a new instance of the board, indicating the the user
has won.

Video of Game Play: https://youtu.be/KO91o-VnE-I
"""

from random import randint
num_unsunk_hits = 17
board = []
#make 10x10 board of 0's
for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "It's time to play Battleship!"
print "Column input must be between A and J"
print "Row input must be between 1 and 10"
print_board(board)


# Aircraft carrier == horizontal, 5 spaces
def random_row_aircraft(board):
    random_row_aircraft = randint(0, 10)
    return random_row_aircraft
def random_col_aircraft(board):
    random_col_aircraft = randint(0, 5)
    return random_col_aircraft
aircraft_row = random_row_aircraft(board)
aircraft_col1 = random_col_aircraft(board)
aircraft_col2 = aircraft_col1 + 1
aircraft_col3 = aircraft_col1 + 2
aircraft_col4 = aircraft_col1 + 3
aircraft_col5 = aircraft_col1 + 4

# Battleship==vertical, 4 spaces
def random_col_battleship(board):
    random_col_battleship = randint(0, 10)
    return random_col_battleship
def random_row_battleship(board):
    random_row_battleship = randint(0, 6)
    return random_row_battleship
battleship_col = random_col_battleship(board)
battleship_row1 = random_row_battleship(board)
if battleship_col == aircraft_col1 and battleship_row1 == aircraft_row:
    battleship_row1 = random_row_battleship(board) #if 1 ship falls on another, try again
battleship_row2 = battleship_row1 + 1
battleship_row3 = battleship_row1 + 2
battleship_row4 = battleship_row1 + 3


# Submarine ==horizontal, 3 spaces
def random_row_sub(board):
    random_row_sub = randint(0, 10)
    return random_row_sub
def random_col_sub(board):
    random_col_sub = randint(0, 7)
    return random_col_sub
submarine_row = random_row_sub(board)
submarine_col1 = random_col_sub(board)
if (submarine_row == battleship_row1 and submarine_col1 == battleship_col) or (submarine_row == battleship_row2 and submarine_col1 == battleship_col) or (submarine_row == battleship_row3 and submarine_col1 == battleship_col):
    submarine_row = random_row_sub(board)
elif (submarine_row == aircraft_row and submarine_col1 == aircraft_col1) or (submarine_row == aircraft_row and submarine_col1 == aircraft_col1) or (submarine_row == aircraft_row and submarine_col1 == aircraft_col1):
    submarine_row = random_row_sub(board)
submarine_col2 = submarine_col1 + 1
submarine_col3 = submarine_col1 + 2

# Destroyer==vertical, 3 spaces
def random_col_destroyer(board):
    random_col_destroyer = randint(0, 10)
    return random_col_destroyer
def random_row_destroyer(board):
    random_row_destroyer = randint(0, 7)
    return random_row_destroyer
destroyer_col = random_col_destroyer(board)
destroyer_row1 = random_row_destroyer(board)
if (destroyer_col == submarine_col1 and destroyer_row1 == submarine_row) or (destroyer_col == submarine_col2 and destroyer_row1 == submarine_row):
    destroyer_col = random_col_destroyer(board)
elif (destroyer_col == battleship_col and destroyer_row1 == battleship_row1) or (destroyer_col == battleship_col and destroyer_row1 == battleship_row2) or (destroyer_col == battleship_col and destroyer_row1 == battleship_row3):
    destroyer_col = random_col_destroyer(board)
elif (destroyer_col == aircraft_col1 and destroyer_row1 == aircraft_row) or (destroyer_col==aircraft_col2 and destroyer_row1==aircraft_row) or (destroyer_col==aircraft_col3 and destroyer_row1==aircraft_row):
    destroyer_col = random_col_destroyer
destroyer_row2 = destroyer_row1 + 1
destroyer_row3 = destroyer_row1 + 2

# Patrol Boat==horizontal, 2 spaces
def random_row_patrolboat(board):
    random_row_patrolboat = randint(0, 10)
    return random_row_patrolboat
def random_col_patrolboat(board):
    random_col_patrolboat = randint(0, 8)
    return random_col_patrolboat
patrol_row = random_row_patrolboat(board)
patrol_col1 = random_col_patrolboat(board)
if (patrol_row == destroyer_row1 and patrol_col1 == destroyer_col) or (patrol_row==destroyer_row2 and patrol_col2==destroyer_col):
    patrol_row = random_row_patrolboat(board)
elif (patrol_row==submarine_row and patrol_col1==submarine_col1) or (patrol_row==submarine_row and patrol_col1==submarine_col2) or (patrol_row==submarine_row and patrol_col1 == submarine_col3):
    patrol_row = random_row_patrolboat(board)
elif (patrol_row ==battleship_row1 and patrol_col1==battleship_col) or (patrol_row==battleship_row2 and patrol_col1==battleship_col) or (patrol_row==battleship_row3 and patrol_col1==battleship_col):
    patrol_row=random_row_patrolboat(board)
elif (patrol_row==aircraft_row and patrol_col1==aircraft_col1) or (patrol_row==aircraft_row and patrol_col1==aircraft_col2) or (patrol_row==aircraft_row and patrol_col1==aircraft_col3) or (patrol_row==aircraft_row and patrol_col1==aircraft_col4) or (patrol_row==aircraft_row and patrol_col1==aircraft_col5):
    patrol_row = random_row_patrolboat(board)
patrol_col2 = patrol_col1 + 1

# Everything from here on should go in your for loop!
for turn in range(150):
    print "turn: "+ str(turn)

    try:
        guess_col = str(raw_input("Guess col:")).lower()

        guess_row = int(raw_input("Guess row:"))

        if num_unsunk_hits == 1:
            print "Game Over."
            break
        else:

 #       num_unsunk_hits = 17 #4 ships, 17 hits(2, 3, 3, 4, 5)
            while num_unsunk_hits > 1:
            
           #convert to int since index of board must be int.
                if guess_col == 'a':
                    guess_col = 1
                elif guess_col == 'b':
                    guess_col = 2
                elif guess_col == 'c':
                    guess_col = 3
                elif guess_col == 'd':
                    guess_col = 4
                elif guess_col == 'e':
                    guess_col = 5
                elif guess_col == 'f':
                    guess_col = 6
                elif guess_col == 'g':
                    guess_col = 7
                elif guess_col == 'h':
                    guess_col = 8
                elif guess_col == 'i':
                    guess_col = 9
                elif guess_col == 'j':
                    guess_col = 10
                #this is in case player guesses one out of range
                elif guess_col == 'k':
                    guess_col = 11
                elif guess_col == 'l':
                    guess_col = 12
                elif guess_col == 'm':
                    guess_col = 13
                elif guess_col == 'n':
                    guess_col = 14
                elif guess_col == 'o':
                    guess_col = 15
                elif guess_col == 'p':
                    guess_col = 16
                elif guess_col == 'q':
                    guess_col = 17
                elif guess_col == 'r':
                    guess_col = 18
                elif guess_col == 's':
                    guess_col = 19
                elif guess_col == 't':
                    guess_col = 20
                elif guess_col == 'u':
                    guess_col = 21
                elif guess_col == 'v':
                    guess_col = 22
                elif guess_col == 'w':
                    guess_col = 23
                elif guess_col == 'x':
                    guess_col = 24
                elif guess_col == 'y':
                    guess_col = 25
                elif guess_col == 'z':
                    guess_col = 26
                elif (board[guess_row-1][guess_col-1] =="X"):
                    print "You already guessed that coordinate!" 
                    break
                elif (guess_row -1 == patrol_row -1 and guess_col-1==patrol_col1-1) or (guess_row-1==patrol_row-1 and guess_col-1==patrol_col2-1) or (guess_row-1==destroyer_row1-1 and guess_col-1==destroyer_col-1) or (guess_row-1==destroyer_row2-1 and guess_col-1==destroyer_col-1) or (guess_row-1==destroyer_row3-1 and guess_col-1==destroyer_col-1) or (guess_col-1==submarine_col1-1 and guess_row-1==submarine_row-1) or (guess_col-1==submarine_col2-1 and guess_row-1==submarine_row-1) or (guess_col-1==submarine_col3-1 and guess_row-1==submarine_row-1) or (battleship_col-1==guess_col-1 and battleship_row1-1==guess_row-1) or (battleship_col-1==guess_col-1 and battleship_row2-1==guess_row-1) or (battleship_col-1==guess_col-1 and battleship_row3-1==guess_row-1) or (battleship_col-1==guess_col-1 and battleship_row4-1==guess_row-1) or (aircraft_row-1==guess_row-1 and aircraft_col1-1==guess_col-1) or (aircraft_row-1==guess_row-1 and aircraft_col2-1==guess_col-1) or (aircraft_row-1==guess_row-1 and aircraft_col3-1==guess_col-1) or (aircraft_row-1==guess_row-1 and aircraft_col4-1==guess_col-1) or (aircraft_row-1==guess_row-1 and aircraft_col5-1==guess_col-1):
                    num_unsunk_hits -=1
                    print "Congratulations! You hit one of my ships! You need to have %d more hits" %num_unsunk_hits
                    board[guess_row-1][guess_col-1] = "X"
                    break
                elif(board[guess_row-1][guess_col-1] == "Y"):
                    print "You already guessed that coordinate!" 
                    break
                else:
                    print "You missed my battleship!"
                    board[guess_row-1][guess_col-1] = "Y"
                    break

            print turn + 1
            print_board(board)
    
    except ValueError:
        print "Invalid entry. Please try again. The row must be an integer from 1 to 10, and the column must be a letter from A to J."
    except TypeError:
        print "Invalid entry. Please try again. The row must be an integer from 1 to 10, and the column must be a letter from A to J."
    except IndexError:
        print "Invalid entry. Please try again. The row must be an integer from 1 to 10, and the column must be a letter from A to J."
        

"""
Koc University, Turkey
KOLT Python Certificate Program
Spring 2020 - Assignment 1

"""

import turtle

my_turtle = turtle.Turtle()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
PEN_SIZE = 5
SQUARE_SIZE = 100
ANIMATION_SPEED = 100   # Animation speed

def draw_empty_board():
    """
    This function should draw the empty tic-tac-toe board using turtle module
    """

    def draw_square(x, y, length):
        
        my_turtle.penup()
        my_turtle.color("Black")
        my_turtle.setpos(x,y)
        my_turtle.pendown()

        for i in range(4):
            my_turtle.left(90)
            my_turtle.forward(length)
    
    x = 200
    y = 200
    length = SQUARE_SIZE

    for j in range(3):
        y -= 100
        x -= 300
        for i in range(3):
            draw_square(x, y, length)
            x += length
    


def draw_x_in_square(row, column):
    """
    This function should draw and X symbol on the given square of tic-tac-toe board
    """
    my_turtle.penup()
    my_turtle.setposition((column-1)*100,(1-row)*100)
    my_turtle.pendown()
    my_turtle.setposition((column-2)*100,(2-row)*100)
    my_turtle.penup()
    my_turtle.setposition((column-2)*100,(1-row)*100)
    my_turtle.pendown()
    my_turtle.setposition((column-1)*100,(2-row)*100)
    


def draw_o_in_square(row, column):
    """
    This function should draw and O symbol on the given square of tic-tac-toe board
    """
    my_turtle.penup()
    my_turtle.setposition(-150 + column * 100, (1 - row) * 100)
    my_turtle.pendown()
    my_turtle.circle(50)

if __name__ == '__main__':
    # Display setup
    display_setup()
    draw_empty_board()

    player_names = []
    
    while True:
        player1 = input("Player 1, please enter your name: ")
        if len(player1) != 0:
            player_names.append(player1)
            break
        else:
            continue    
 
    while True:
        player2 = input("Player 2, please enter your name: ")
        if len(player2) != 0:
            player_names.append(player2)
            break
        else:
            continue
        

    # TODO: Take player names, any string other than empty string is considered a valid name

    # Game setup
    game = [['', '', ''], ['', '', ''], ['', '', '']]

    # Loop for the game
    for move_counter in range(9):
        # TODO: Get current user to play

        current_player_name = player_names[move_counter]
        player_names.extend(player_names)

        # TODO: take user's move
        
        while True:
            move = input(current_player_name + ', which row and column? (0-based, seperated with a space i.e "0 1"): ')
            try:
                move_lst = move.split(' ')
                if len(move_lst) == 2:
                    move_row = int(move_lst[0])
                    move_column = int(move_lst[1])
                    if move_row in range(0, 3) and move_column in range(0, 3) and game[move_row][move_column] == '':      
                        break   

            except ValueError:
                continue

        # TODO: validate the user's move, you need to ask again until user enters a valid move

        if move_counter % 2 == 0:
            game[move_row][move_column] = 'X'
            draw_x_in_square(move_row, move_column)
        else:
            game[move_row][move_column] = 'O'
            draw_o_in_square(move_row, move_column)

        # TODO: play the move: you should modify the game list & display the move using turtle

        there_is_winner = False

        #for horizontal win
        for i in range(len(game)):
            for j in range(len(game[i])):
                if game[i][0] == game[i][1] == game[i][2] and game[i][j] != '':
                    there_is_winner = True
                    break


        #for vertical win
        for i in range(len(game)):
            for j in range(len(game[i])):
                if game[0][j] == game[1][j] == game[2][j] and game[i][j] != '':
                    there_is_winner = True
                    break
                    
        
        #for diagonal win
        for i in range(len(game)):
            for j in range(len(game[i])):
                if game[0][0] == game[1][1] == game[2][2] != '':
                    there_is_winner = True
                    break
                elif game[0][2] == game[1][1] == game[2][0] != '':
                    there_is_winner = True
                    break
        
        # TODO: check win conditions

        # If there is a winner, terminate loop
        # and display winner
        if there_is_winner:
            print(current_player_name + " wins!")
            break

    # If there_is_winner variable is still false, game ended in a draw
    if not there_is_winner:
        print('Game ended in a draw')

    turtle.done()

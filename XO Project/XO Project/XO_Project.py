import time

board = { 1 : ' ', 2 : ' ', 3: ' ',
         4 : ' ', 5 : ' ', 6 : ' ', 
         7 : ' ', 8 : ' ', 9 : ' '}

count = 0		    
winner = False		
play = True		    
tie = False		    
curr_player = ''	
player_details = []	
name = ['p1', 'p2']
import random
turn = random.choice(name)

def get_player_details(curr_player):
   
        if turn == 'p1':
            if curr_player == 'p1':
                return ['p2','O']
            else:
                 return ['p1','X']
        else:
            if curr_player == 'p1':
                return ['p2','X']
            else:
                return ['p1','O']
   
def print_board():
    for i in board:
        print( i, ':', board[i], ' ', end='')
        if i%3 == 0:
            print()

def win_game(marker, player_id):
    if board[1] == marker and board[2] == marker and board[3] == marker or \
    board[4] == marker and board[5] == marker and board[6] == marker or \
    board[7] == marker and board[8] == marker and board[9] == marker or \
    board[1] == marker and board[4] == marker and board[7] == marker or \
    board[2] == marker and board[5] == marker and board[8] == marker or \
    board[3] == marker and board[6] == marker and board[9] == marker or \
    board[1] == marker and board[5] == marker and board[9] == marker or \
    board[3] == marker and board[5] == marker and board[7] == marker:

        print_board()
        time.sleep(1)
        print("good player", player_id, "wins!")
        return True

    else:
        return False

def insert_input(slot_num, marker):
    while board[slot_num] != ' ':
        print("choose another cell")
        slot_num = int(input())
    board[slot_num] = marker

def play_again():
    print("Do you want to play again? press y")
    play_again = input()

    if play_again.upper() == 'Y':
        for z in board:
            board[z] = ' '
        return True
    else:
        print("wish you best luck")
        return False
    
while play:

    print_board()

    player_details = get_player_details(curr_player)
    curr_player = player_details[0]
    print("Player {}: Enter a number between 1 and 9".format(curr_player))
    input_slot = int(input())

    insert_input(input_slot, player_details[1])
    count += 1
    
    winner = win_game(player_details[1], curr_player)
    if count == 9 and not winner:
        print("tie")
        tie = True
        print_board()

    if winner or tie:
        play = play_again()
        if play:
            curr_player = ''
            count = 0

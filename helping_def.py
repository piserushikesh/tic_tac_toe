from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[7]+'  |  '+board[8]+'  |  '+board[9])
    print(board[4]+'  |  '+board[5]+'  |  '+board[6])
    print(board[1]+'  |  '+board[2]+'  |  '+board[3])




def player_input():   
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = ''
     
    while not (marker =='X' or marker == 'O') :
        marker = input('Player 1, choose X or O: ').upper()
                
    if marker == 'X':        
        return ('X','O')        
    else:
        return ('O','X')
        


def place_marker(board, marker, position):
    
    board[position] = marker


def win_check(board, mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or  #row1
            (board[4]==mark and board[5]==mark and board[6]==mark) or  #row2
            (board[1]==mark and board[2]==mark and board[3]==mark) or  #row3
            (board[7]==mark and board[4]==mark and board[1]==mark) or  #col1
            (board[8]==mark and board[5]==mark and board[2]==mark) or  #col2
            (board[9]==mark and board[6]==mark and board[3]==mark) or  #col3
            (board[7]==mark and board[5]==mark and board[3]==mark) or  #digonal1
            (board[9]==mark and board[5]==mark and board[1]==mark))    #digonal2
           



def choose_first():
    
    flip = random.randint(0,1)    
    if flip ==0 :
        return 'Player 1'
    else:
        return 'Player 2'
    

def space_check(board, position):
    
    return board[position] == ' '



def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False        
    return True


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position : (1-9) '))    
    return position


def replay():
    
    choice = input("Play again? Enter Yes or No ")   
    return choice == ('Yes').upper()


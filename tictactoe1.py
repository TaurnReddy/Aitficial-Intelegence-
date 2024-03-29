players = ['O','X']
empty = '_'
init_board = [empty]*9
MAX_LIMIT = 1
MIN_LIMIT = -1

def show_board(board):
    for i in range(len(board)):
        print(board[i],end=" ")
        if i % 3 == 2:
            print()

def get_row(board, index):
    r = index // 3
    return board[3*r:3*r+3]
def get_col(board, index):
    c = index % 3
    return board[c::3]
def get_p_diag(board):
    return [board[0],board[4],board[8]]
def get_n_diag(board):
    return [board[2],board[4],board[6]]
def get_lines(board):
    rows = [get_row(board,0),get_row(board,3),get_row(board,6)]
    cols = [get_col(board,0),get_col(board,1),get_col(board,2)]
    diagonals = [get_p_diag(board),get_n_diag(board)]
    return rows + cols + diagonals

def is_winner(board,player):
    return [player]*3 in get_lines(board)

def is_game_over(board):
    return is_winner(board,players[0]) or is_winner(board,players[1]) or empty not in board

def evaluate(board, player):
    if is_winner(board,players[player]):
        return MAX_LIMIT    # player wins
    if is_winner(board,players[(player+1)%2]):
        return MIN_LIMIT    # the other player wins.
    return 0    # no one wins? then 0

def get_possible_moves(board):
    possible_moves = []
    for i in range(len(board)):
        if board[i] == empty:
            possible_moves.append(i)
    return possible_moves

##show_board(range(9))
##print(get_row(list(range(9)),3))
##print(get_col(list(range(9)),2))
##print(get_p_diag(list(range(9))))
##print(get_n_diag(list(range(9))))
#print(is_winner(init_board,p1))

def two_player_run():
    board = init_board  
    show_board(board)
    move_cnt = 0
    while not is_game_over(board):
        possible_moves = get_possible_moves(board)
        move = eval(input("{}'s turn: Enter your move (0-8): ".format(players[move_cnt%2])))
        while (move not in possible_moves):
            move = eval(input("{}'s turn: Enter your move (0-8): ".format(players[move_cnt%2])))
        board[move] = players[move_cnt%2]
        show_board(board)
        move_cnt += 1
        
    if is_winner(board,players[0]):
        print(players[0], "won the game")
    elif is_winner(board,players[1]):
        print(players[1], "won the game")
    else:
        print("Draw")


import random
def random_move(board):
    return random.choice(get_possible_moves(board))

def min_max_decision(board,player):
    possible_moves = get_possible_moves(board)
    if not possible_moves:
        return None
    
    move = possible_moves[0]
    maxV = MIN_LIMIT
    for action in possible_moves:
        board[action] = players[player]
        res = min_value(board,player)
        #print("min_max_decision",player,show_board(board),action,res)
        if maxV < res:
            maxV = res
            move = action
        board[action] = empty
    return move

def min_value(board,player):
    if is_game_over(board):
        return evaluate(board,player)

    possible_moves = get_possible_moves(board)
    minV = MAX_LIMIT
    for action in possible_moves:
        board[action] = players[(player+1)%2]
        res = max_value(board,player)
        #print("min_value",show_board(board),action,res)
        if minV > res:
            minV = res
        board[action] = empty   
    return minV
        
def max_value(board,player):
    if is_game_over(board):
        return evaluate(board,player)

    possible_moves = get_possible_moves(board)
    maxV = MIN_LIMIT
    for action in possible_moves:
        board[action] = players[player]
        res = min_value(board,player)
        #print("max_vale",show_board(board),action,res)
        if maxV < res:
            maxV = res
        board[action] = empty
    return maxV


def alpha_beta_min_max_decision(board,player):
    if is_game_over(board):
        return None
    
    val, act = alpha_beta_max_value(board,player,MIN_LIMIT,MAX_LIMIT)
    return act

def alpha_beta_max_value(board,player,alpha,beta):
    if is_game_over(board):
        return evaluate(board,player), None

    #print("alpha_beta_max_vale",show_board(board),player,alpha,beta)
    possible_moves = get_possible_moves(board)
    maxV = MIN_LIMIT
    maxAct = None
    for action in possible_moves:
        board[action] = players[player]
        val = alpha_beta_min_value(board,player,alpha,beta)
        if maxV < val:
            maxV = val
            maxAct = action
        if maxV >= beta:
            board[action] = empty
            return maxV, maxAct
        alpha = max(alpha,maxV)
        board[action] = empty
    return maxV, maxAct

def alpha_beta_min_value(board,player,alpha,beta):
    if is_game_over(board):
        return evaluate(board,player)

    #print("alpha_beta_min_value",show_board(board),player,alpha,beta)
    possible_moves = get_possible_moves(board)
    minV = MAX_LIMIT
    for action in possible_moves:
        board[action] = players[(player+1)%2]
        val, act = alpha_beta_max_value(board,player,alpha,beta)
        if minV > val:
            minV = val
        if minV <= alpha:
            board[action] = empty
            return minV
        beta = min(beta,minV)
        board[action] = empty   
    return minV
        

def single_player_run():
    board = init_board
    #board = ['X','O','O','_','O','_','X','X','_']
    #board = ['X','O','_','_','O','_','_','X','_']
    show_board(board)
    move_cnt = 0
    while not is_game_over(board):
        possible_moves = get_possible_moves(board)
        move = eval(input("{}'s turn: Enter your move (0-8): ".format(players[move_cnt%2])))
        while (move not in possible_moves):
            move = eval(input("{}'s turn: Enter your move (0-8): ".format(players[move_cnt%2])))
        board[move] = players[move_cnt%2]
        show_board(board)
        move_cnt += 1

##        computer_move = random_move(board)
        computer_move = min_max_decision(board, move_cnt%2)
##        computer_move = alpha_beta_min_max_decision(board, move_cnt%2)
        if computer_move is None:
            break
        board[computer_move] = players[move_cnt%2]
        print("Computer made a move:",computer_move)
        show_board(board)
        move_cnt += 1
        
    if is_winner(board,players[0]):
        print(players[0], "won the game")
    elif is_winner(board,players[1]):
        print(players[1], "won the game")
    else:
        print("Draw")

#print(is_game_over(['X','O','X','X','O','_','_','O','_']))
single_player_run()

    

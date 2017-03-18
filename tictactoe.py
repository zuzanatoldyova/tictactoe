import random

""" Author Zuzana Toldyova

    Strategy part: """

def possible_moves(state):
    i=0
    active_squares = []
    while i< len(state):
        if ((i+2 < len(state)) and state[i+2] == "O"):
            i += 5
            continue
        if ((i+1 < len(state)) and state[i+1] == "O"):
            i += 4
            continue
        if (state[i] == "O"):
            i += 3
            continue
        active_squares.append(i)
        i +=1
    return active_squares

def easy_win(state):
    indices = [i for i,j in enumerate(state) if j == 'O']
    for i in range(len(indices)):
        if indices[i] - indices[i-1] == 1 and indices[i]+1 < len(state):
            return indices[i] + 1
        elif indices[i] - indices[i-1] == 1 and indices[i]+1 >= len(state):
            return indices[i-1] - 1
        elif indices[i] - indices[i-1] == 2:
            return indices[i] - 1
    return -1

""" Simulates move from strategy and calls recursively strategy so that it can find optimal move, where the opponent can't win. If the move is optimal returns True, if not returns False."""

def simulation(state, move):
    fake_state = state[:]
    a = 0
    while not is_won(fake_state):
        fake_state[move] = "O"
        a += 1
        move = strategy(fake_state)
    if a % 2 != 0:
            return True
    else: return False

""" First checks if it's possible to win in one move if yes returns this move. If not then counts possible moves, which are not "O" and also at least three squares from "O" so that the opponent
    couldn't win in the next move. If there's more than 20 possible moves chooses randomly one. Else simulates recusively every possible move and reaction from the opponent, and returns optimal
    one, where the oponent can't win, if this move exists. If there is no optimal move chooses randomly from the possible moves. If there are no possible moves (opponent can win in the next move) chooses first valid move."""

def strategy(state):
    if easy_win(state) != -1:
        return easy_win(state)
    moves = []
    moves = possible_moves(state)
    if (len(moves) > 20):
        return random.choice(moves)
    else:
        for i in range(len(moves)):
            move = moves[i]
            if simulation(state, move):
                return move
    if len(moves) != 0:
        return random.choice(moves)
    return get_any_move(state)

""" Returns any valid move."""

def get_any_move(state):
    for i in range(len(state)):
        if state[i] == "_":
            return i

""" Game part: """

def show_state(state):
    for i in range(len(state)):
        print state[i],
    print
    for i in range(len(state)):
        print i%10,
    print
    for i in range(len(state)):
        if i%10 == 5:
            print i/10,
        elif i%10 == 0 and i != 0:
            print "|",
        else: print " ",
    print

def moving(state, human_starts):
    if human_starts:
        print "Player's turn"
        move = int(input("Insert your move (0 - 29): "))
    else:
        print "Computer's turn"
        move = strategy(state)
    return move

def valid_move(move, state):
    print move
    if move >= len(state) or move < 0:
        return False
    if state[move] == "_":
        return True
    else:
        return False

def is_won(state):
    a = 0
    for i in state:
        if i == "O":
            a += 1
            if a == 3:
                return True
        else: a = 0
    return False

def tictactoe(size, human_starts=True):
    state = []
    for i in range(size):
        state.append("_")
    while not is_won(state):
        move = moving(state, human_starts)
        while not valid_move(move, state):
            print "Not a valid move!"
            move = moving(state, human_starts)
        state[move] = "O"
        show_state(state)
        human_starts = not human_starts
    if human_starts:
        print "You lost..."
    else:
        print "You won!"

tictactoe(30)

state1 = [0,2,4,6,1,3,5,7] # not good
state2 = [0,2,4] # not good
state3a = [4,5,2,0,6,7,1,3] # not good
state3 = [6,4,2,0,5,7,1,3] # good
state4 = [7,1,4,2,0,6,3,5] # good
N = 8
    
# returns True if the state is free from conflicts
# return False if there is any conflicts
def is_goal(state):
    if len(state) < N:
        return False
    if len(set(state)) < N: # check duplicates in row
        return False
    if len(set([c+state[c] for c in range(N)])) < N: # duplicates in + diagonals
        return False
    if len(set([c-state[c] for c in range(N)])) < N: # duplicates in - diagonals
        return False
    return True

def get_possible_rows(state):
    # get_possible_rows([0]) --> {2,3,4,5,6,7}    
    # get_possible_rows([1]) --> {3,4,5,6,7}
    # get_possible_rows([2]) --> {0,4,5,6,7}
    # get_possible_rows([0,2,4]) --> {1,6,7}
    cols = len(state)
    all_rows = set(range(N))
    row_nums = set(state)
    p_diagonals = set(state[i]+i-cols for i in range(cols))
    n_diagonals = set(state[i]-i+cols for i in range(cols))
    return all_rows - row_nums - p_diagonals - n_diagonals

def solve(state):
#   if the state is a goal state, then return True
#   if a queen is attacked by another one, then return False
#   For each possible row for the the current column,
#   try to solve with that row appended. If succeed, all done.
#   If it fails with all possible rows, then return False
    return False

state = [0,4,7] # this will be solved
#state = [0,4,7,1] # this will not
if solve(state):
    print("Successfully solved")
    print(state)
else:
    print("Failed to solve")
    
##print(is_goal(state1))
##print(is_goal(state2))
##print(is_goal(state3a))
##print(is_goal(state3))
##print(is_goal(state4))
##
##print(get_possible_rows([0]))
##print(get_possible_rows([1]))
##print(get_possible_rows([2]))
##print(get_possible_rows([0,2,4]))

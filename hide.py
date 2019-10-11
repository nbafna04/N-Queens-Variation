import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0]))
            if board[r][c] == '.' and check_left(board, r, c) is True and check_above(board, r,c) is True
            and check_below(board, r , c) is True and check_right(board, r, c) is True]

# Traverse above, check legal moves and check if F can be placed
def check_above(board, row, clm):
    if row != 0:
        for j in range (row-1,-1,-1):
            if (board[j][clm] == '&'):
                return True
            elif (board[j][clm] == 'F') :
                return False
            else:
                continue
        return True
    else:
        return True

# Traverse below, check legal moves and check if F can be placed
def check_below(board, row,clm):
    if row != len(board)-1:
        for j in range(row+1,len(board)):
            if (board[j][clm] == '&'):
                return True
            elif (board[j][clm] == 'F'):
                return False
            else:
                continue
        return True
    else:
        return True

# Traverse left, check legal moves and check if F can be placed
def check_left(board,row,clm):
    if clm != 0:
        for j in range (clm-1,-1,-1):
            if (board[row][j] == '&'):
                return True
            elif (board[row][j] == 'F') :
                return False
            else:
                continue
        return True
    else:
        return True

# Traverse right, check legal moves and check if F can be placed
def check_right(board,row,clm):
    if clm != len(board[0])-1:

        for j in range (clm+1,len(board[0])):
            if (board[row][j] == '&'):
                return True
            elif (board[row][j] == 'F') :
                return False
            else:
                continue
        return True
    else:
        return True

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    visited = []
    while len(fringe) > 0:
        for s in successors(fringe.pop()):
            if s not in visited:
                if is_goal(s):
                    return(s)
                fringe.append(s)
                visited.append(s)
    return False

# Main Function
if __name__ == "__main__":
    IUB_map = parse_map(sys.argv[1])
    #print (IUB_map)

    # This is K, the number of friends
    K = int(sys.argv[2])

    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)

    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")
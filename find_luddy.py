#!/usr/local/bin/python3
import sys
import json

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().split("\n")]ifline

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0]))
                 and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
def search1(IUB_map):
        # Find my start position
        you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0]))
                 for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i] == "#"][0]

        fringe=[(you_loc,0)]

        parent = {}
        parent[you_loc] = None
        visited = []
        while fringe:
                (curr_move, curr_dist)=fringe.pop(0)
                for move in moves(IUB_map, *curr_move):

                        if move not in visited:
                            if IUB_map[move[0]][move[1]]=="@":
                                    if move not in parent:
                                            parent[move] = curr_move
                                    mypath = print_path(parent, move, you_loc)
                                    strpath = str("".join(mypath))
                                    return str(curr_dist+1)  +" "+ (strpath)
                            else:
                                    visited.append(move)
                                    fringe.append((move, curr_dist + 1))
                                    if move not in parent:
                                            parent[move] = curr_move

def print_path(parent, goal, start):
    path = [goal]
    direction = []
    # trace the path back till we reach start
    while goal != start and goal != None:
        goal = parent[goal]
        if goal != None:
                path.insert(0, goal)
    i = 0
    j = 1
    while i < j and j <= len(path)-1:
            if path[j][1] == path[i][1] +1:
                    i += 1
                    j += 1
                    direction.append("E")
            elif path[j][1] == path[i][1] -1:
                    i += 1
                    j += 1
                    direction.append("W")
            elif path[j][0] == path[i][0] +1:
                    i += 1
                    j += 1
                    direction.append("S")
            elif path[j][0] == path[i][0] -1:
                    i += 1
                    j += 1
                    direction.append("N")
    return direction

# Main Function
if __name__ == "__main__":
        IUB_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search1(IUB_map)
        print("Here's the solution I found:")
        print(solution if solution else None)

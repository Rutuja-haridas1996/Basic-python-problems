"""Problem Statement: Pandemic Linearity is a simple board game in which a
single player must identify the source of a viral outbreak. It is played on
board that consists of n cities lined up in a row.

The cities are numbered in order from 0 through n-1 .
The rules of the game are as follows:
In the beginning, the caseload for each city is set to 0. A single city is chosen to
be the epicenter, and begins with a caseload of 1. The epicenter is a secret
from the player.
The game proceeds in time steps. Each time step has two parts:
1. First, the player selects a single city to inspect. Inspecting a city means that
the player learns the caseload for that city.
2. The disease spreads. Each city that either has a positive caseload or is
directly next to a city with a positive caseload increases its caseload by 1. All
other cities continue to have 0 caseload.
Note that the player learns the caseload of a city before the disease spreads.
Your task is to implement the game Pandemic Linearity in Python 3. You may
only use the Python Standard Library (For example, Do NOT use numpy).

Author: Rutuja Haridas
"""

class Board(object):
    
    def __init__(self, cities_num, index_epicenter):
        self.size = cities_num
        self.board = [0] * cities_num
        self.board[index_epicenter] = 1
        

    def move(self, inspect_index):
        """Return the value of index at epicenter Check all the values in list
        where there is +ve number and add 1 to it.

        Also add 1 to the adjacent index values where there is +ve
        integer
        """
        epicenter_index_value = self.board[inspect_index]
        adjacent_index = []
        for index in range(len(self.board)): 
            if self.board[index] > 0:
                if index != len(self.board) - 1:
                    adjacent_index.append(index + 1)
                if index != 0:
                    adjacent_index.append(index - 1)


        positive_index = [index for index in range(len(self.board)) if self.board[index] > 0]
        for index in list(set(adjacent_index + positive_index)):
            self.board[index] = self.board[index] + 1

        print("Board : {}  ".format(self.board))
        print("Element at Epicenter of the city {} : {}".format(inspect_index,epicenter_index_value))
        return epicenter_index_value
        

class Solver(object):
    """Find the epiccenter of board."""
    def __init__(self, board):
        self.board_size = len(board.board)

    def solve(self):   
        for i in range(self.board_size):
            epic_move = board.move(i)
            if epic_move == i + 1:
                print("Epicenter is at {}".format(i))
                break

board = Board(10000, 1588)
solver = Solver(board)
print(solver.solve())


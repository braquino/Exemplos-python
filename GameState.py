from copy import deepcopy

class Board:

    def __init__(self, width=3, height=2):
        self.width = width
        self.height = height
        self.board = self.create_board()
        self.active = {'X': None, 'O': None}
        self.active_player = 'X'

    def __str__(self):
        result = ''
        for y in range(self.height):
            for x in range(self.width):
                result += str(self.board[(x, y)])
                if self.board[(x, y)] == '':
                    result += '_'
            result += '\n'
        return result

    def play(self, move):
        self.board[move] = self.active_player
        self.active[self.active_player] = move
        # Change the active player
        self.active_player = [p for p in ('X', 'O') if p != self.active_player][0]

    def __copy__(self):
        new_board = Board()
        new_board.board = self.board.copy()
        new_board.active = self.active.copy()
        new_board.active_player = self.active_player
        return new_board

    def create_board(self):
        board = {}
        for x in range(self.width):
            for y in range(self.height):
                board[(x, y)] = ''
        board[(2, 1)] = 'B'
        return board


class GameState:

    def __init__(self, board=Board()):
        self.board = board

    def forecast_move(self, move):
        new_board = deepcopy(self.board)
        new_board.play(move)
        return GameState(new_board)

    def get_legal_moves(self):
        player = self.board.active_player
        location = self.board.active[player]
        board = self.board.board
        legal_moves = []
        if location is None:
            return [box for box in board if board[box] == '']
        for c in ((1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (-1, 1), (1, -1)):
            for r in range(1, self.board.width):
                x = location[0] + r * c[0]
                y = location[1] + r * c[1]
                if (x,y) in board.keys():
                    if board[(x,y)] == '':
                        legal_moves += [(x, y)]
                    else:
                        break
                else:
                    break
        return legal_moves


def terminal_test(gameState):
    if gameState.get_legal_moves() == []:
        return True
    else:
        return False


def min_value(gameState):
    if terminal_test(gameState):
        return 1
    v = 0
    for action in gameState.get_legal_moves():
        new_gameState = gameState.forecast_move(action)
        v = min(v, max_value(new_gameState))
        return v


def max_value(gameState):
    if terminal_test(gameState):
        return -1
    v = 0
    for action in gameState.get_legal_moves():
        new_gameState = gameState.forecast_move(action)
        v = max(v, min_value(new_gameState))
        return v


def minimax_decision(gameState):
    best_score = float("-inf")
    best_move = None
    for m in gameState.get_legal_moves():
        v = min_value(gameState.forecast_move(m))
        if v > best_score:
            best_score = v
            best_move = m
    return best_move

best_moves = set([(0, 0), (2, 0), (0, 1)])
rootNode = GameState()
minimax_move = minimax_decision(rootNode)

print("Best move choices: {}".format(list(best_moves)))
print("Your code chose: {}".format(minimax_move))

if minimax_move in best_moves:
    print("That's one of the best move choices. Looks like your minimax-decision function worked!")
else:
    print("Uh oh...looks like there may be a problem.")


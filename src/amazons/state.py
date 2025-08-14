
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
BLOCK = -1

class GameState:
    def __init__(self, board_X = 10, board_y = 10, pos_player1 = [(0, 0), (0, 9)], pos_player2 = [(9, 0), (9, 9)],  case_blocked = [], turn_player = PLAYER1):
        self.board_X = board_X
        self.board_y = board_y
        self.pos_player1 = pos_player1
        self.pos_player2 = pos_player2
        self.case_blocked = case_blocked
        self.turn_player = turn_player
        self.board = [[EMPTY for _ in range(self.board_y)] for _ in range(self.board_X)]
        self.initialize_board()
        self.is_finished = False

    def initialize_board(self):
        print("Initializing board...")
        for i in range(self.board_X):
            for j in range(self.board_y):
                if (i, j) in self.case_blocked:
                    self.board[i][j] = BLOCK
                elif (i, j) in self.pos_player1:
                    self.board[i][j] = PLAYER1
                elif (i, j) in self.pos_player2:
                    self.board[i][j] = PLAYER2
                else:
                    self.board[i][j] = EMPTY

    def display_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))
        print("\n")

    ### Getters for the GameState class

    def get_player1_positions(self):
        return self.pos_player1
    
    def get_player2_positions(self):
        return self.pos_player2
    
    def get_board(self):
        return self.board
    
    def get_board_X(self):
        return self.board_X
    
    def get_board_y(self):
        return self.board_y
    
    def get_case_blocked(self):
        return self.case_blocked
    
    def get_turn_player(self):
        return self.turn_player
    
    def get_is_finished(self):
        return self.is_finished
    
    ### Setters for the GameState class

    def set_player1_positions(self, positions, new_positions):
        if positions == self.pos_player1[0]:
            self.pos_player1[0] = new_positions
        elif positions == self.pos_player1[1]:
            self.pos_player1[1] = new_positions
        self.initialize_board()

    def set_player2_positions(self, positions, new_positions):
        if positions == self.pos_player2[0]:
            self.pos_player2[0] = new_positions
        elif positions == self.pos_player2[1]:
            self.pos_player2[1] = new_positions
        self.initialize_board()

    def set_case_blocked(self, positions):
        self.case_blocked.append(positions)
        self.initialize_board()

    def set_turn_player(self, player):
        if self.turn_player == PLAYER1:
            self.turn_player = PLAYER2
        elif self.turn_player == PLAYER2:
            self.turn_player = PLAYER1

    def set_is_finished(self):
        if self.is_finished:
            self.is_finished = False
        else:
            self.is_finished = True
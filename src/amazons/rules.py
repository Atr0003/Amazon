

from amazons.state import GameState, EMPTY, BLOCK, PLAYER1, PLAYER2

class Rules:
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


    def ray_from(self, state, pos):
        x, y = pos
        moves = []
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < state.board_X and 0 <= ny < state.board_y:
                if state.board[nx][ny] == EMPTY:
                    moves.append((nx, ny))
                elif state.board[nx][ny] == BLOCK:
                    break
                else:
                    break
                nx += dx
                ny += dy
        return moves
    
    def legal_arrows(self, state, src):
        return self.ray_from(state, src)
    
    def legal_moves(self, state, src):
        return self.ray_from(state, src)
    
    def check_move(self, state, src, dest):
        if dest in self.legal_moves(state, src):
            return True
        return False
    
    def check_arrow(self, state, src, dest):
        if dest in self.legal_arrows(state, src):
            return True
        return False
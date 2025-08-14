

from state import GameState, EMPTY, BLOCK, PLAYER1, PLAYER2

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
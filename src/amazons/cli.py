from amazons.state import GameState, EMPTY, BLOCK, PLAYER1, PLAYER2
from amazons.rules import Rules
import pygame


def main():
    print("Amazons CLI OK")
    game = GameState()
    rules = Rules()


    while not game.get_is_finished():
        player = game.get_turn_player()
        print(f"Player {1 if player == PLAYER1 else 2}'s turn")
        game.display_board()
        positions = game.get_player_positions(player)
        choise = input(f"Enter your select choise amazon (e.g., 'choise 0 or 1'): ")
        if choise not in [str(i) for i in range(len(positions))]:
            print("Invalid choice, try again.")
            continue
        pos = positions[int(choise)]
        print(rules.legal_moves(game, pos))
        move_x = input("Enter your select possition move x : ")
        move_y = input("Enter your select possition move y : ")
        dest = (int(move_x), int(move_y))
        check_move = rules.check_move(game, pos, dest)
        if not check_move:
            print("Invalid move, try again.")
            continue

        game.set_player_positions(player, pos, dest)
        game.display_board()
        print(rules.legal_arrows(game, dest))
        arrow_x = input("Enter your select arrow x : ")
        arrow_y = input("Enter your select arrow  y : ")
        arrow = (int(arrow_x), int(arrow_y))
        check_arrow = rules.check_arrow(game, dest, arrow)
        if not check_arrow:
            print("Invalid arrow, try again.")
            continue
        game.set_case_blocked(arrow)
        game.display_board()
        #game.set_is_finished()
        game.set_turn_player(PLAYER2 if player == PLAYER1 else PLAYER1)
        coup = (pos, dest, arrow)
        game.set_stack(coup)
        print(game.get_stack())
    

if __name__ == "__main__":
    main()

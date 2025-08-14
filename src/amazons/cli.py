from state import GameState, EMPTY, BLOCK, PLAYER1, PLAYER2
from rules import Rules

def main():
    print("Amazons CLI OK")
    game = GameState()
    rules = Rules()

    while not game.get_is_finished():
        if game.get_turn_player() == PLAYER1:
            game.display_board()
            choise = input("Enter your select choise amazon (e.g., 'choise 0 or 1'): ")
            pos = game.get_player1_positions()[int(choise)]
            print(rules.legal_moves(game, pos))
            move_x = input("Enter your select possition move x : ")
            move_y = input("Enter your select possition move y : ")
            dest = (int(move_x), int(move_y))
            check_move = rules.check_move(game, pos, dest)
            if not check_move:
                print("Invalid move, try again.")
                continue

            # Update the position of the selected amazon
            game.set_player1_positions(pos, dest)
            game.display_board()
            #dest = game.get_player1_positions()[int(choise)]
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
            game.set_is_finished()  
            game.set_turn_player("PLAYER2")
            coup = (pos, dest, arrow)
            game.set_stack(coup)
            print(game.get_stack())
        else:
            print("Player 2's turn")

if __name__ == "__main__":
    main()

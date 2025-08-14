from state import GameState
from rules import Rules

def main():
    print("Amazons CLI OK")
    game = GameState()
    rules = Rules()

    while not game.get_is_finished():
        print(f"Current turn: {game.get_turn_player()}")
        game.display_board()
        choise = input("Enter your select choise amazon (e.g., 'choise 0 or 1'): ")
        pos = game.get_player1_positions()[int(choise)]
        print(rules.ray_from(game, pos))
        move_x = input("Enter your select possition move x : ")
        move_y = input("Enter your select possition move y : ")
        game.set_player1_positions(pos, (int(move_x), int(move_y)))
        game.display_board()
        pos = game.get_player1_positions()[int(choise)]
        print(rules.ray_from(game, pos))
        arrow_x = input("Enter your select arrow x : ")
        arrow_y = input("Enter your select arrow  y : ")
        game.set_case_blocked((int(arrow_x), int(arrow_y)))
        game.display_board()
        game.set_is_finished()  

if __name__ == "__main__":
    main()

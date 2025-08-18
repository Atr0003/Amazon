import pygame
from amazons.state import GameState, EMPTY, BLOCK, PLAYER1, PLAYER2

def InitializeBoard(screen):
    # Define the grid size and colors
    grid_size = 8
    cell_size = 100
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Create a grid surface
    screen = pygame.Surface((grid_size * cell_size, grid_size * cell_size))

    # Draw the grid
    for row in range(grid_size):
        for col in range(grid_size):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    setAmazonPositions(screen)

    return screen

def setAmazonPositions(screen):
    # Define the positions of the amazons
    state = GameState()
    amazon1_pos = state.get_player_positions(PLAYER1)[0]  # (0, 0)
    amazon2_pos = state.get_player_positions(PLAYER1)[1]  # (0, 7)
    amazon3_pos = state.get_player_positions(PLAYER2)[0]  # (7, 0)
    amazon4_pos = state.get_player_positions(PLAYER2)[1]  # (7, 7)

    # Draw the amazons on the grid
    amazon_color_1 = (255, 0, 0)  # Red color for amazons
    amazon_color_2 = (0, 225, 0)  # Red color for amazons
    pygame.draw.circle(screen, amazon_color_1, (amazon1_pos[0] * 100 + 50, amazon1_pos[1] * 100 + 50), 30)
    pygame.draw.circle(screen, amazon_color_1, (amazon2_pos[0] * 100 + 50, amazon2_pos[1] * 100 + 50), 30)
    pygame.draw.circle(screen, amazon_color_2, (amazon3_pos[0] * 100 + 50, amazon3_pos[1] * 100 + 50), 30)
    pygame.draw.circle(screen, amazon_color_2, (amazon4_pos[0] * 100 + 50, amazon4_pos[1] * 100 + 50), 30)

def main():
    print("Amazons Pygame UI OK")
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Amazons Game")

    # Main game loop
    running = True
    board = InitializeBoard(screen)  # Crée la grille une seule fois
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(board, (0, 0))  # Affiche la grille sur l'écran

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
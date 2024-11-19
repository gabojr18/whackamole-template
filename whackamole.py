import pygame
import random


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_img = pygame.image.load("mole.png")

        cell_size = 32
        rows, columns = 16, 20
        mole_pos_x, mole_pos_y = 0, 0

        game_active = True
        while game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_active = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if mole_pos_x <= click_x < mole_pos_x + cell_size and mole_pos_y <= click_y < mole_pos_y + cell_size:
                        mole_pos_x = random.randint(0, columns - 1) * cell_size
                        mole_pos_y = random.randint(0, rows - 1) * cell_size

            screen.fill((173, 216, 230))
            for vertical in range(0, 640, cell_size):
                pygame.draw.line(screen, (0, 0, 0), (vertical, 0), (vertical, 512))
            for horizontal in range(0, 512, cell_size):
                pygame.draw.line(screen, (0, 0, 0), (0, horizontal), (640, horizontal))

            screen.blit(mole_img, mole_img.get_rect(topleft=(mole_pos_x, mole_pos_y)))
            pygame.display.update()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

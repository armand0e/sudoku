from turtle import back
import pygame
from sudoku_generator import SudokuGenerator, Board, Cell, generate_sudoku


class Button:
    def __init__(self, surface, rect, screen):
        self.screen = screen
        self.surface = surface
        self.rect = rect
        self.clicked = False

    def draw(self, surface):
        drawn = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                drawn = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on screen
        surface.blit(self.surface, self.rect)

        return drawn


def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def main():
    # init
    pygame.init()
    size = screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku!")

    # game variables
    game_paused = False
    menu_state = "main"

    # style
    title_font = pygame.font.Font(None, 100)
    menu_font = pygame.font.Font(None, 60)

    # surfaces
    title_surface = title_font.render("Main Menu", 1, [255, 255, 255], [64, 64, 64])
    easy_surface = menu_font.render("Easy", 1, [255, 255, 255], [64, 64, 64])
    medium_surface = menu_font.render("Medium", 1, [255, 255, 255], [64, 64, 64])
    hard_surface = menu_font.render("Hard", 1, [255, 255, 255], [64, 64, 64])

    # images
    resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    options_img = pygame.image.load("images/button_options.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()

    # rectangles
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
    easy_rect = easy_surface.get_rect(center=(2 * screen_width // 5, screen_height // 2))
    medium_rect = medium_surface.get_rect(center=(3 * screen_width // 5, screen_height // 2))
    hard_rect = hard_surface.get_rect(center=(4 * screen_width // 5, screen_height // 2))

    # buttons
    easy_button = Button(screen_width // 5, 200, easy_surface, 0.5)
    medium_button = Button(2 * screen_width // 5, 200, medium_surface, 0.5)
    hard_button = Button(3.5 * screen_width // 5, 200, hard_surface, 0.5)
    resume_button = Button(304, 125, resume_img, 0.5)
    options_button = Button(297, 250, options_img, 0.5)
    quit_button = Button(336, 375, quit_img, 0.5)
    back_button = Button(332, 450, back_img, 0.5)

    # main
    program_run = True
    while program_run:
        # window background
        screen.fill([200, 200, 200])

        # check menu state
        if menu_state == "main":
            screen.blit(title_surface, title_rect)
            screen.blit(easy_surface, easy_rect)
            screen.blit(medium_surface, medium_rect)
            screen.blit(hard_surface, hard_rect)

            if easy_button.draw(screen):
                menu_state = "easy"
            if medium_button.draw(screen):
                menu_state = "medium"
            if hard_button.draw(screen):
                menu_state = "hard"
        if menu_state == "easy":
            difficulty = "easy"
            menu_state = "game"
        if menu_state == "medium":
            difficulty = "medium"
            menu_state = "game"
        if menu_state == "hard":
            difficulty = "hard"
            menu_state = "game"

        if menu_state == "game":
            board = Board(400, 400, screen, difficulty)
            board.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()
    print(generate_sudoku(9, 1))


if __name__ == '__main__':
    main()

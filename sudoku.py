import pygame
from sudoku_generator import SudokuGenerator, Board, Cell, generate_sudoku

def main():
    # init
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    
    # style
    background_image = pygame.image.load("background.jpg")
    
    
    # main
    program_run = True
    while program_run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                quit()
            
        screen.blit(background_image, (0,0))
        pygame.display.flip()
    print(generate_sudoku(9,1))

if __name__ == '__main__':
    main()
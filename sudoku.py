import pygame
from sudoku_generator import SudokuGenerator, Board, Cell

def main():
    # init
    pygame.init()
    size = screen_width, screen_height = 600, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku!")

    # game variables
    menu_state = "main"

    # style
    title_font = pygame.font.SysFont("Courier New", 100)
    menu_font = pygame.font.SysFont("Courier New", 30)
    title_font.set_bold(True)
    title_font.set_underline(False)

    # surfaces
    title_surface = title_font.render("Sudoku!", 1, [64, 64, 64])
    easy_surface = menu_font.render(" Easy ", 1, [64, 64, 64], [255, 255, 255])
    medium_surface = menu_font.render(" Medium ", 1, [64, 64, 64], [255, 255, 255])
    hard_surface = menu_font.render(" Hard ", 1, [64, 64, 64], [255, 255, 255])

    # rectangles
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    easy_rect = easy_surface.get_rect(center=(screen_width // 4, screen_height // 2))
    medium_rect = medium_surface.get_rect(center=(2 * screen_width // 4, screen_height // 2))
    hard_rect = hard_surface.get_rect(center=(3* screen_width // 4, screen_height // 2))
    
    runs = 0
    board = Board(450, 450, screen, 30)
    game = False
    # main
    while True:
        # window background
        screen.fill([200, 200, 200])
        screen.blit(title_surface, title_rect)
        screen.blit(easy_surface, easy_rect)
        screen.blit(medium_surface, medium_rect)
        screen.blit(hard_surface, hard_rect)

        if easy_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                difficulty = 30
                game = True
                break
        if medium_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                difficulty = 40
                game = True
                break
        if hard_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                difficulty = 40
                game = True
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()        
        pygame.display.update()
    
    # game screen
    while game:
        # init board
        if runs == 0:
            board = Board(450, 450, screen, difficulty)
            runs += 1
        # draw board
        board.draw()
        if board.selected == True:
            width = 4
            x1, y1 = board.selected_cell.x, board.selected_cell.y
            x2, y2 = x1 + 50, y1 + 50
            pygame.draw.line(board.screen, (255,0,0), (x1, y1), (x2, y1), width)
            pygame.draw.line(board.screen, (255,0,0), (x1, y1), (x1, y2), width)
            pygame.draw.line(board.screen, (255,0,0), (x2, y1), (x2, y2), width)
            pygame.draw.line(board.screen, (255,0,0), (x1, y2), (x2, y2), width) 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if board.click(x,y) != None:
                    row, col = board.click(x,y)
                    board.select(row,col)
            
            elif event.type == pygame.KEYDOWN:
                cell_input = None
                match event.key:
                    case pygame.K_1:
                        cell_input = 1
                    case pygame.K_2:
                        cell_input = 2
                    case pygame.K_3:
                        cell_input = 3
                    case pygame.K_4:
                        cell_input = 4
                    case pygame.K_5:
                        cell_input = 5
                    case pygame.K_6:
                        cell_input = 6
                    case pygame.K_7:
                        cell_input = 7
                    case pygame.K_8:
                        cell_input = 8
                    case pygame.K_9:
                        cell_input = 9
                if event.key in [pygame.K_DELETE, pygame.K_BACKSPACE]:
                    cell_input = 0
                if board.selected != False and cell_input != None:
                    if board.selected_cell.sketchable:
                        board.selected_cell.set_sketched_value(cell_input)
                        board.update_board()
                    
            elif event.type == pygame.QUIT:
                quit()
        pygame.display.update()
    

if __name__ == '__main__':
    main()

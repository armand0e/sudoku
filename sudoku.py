import pygame, random
from sudoku_generator import Board

def main():
    
    # init
    pygame.init()
    size = screen_width, screen_height = 650, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku")
    background_color = [200,200,200]
    
    # fonts
    title_font = pygame.font.SysFont("Courier New", 100)
    menu_font = pygame.font.SysFont("Courier New", 30)
    game_font = pygame.font.SysFont("Courier New", 25)
    game_font.set_bold(True)
    rules_font = pygame.font.SysFont("Courier New", 17)
    title_font.set_bold(True)
    title_font.set_underline(False)

    # surfaces
    title_surface = title_font.render("Sudoku!", 1, [64, 64, 64])
    easy_surface = menu_font.render(" Easy ", 1, [64, 64, 64], [255, 255, 255])
    medium_surface = menu_font.render(" Medium ", 1, [64, 64, 64], [255, 255, 255])
    hard_surface = menu_font.render(" Hard ", 1, [64, 64, 64], [255, 255, 255])
    winner_surface = title_font.render("You Win!", 1, [64, 64, 64])
    loser_surface = title_font.render("You Lose!", 1, [64, 64, 64])
    menu_surface = menu_font.render(" Menu ", 1, [64, 64, 64], [255, 255, 255])
    retry_surface = menu_font.render(" Retry ", 1, [64, 64, 64], [255, 255, 255])
    newgame_surface = menu_font.render(" New Game ", 1, [64, 64, 64], [255, 255, 255])
    exit_surface = menu_font.render(" Exit ", 1, [64, 64, 64], [255, 255, 255])
    restart_surface = game_font.render(" Restart ", 1, [64, 64, 64], [255, 255, 255])
    reset_surface = game_font.render(" Reset ", 1, [64, 64, 64], [255, 255, 255])
    exitgame_surface = game_font.render(" Exit ", 1, [64, 64, 64], [255, 255, 255])
    rules_font.set_bold(True)
    rules_font.set_underline(True)
    rules_surface = rules_font.render("Rules", 1, [0, 0, 0])
    rules_font.set_bold(False)
    rules_font.set_underline(False)
    rule1_surface = rules_font.render("- Click on a cell to select it", 1, [0, 0, 0])
    rule2_surface = rules_font.render("- Type a value to sketch it into the cell", 1, [0, 0, 0])
    rule3_surface = rules_font.render("- Press backspace or delete to clear a cell", 1, [0, 0, 0])
    rule4_surface = rules_font.render("- Press enter to lock a cell in", 1, [0, 0, 0])
    
    # rectangles
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    easy_rect = easy_surface.get_rect(center=(screen_width // 4, screen_height // 2))
    medium_rect = medium_surface.get_rect(center=(2 * screen_width // 4, screen_height // 2))
    hard_rect = hard_surface.get_rect(center=(3 * screen_width // 4, screen_height // 2))
    winner_rect = winner_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    loser_rect = loser_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    menu_rect = menu_surface.get_rect(center=(screen_width // 4, 2*screen_height // 3))
    retry_rect = retry_surface.get_rect(center=(2 * screen_width // 4, 2*screen_height // 3))
    newgame_rect = newgame_surface.get_rect(center=(2 * screen_width // 4, 2*screen_height // 3))
    exit_rect = exit_surface.get_rect(center=(3 * screen_width // 4, 2*screen_height // 3))
    rules_rect = rules_surface.get_rect(center=(screen_width // 2, screen_height-105))
    rule1_rect = rule1_surface.get_rect(center=(screen_width // 2, screen_height-80))
    rule2_rect = rule2_surface.get_rect(center=(screen_width // 2, screen_height-60))
    rule3_rect = rule3_surface.get_rect(center=(screen_width // 2, screen_height-40))
    rule4_rect = rule4_surface.get_rect(center=(screen_width // 2, screen_height-20))
    reset_rect = reset_surface.get_rect(center=(screen_width // 4, 25*1.5))
    restart_rect = restart_surface.get_rect(center=(screen_width // 2, 25*1.5))
    exitgame_rect = exitgame_surface.get_rect(center=(3 * screen_width // 4, 25*1.5))
    exitmenu_rect = exit_surface.get_rect(center=(screen_width//2, 4*screen_height//5))
    
    # game variables
    runs = 0
    difficulty = 30
    board = Board(450, 450, screen, 30)
    winner = None
    game_state = "menu"
    program_run = True
    
    # loop
    while program_run:
        if game_state == "menu":
            
            # window background
            screen.fill(background_color)
            
            # blit title and buttons
            screen.blit(title_surface, title_rect)
            screen.blit(easy_surface, easy_rect)
            screen.blit(medium_surface, medium_rect)
            screen.blit(hard_surface, hard_rect)
            screen.blit(exit_surface, exitmenu_rect)
            if title_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    # easter egg - change background color
                    for i in range(3):
                        change = random.randint(5, 100)
                        background_color[i] = 200 - change
            if easy_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    difficulty = 30
                    runs = 0
                    winner = None
                    game_state = "game"
            if medium_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    difficulty = 40
                    runs = 0
                    winner = None
                    game_state = "game"
            if hard_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    difficulty = 50
                    runs = 0
                    winner = None
                    game_state = "game"
            if exitmenu_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()        
        
        # game screen
        if game_state == "game":
            
            # init board
            if runs == 0:
                board = Board(450, 450, screen, difficulty)
                runs += 1
            
            # fill background
            screen.fill(background_color)
            
            # blit buttons and rules
            screen.blit(reset_surface, reset_rect)
            screen.blit(restart_surface, restart_rect)
            screen.blit(exitgame_surface, exitgame_rect)
            screen.blit(rules_surface, rules_rect)
            screen.blit(rule1_surface, rule1_rect)
            screen.blit(rule2_surface, rule2_rect)
            screen.blit(rule3_surface, rule3_rect)
            screen.blit(rule4_surface, rule4_rect)
            
            # draw board
            board.draw()
            
            # buttons - Reset, Restart, Exit
            if restart_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    runs = 0
                    difficulty = 30
                    board = Board(450, 450, screen, 30)
                    winner = None
                    game_state = "menu"
                    program_run = True
            if reset_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    runs = 1
                    board.reset_to_original()
                    game_state = "game"
            if exitgame_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1:
                    quit()
            
            # draw red outline around selected cell
            if board.selected_cell is not None:
                width = 4
                x1, y1 = board.selected_cell.x, board.selected_cell.y
                x2, y2 = x1 + 50, y1 + 50
                pygame.draw.line(board.screen, (255,0,0), (x1, y1), (x2, y1), width)
                pygame.draw.line(board.screen, (255,0,0), (x1, y1), (x1, y2), width)
                pygame.draw.line(board.screen, (255,0,0), (x2, y1), (x2, y2), width)
                pygame.draw.line(board.screen, (255,0,0), (x1, y2), (x2, y2), width)
            
            
            for event in pygame.event.get():
                
                # clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if board.click(x,y) is not None:
                        row, col = board.click(x,y)
                        board.select(row,col)
                
                # keys
                elif event.type == pygame.KEYDOWN:
                    
                    if board.selected_cell is not None:
                        selected_row = int(board.selected_cell.row)
                        selected_col = int(board.selected_cell.col)
                        # arrow keys
                        match event.key:
                            case pygame.K_LEFT :
                                if selected_col > 0:
                                    selected_col -= 1
                            case pygame.K_RIGHT:
                                if selected_col < 8:
                                    selected_col += 1
                            case pygame.K_UP: 
                                if selected_row > 0:
                                    selected_row -= 1
                            case pygame.K_DOWN:
                                if selected_row < 8:
                                    selected_row += 1
                        board.select(selected_row, selected_col)
                    
                        # number keys
                        match event.key:
                            case pygame.K_1:
                                board.sketch(1)
                            case pygame.K_2:
                                board.sketch(2)
                            case pygame.K_3:
                                board.sketch(3)
                            case pygame.K_4:
                                board.sketch(4)
                            case pygame.K_5:
                                board.sketch(5)
                            case pygame.K_6:
                                board.sketch(6)
                            case pygame.K_7:
                                board.sketch(7)
                            case pygame.K_8:
                                board.sketch(8)
                            case pygame.K_9:
                                board.sketch(9)
                            case pygame.K_DELETE:
                                board.sketch(0)
                            case pygame.K_BACKSPACE:
                                board.sketch(0)
                            # enter/return
                            case pygame.K_RETURN:
                                # dont place_number if the sketched value is 0
                                if board.selected_cell.sketched_value != 0:
                                    board.place_number(board.selected_cell.sketched_value)
                                    board.selected_cell.sketchable = False
                                    board.update_board()
                                    # select the first empty cell
                                    if not board.is_full():
                                        row,col = board.find_empty()
                                        board.select(row,col)
                                
                    # check if board is full
                    if board.is_full():
                        board.update_board()
                        # check if they won
                        if board.check_board():
                            winner = True
                        else:
                            winner = False
                        game_state = "gameover"

                elif event.type == pygame.QUIT:
                    quit()
        
        # gameover screen
        if game_state == "gameover":
            # fill screen
            screen.fill(background_color)

            # winner screen
            if winner:
                
                # blit message and buttons
                screen.blit(winner_surface, winner_rect)
                screen.blit(menu_surface, menu_rect)
                screen.blit(newgame_surface, newgame_rect)
                screen.blit(exit_surface, exit_rect)
                
                # buttons
                if menu_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        runs = 0
                        board = Board(450, 450, screen, 30)
                        winner = None
                        game_state = "menu"
                        program_run = True
                if newgame_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        runs = 1
                        board = Board(450, 450, screen, difficulty)
                        game_state = "game"
                if exit_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        program_run = False
                        quit()
                
                # event handler
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()  
            
            # loser screen
            elif not winner:
                
                # blit message and buttons
                screen.blit(loser_surface, loser_rect)
                screen.blit(menu_surface, menu_rect)
                screen.blit(retry_surface, retry_rect)
                screen.blit(exit_surface, exit_rect)
                
                # buttons
                if menu_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        runs = 0
                        board = Board(450, 450, screen, 30)
                        winner = None
                        game_state = "menu"
                        program_run = True
                if retry_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        runs = 1
                        board.reset_to_original()
                        game_state = "game"
                if exit_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        program_run = False
                        quit()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                          
        pygame.display.update()

if __name__ == '__main__':
    main()
    
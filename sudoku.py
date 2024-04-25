import pygame
from sudoku_generator import Board

def main():
    # init
    pygame.init()
    size = screen_width, screen_height = 650, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sudoku")

    # style
    title_font = pygame.font.SysFont("Courier New", 100)
    menu_font = pygame.font.SysFont("Courier New", 30)
    game_font = pygame.font.SysFont("Courier New", 20)
    rules_font = pygame.font.SysFont("Courier New", 15)
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
    back_surface = game_font.render(" Back ", 1, [64, 64, 64], [255, 255, 255])
    rules_font.set_bold(True)
    rules_font.set_underline(True)
    rules_surface = rules_font.render("Rules", 1, [0, 0, 0])
    #rules_font.set_bold(False)
    rules_font.set_underline(False)
    rule1_surface = rules_font.render("- Click on a cell to select it", 1, [0, 0, 0])
    rule2_surface = rules_font.render("- Type a value to sketch it into the cell", 1, [0, 0, 0])
    rule3_surface = rules_font.render("- Press backspace or delete to clear a cell", 1, [0, 0, 0])
    rule4_surface = rules_font.render("- Press enter to lock a cell in", 1, [0, 0, 0])
    
    

    # rectangles
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    easy_rect = easy_surface.get_rect(center=(screen_width // 4, screen_height // 2))
    medium_rect = medium_surface.get_rect(center=(2 * screen_width // 4, screen_height // 2))
    hard_rect = hard_surface.get_rect(center=(3* screen_width // 4, screen_height // 2))
    winner_rect = winner_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    loser_rect = loser_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    menu_rect = menu_surface.get_rect(center=(screen_width // 4, 2*screen_height // 3))
    retry_rect = retry_surface.get_rect(center=(2 * screen_width // 4, 2*screen_height // 3))
    newgame_rect = newgame_surface.get_rect(center=(2 * screen_width // 4, 2*screen_height // 3))
    exit_rect = exit_surface.get_rect(center=(3* screen_width // 4, 2*screen_height // 3))
    back_rect = back_surface.get_rect(center=(50,25))
    rules_rect = rules_surface.get_rect(center=(screen_width // 2, screen_height-125))
    rule1_rect = rule1_surface.get_rect(center=(screen_width // 2, screen_height-100))
    rule2_rect = rule2_surface.get_rect(center=(screen_width // 2, screen_height-80))
    rule3_rect = rule3_surface.get_rect(center=(screen_width // 2, screen_height-60))
    rule4_rect = rule4_surface.get_rect(center=(screen_width // 2, screen_height-40))
    
    # init new game
    runs = 0
    difficulty = 30
    board = Board(450, 450, screen, 30)
    winner = None
    game_state = "menu"
    program_run = True
    # main
    while program_run:
        if game_state == "menu":
            # window background
            screen.fill([200, 200, 200])
            screen.blit(title_surface, title_rect)
            screen.blit(easy_surface, easy_rect)
            screen.blit(medium_surface, medium_rect)
            screen.blit(hard_surface, hard_rect)

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()        
            pygame.display.update()
        # game screen
        if game_state == "game":
            # init board
            if runs == 0:
                board = Board(450, 450, screen, difficulty)
                runs += 1
            
            # fill background
            screen.fill([200, 200, 200])
            
            # blit rules and back button
            screen.blit(back_surface, back_rect)
            screen.blit(rules_surface, rules_rect)
            screen.blit(rule1_surface, rule1_rect)
            screen.blit(rule2_surface, rule2_rect)
            screen.blit(rule3_surface, rule3_rect)
            screen.blit(rule4_surface, rule4_rect)
            
            # draw board
            board.draw()
            
            # back button
            if back_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        runs = 0
                        difficulty = 30
                        board = Board(450, 450, screen, 30)
                        winner = None
                        game_state = "menu"
                        program_run = True
            
            # if the selected cell is no longer selectable, deselect it.
            try:
                if board.selected_cell.sketchable == False and not board.is_full():
                    row, col = board.find_empty()
                    board.select(row,col)
            except AttributeError:
                pass
                
            # draw red outline around selected cell
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
                    elif event.key == pygame.K_RETURN:
                        for row in range(len(board.cells)):
                            if board.selected_cell.sketched_value != 0:
                                board.place_number(board.selected_cell.sketched_value)
                                board.selected_cell.sketchable = False
                                board.update_board()
                                
                    
                    if board.selected != False and cell_input != None:
                        if board.selected_cell.sketchable:
                            board.sketch(cell_input)
                    if board.is_full():
                        board.selected = False
                        if board.check_board():
                            winner = True
                        else:
                            winner = False
                        game_state = "gameover"
                        

                elif event.type == pygame.QUIT:
                    quit()
            pygame.display.update()
        
        # game over screen
        if game_state == "gameover":
            screen.fill([200, 200, 200])
           
            if winner:
                screen.blit(winner_surface, winner_rect)
                screen.blit(menu_surface, menu_rect)
                screen.blit(newgame_surface, newgame_rect)
                screen.blit(exit_surface, exit_rect)
                
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
                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()  
            elif not winner:
                screen.blit(loser_surface, loser_rect)
                screen.blit(menu_surface, menu_rect)
                screen.blit(retry_surface, retry_rect)
                screen.blit(exit_surface, exit_rect)
                if menu_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        game_state = "menu"
                if newgame_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        runs = 1
                        board.reset_to_original()
                        
                        game_state = "game"
                if exit_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0] == 1:
                        pygame.quit()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  
            pygame.display.update()        
  
                                
                                
                        
                    
            
        
    

if __name__ == '__main__':
    main()

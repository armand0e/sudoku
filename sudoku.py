
import pygame
from sudoku_generator import SudokuGenerator, Board, Cell, generate_sudoku

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

def main():
    # init
    pygame.init()
    size = screen_width, screen_height = 480*16/9, 480
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    
    # style
    background_image = pygame.image.load("background.jpg")
    title_font = pygame.font.Font(None, 100)
    menu_font = pygame.font.Font(None, 75)
    
    # surfaces
    title_surface = title_font.render("Sudoku!", 1, [255,255,255], [255,161,27])
    easy_surface = menu_font.render("Easy", 1, [255,255,255], [255,161,27])
    medium_surface = menu_font.render("Medium", 1, [255,255,255], [255,161,27])
    hard_surface = menu_font.render("Hard", 1, [255,255,255], [255,161,27])

    # rectangles
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
    easy_rect = easy_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    medium_rect = medium_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
    hard_rect = hard_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 200))

    # blit
    screen.blit(background_image, (0,0))
    #screen.fill([255,255,255])
    screen.blit(title_surface, title_rect)
    '''screen.blit(easy_surface, easy_rect)
    screen.blit(medium_surface, medium_rect)
    screen.blit(hard_surface, hard_rect)'''
    
    # buttons
    easy_button = Button(100,200, easy_rect, 0.8)
    medium_button = Button(100,200, medium_rect, 0.8)
    hard_button = Button(100,200, hard_rect, 0.8)
    
    # main
    program_run = True
    while program_run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                quit()
            if easy_button.draw(screen):
                pass
            if medium_button.draw(screen):
                pass
            if hard_button.draw(screen):
                pass

            '''if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    difficulty = "easy"
                elif medium_rect.collidepoint(event.pos):
                    difficulty = "medium"
                elif hard_rect.collidepoint(event.pos):
                    difficulty = "hard"
                print(difficulty)'''
        pygame.display.flip()
    print(generate_sudoku(9,1))

if __name__ == '__main__':
    main()
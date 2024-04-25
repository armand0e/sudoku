# put this at the start of the file
import pygame

# replace Cell class with this one

class Cell:
    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched = False
        self.sketchable = False
        if self.value == 0:
            self.sketchable = True
        self.sketched_value = 0
        self.size = 50
        self.x = self.col * self.size
        self.y = self.row * self.size 
    
    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.sketched = True
        self.sketched_value = value

    def draw(self):
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected. 
        font = pygame.font.SysFont("Courier New", 20)
        font.set_bold(True)
        pygame.draw.rect(self.screen, [255, 255, 255], (self.x, self.y, self.size, self.size), 0)
        centerx, centery = self.x + self.size/2, self.y + self.size/2
        if self.value != 0 or self.sketched_value != 0:
            if not self.sketchable:
                text_surface = font.render(str(self.value), 1, [64, 64, 64])
                text_rect = text_surface.get_rect(center=(centerx, centery))
                self.screen.blit(text_surface, text_rect)
            elif self.sketchable:
                text_surface = font.render(str(self.sketched_value), 1, [128, 128, 128])
                self.screen.blit(text_surface, (self.x+2,self.y+2))

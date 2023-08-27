# -*- coding: utf-8 -*-
"""
@author: 18019
"""

import pygame
import sys

def __main__():
    # Initialize Pygame
    pygame.init()
    
    # Constants for the game window
    WIDTH, HEIGHT = 300, 300
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Game variables
    turn = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouseX, mouseY = pygame.mouse.get_pos()
                
                # Calculate the cell clicked
                row = mouseY // (HEIGHT // 3)
                col = mouseX // (WIDTH // 3)
                
                # Check if the cell is empty and make a move
                if board[row][col] == '':
                    board[row][col] = turn
                    turn = 'O' if turn == 'X' else 'X'
    
        # Clear the screen
        win.fill(BLACK)
    
        # Draw the grid lines
        for i in range(1, 3):
            pygame.draw.line(win, WHITE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3))
            pygame.draw.line(win, WHITE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT))
    
        # Draw X and O on the board
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    pygame.draw.line(win, WHITE, (col * WIDTH // 3, row * HEIGHT // 3), ((col + 1) * WIDTH // 3, (row + 1) * HEIGHT // 3), 3)
                    pygame.draw.line(win, WHITE, ((col + 1) * WIDTH // 3, row * HEIGHT // 3), (col * WIDTH // 3, (row + 1) * HEIGHT // 3), 3)
                elif board[row][col] == 'O':
                    pygame.draw.circle(win, WHITE, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), WIDTH // 6, 3)
        
        winStatus = winCheck(board)
        print(winStatus)
        if winStatus != "A":
            winText = winStatus + " is the winner!"
            win.fill(BLACK)
            winButton = button(100, 100, 200, 200, winText, WHITE, BLACK)
            winButton.draw(win)
            #pygame.draw.rect(win, quit_button_color, quit_button_rect)
            #win.blit(quit_button_text, quit_text_rect)
            
            
        pygame.display.update()
        
    # Quit Pygame
    pygame.quit()
    sys.exit()

#will need to come up with a more clever way to do this
def winCheck(board):
    #print(board)
    if board[0][0] != '' and board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        winner = board[0][0]
        return winner
    if board[1][0] != '' and board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        winner = board[1][0]
        return winner
    if board[2][0] != '' and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        winner = board[2][0]
        return winner
    if board[0][1] != '' and board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        winner = board[0][1]
        return winner
    if board[0][2] != '' and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        winner = board[0][2]
        return winner
    if board[0][0] != '' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        winner = board[0][0]
        return winner
    if board[0][2] != '' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        winner = board[0][2]
        return winner
    if board[0][0] != '' and board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        winner = board[0][0]
        return winner
    return "A"

class button:
    def __init__(self, x, y, width, height, text, button_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

__main__()

# -*- coding: utf-8 -*-
"""
@author: 18019
"""

import pygame
import sys

def __main__():
    # Initialize Pygame
    pygame.init()
    newGameFlag = True
    # Constants for the game window
    WIDTH, HEIGHT = 500, 500
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Tic Tac Toe")
    score = {"X":0,"O":0}
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    gameStatus = True
    while newGameFlag == True:

        # Game variables
        turn = 'X'
        board = [['' for _ in range(3)] for _ in range(3)]
        
        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
                if event.type == pygame.VIDEORESIZE:
                    new_width, new_height = event.size
                    WIDTH, HEIGHT = new_width, new_height
                    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        
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
            drawStatus = checkDraw(board)
            if drawStatus == True:
                print(board)
                drawText = "DRAW"
                drawButton = button(50, 100, 200, 100, drawText, WHITE, BLACK)
                newGameText = "New Game"
                newGameButton = button(165,225,125,50,newGameText,WHITE,BLACK)
                quitText = "Quit"
                quitButton = button(25,225,100,50, quitText, WHITE, BLACK)
                win.fill(BLACK)
                drawButton.draw(win)
                newGameButton.draw(win)
                quitButton.draw(win)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if newGameButton.is_clicked(pygame.mouse.get_pos()):
                            print("New Game Button clicked!")
                            turn = 'X'
                            board = [['' for _ in range(3)] for _ in range(3)]
                            for i in range(1, 3):
                                pygame.draw.line(win, WHITE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3))
                                pygame.draw.line(win, WHITE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT))
                                gameStatus = True
                        if quitButton.is_clicked(pygame.mouse.get_pos()):
                            print("Quit Button clicked!")
                            newGameFlag = False
                            running = False
            if winStatus != "A":
                if gameStatus == True:  
                    print(winStatus)
                    score[winStatus] = score[winStatus] + 1
                    gameStatus = False
                    print(score)
                winText = winStatus + " is the winner!"
                newGameText = "New Game"
                xScore = str(score['X'])
                oScore = str(score['O'])
                scoreText = "X: " + xScore + "    O: " + oScore
                quitText = "Quit"
                win.fill(BLACK)
                winButton = button(50, 100, 200, 100, winText, WHITE, BLACK)
                newGameButton = button(165,225,125,50,newGameText,WHITE,BLACK)
                quitButton = button(25,225,100,50, quitText, WHITE, BLACK)
                scoreButton = button(25,25,125,50, scoreText, WHITE, BLACK)
                winButton.draw(win)
                newGameButton.draw(win)
                quitButton.draw(win)
                scoreButton.draw(win)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if newGameButton.is_clicked(pygame.mouse.get_pos()):
                            print("New Game Button clicked!")
                            turn = 'X'
                            board = [['' for _ in range(3)] for _ in range(3)]
                            for i in range(1, 3):
                                pygame.draw.line(win, WHITE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3))
                                pygame.draw.line(win, WHITE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT))
                                gameStatus = True
                        if quitButton.is_clicked(pygame.mouse.get_pos()):
                            print("Quit Button clicked!")
                            newGameFlag = False
                            running = False
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

def checkDraw(board):
    draw = False
    k = 0
    for i in board:
        for j in i:
            if j != '':
                k+= 1
    if k == 9:
        draw = True
    return draw

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

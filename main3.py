import pygame, sys
from sudoku_generator import *
from Board import board


# importing all needed classes as well as libraies needed for Main

# def draw_game_start(screen):
#     start_title_font = pygame.font.Font(None, 100)
#     button_font = pygame.font.Font(None, 70)
#
#     screen.fill()


class Button:
    def __init__(self, x, y, width, height, text, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.font = pygame.font.SysFont("Arial", 24)
        self.text_surface = self.font.render(text, True, (0, 0, 0))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.text_surface, (self.x + self.width // 2 - self.text_surface.get_width() // 2,
                                        self.y + self.height // 2 - self.text_surface.get_height() // 2))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.x <= event.pos[0] <= self.x + self.width and self.y <= event.pos[1] <= self.y + self.height:
                return True
        return False


pygame.init()
# Initializing Pygame

# Seting up Pygame window
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Defining colors (will be black and white)
WHITE = (255, 255, 255)

# seting up game variables
difficulty = None
board_size = 9
empty_cells = {'easy': 30, 'medium': 40, 'hard': 50}
# Default difficulty is easy

# Creating board object
# board_values = generate_sudoku(board_size, 30)
# board = board(WIDTH, HEIGHT, screen, difficulty, board_values)
# board.board_values
screen.fill(WHITE)

LINE_COLOR = (245, 152, 66)
start_title_font = pygame.font.Font(None, 60)

game_state = "start_menu"


def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))

    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
    button = Button(100, 100, 100, 50, "Easy", (255, 0, 0))
    button2 = Button(100, 200, 100, 50, "Medium", (255, 0, 0))
    button3 = Button(100, 300, 100, 50, "Hard", (255, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if button.is_clicked(event):
                print("Button clicked!")
                board_values = generate_sudoku(board_size, 30)
                return board_values

            if button2.is_clicked(event):
                print("Button 2 clicked")
                board_values = generate_sudoku(board_size, 40)
                return board_values
                # board = board(WIDTH, HEIGHT, screen, difficulty, board_values)

            if button3.is_clicked(event):
                print("Button 3 clicked")
                board_values = generate_sudoku(board_size, 50)
                return board_values
                # board = board(WIDTH, HEIGHT, screen, difficulty, board_values)

        screen.fill((0, 0, 0))

        button.draw(screen)
        button2.draw(screen)
        button3.draw(screen)

        pygame.display.flip()


def success_page():
    print("inside")
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Won!', True, (255, 255, 255))

    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
    button = Button(100, 100, 100, 50, "Exit", (255, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if button.is_clicked(event):
                print("Exit clicked!")

        button.draw(screen)
        pygame.display.flip()


def failure_page():
    print("inside")
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Lost!', True, (255, 255, 255))

    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
    button = Button(100, 100, 100, 50, "RESTART", (255, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if button.is_clicked(event):
                print("Restart clicked!")

        button.draw(screen)
        pygame.display.flip()


board_values = draw_start_menu()
board = board(WIDTH, HEIGHT, screen, difficulty, board_values)

# This will be the main game loop
running = True
while running:
    screen.fill(WHITE)
    # value = False
    # handling each potential event
    reset = Button(20, 530, 100, 50, "RESTART", (255, 0, 0))
    restart = Button(200, 530, 100, 50, "EXIT", (255, 0, 0))
    exit = Button(400, 530, 100, 50, "EXIT", (255, 0, 0))


    for event in pygame.event.get():
        if exit.is_clicked(event):
            pygame.quit()
            sys.exit()

        if restart.is_clicked(event):
            pass

        if reset.is_clicked(event):
            pass

        if event.type == pygame.QUIT:
            # running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # handling mouse clicks
            pos = pygame.mouse.get_pos()
            row, col = board.click(*pos)
            if row is not None and col is not None:
                board.select(row, col)
        elif event.type == pygame.KEYDOWN:
            # handling key press's
            if event.unicode.isdigit():
                if board.selected_cell is not None:
                    board.place_number(int(event.unicode))
            elif event.key == pygame.K_RETURN:
                board.selected_cell = None
            elif event.key == pygame.K_BACKSPACE:
                if board.selected_cell is not None:
                    board.clear_selected_cell()

    if board.is_full():
        if board.check_board():
            print("Success")
            success_page()
        else:
            print("incorrect")
            failure_page()
        break

    # drawing board
    board.draw()

    reset.draw(screen)
    restart.draw(screen)
    exit.draw(screen)


    # Updating the display
    pygame.display.flip()

# This quits Pygame
pygame.quit()

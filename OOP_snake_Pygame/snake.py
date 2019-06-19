from pygame.locals import *
import pygame

class Snake():
    x = None
    y = None
    width = 20
    height = 20
    speed = 20
    direction = None
    color = (255, 0, 0)

    #The following function block and the update function allow the snake to continue movement until another button is pressed.
    def move_right(self):
        self.direction = "right"
    def move_left(self):
        self.direction = "left"
    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"

    def update(self):
        if self.direction == "right":
            self.x += self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "down":
            self.y += self.speed

class Game():
    display_width = 1000
    display_height = 1000
    display_color = (0, 0, 0)
    snake = Snake()
    snake.y = display_height / 2
    snake.x = display_width / 2
    running = True

    #This runs once when the main function is called, this initializes required PyGame modules, draws the map, and draws the snake at its starting point.  
    def setup(self):
        pygame.init()
        window = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Snake!")
        window.fill(self.display_color)            
        pygame.draw.rect(window, (self.snake.color), (self.snake.x, self.snake.y, self.snake.width, self.snake.height))
        pygame.display.update()

    #This updates the screen to display the current location of all objects.
    def refresh(self, window):
        window.fill(self.display_color)            
        pygame.draw.rect(window, (self.snake.color), (self.snake.x, self.snake.y, self.snake.width, self.snake.height))
        pygame.display.update()

    #This contains the core functionality of the game, including the main game loop. Pressing Escape or the Exit button will close the PyGame window.
    def main(self):
        self.setup()
        keys = pygame.key.get_pressed()

        while self.running:
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()

                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            self.snake.update()
            self.refresh(pygame.display.set_mode((self.display_width, self.display_height)))
            pygame.time.delay(100)

        pygame.quit()
tester = Game()
tester.main()
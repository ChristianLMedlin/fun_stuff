from pygame.locals import *
import pygame

class Snake():
    x = 0
    y = 0
    width = 20
    height = 20
    speed = 20
    direction = None
    color = (255, 0, 0)

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
    snake = Snake()
    display_width = 500
    display_height = 500
    display_color = (0, 0 ,0)
    running = True

    def setup(self):
        pygame.init()
        window = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Snake!")
        window.fill(self.display_color)            
        pygame.draw.rect(window, (self.snake.color), (self.snake.x, self.snake.y, self.snake.width, self.snake.height))
        pygame.display.update()

    def main(self):
        self.setup()
        keys = pygame.key.get_pressed()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

tester = Game()
tester.main()
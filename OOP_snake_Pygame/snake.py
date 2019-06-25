from pygame.locals import *
import pygame
import random


class Snake():
    x = None
    y = None
    width = 20
    height = 20
    speed = 20
    direction = None
    head_color = (255, 0, 0)
    body_color = (180, 0, 0)

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
    window = pygame.display.set_mode((display_width, display_height))
    food_x = random.randrange(0, display_width, 20)
    food_y = random.randrange(0, display_height, 20)
    food_color = (0, 255, 0)
    snake = Snake()
    snake.x = display_width / 2
    snake.y = display_height / 2
    snake.body = []
    snake.body_length = 0
    running = True

    #When main() is called, this initializes required PyGame modules, draws the map, and draws the snake at its starting point.  
    def setup(self):
        pygame.init()
        pygame.display.set_caption("Snake!")
        self.window.fill(self.display_color)            
        pygame.draw.rect(self.window, (self.snake.head_color), (self.snake.x, self.snake.y, self.snake.width, self.snake.height))
        pygame.display.update()
        self.food_sound = pygame.mixer.music
        self.food_sound.load("Food.ogg")

    #This updates the screen to display the current location of all objects.
    def refresh(self, window):
        self.window.fill(self.display_color)   

        for i in self.snake.body:
            for snake_x, snake_y in i.items():
                pygame.draw.rect(self.window, self.snake.body_color, (snake_x, snake_y, self.snake.width, self.snake.height))
         
        pygame.draw.rect(self.window, self.food_color, (self.food_x, self.food_y, self.snake.width, self.snake.height))
        pygame.draw.rect(self.window, self.snake.head_color, (self.snake.x, self.snake.y, self.snake.width, self.snake.height))

        pygame.display.update()

    #Generates a new random location for the food.
    def food_eaten(self):
        self.food_sound.play(0)
        self.food_x = random.randrange(0, self.display_width, 20)
        self.food_y = random.randrange(0, self.display_height, 20)

    #This needs to increase the length of the snake by 2 when food is eaten. This will be 2 elements inserted into a list, the elements will be the previous snake coordinates.
    def control_body(self):
        self.snake.body.insert(0, {self.snake.x: self.snake.y})

        while len(self.snake.body) > self.snake.body_length:
            del self.snake.body[self.snake.body_length]

    #This displays the game over text and resets snake direction and coordinates.
    def game_over(self):
        game_over_text = pygame.font.Font('pixel_font.ttf', 64).render("Game over!", False, (255, 0, 0))
        text_surface = game_over_text.get_rect()
        text_surface.center = (self.display_width / 2, self.display_height / 2)
        self.death_sound = pygame.mixer.music
        self.death_sound.load("Death.ogg")
        self.death_sound.set_volume(.5)
        self.death_sound.play(0)
        self.snake.y = self.display_height / 2
        self.snake.x = self.display_width / 2
        self.snake.body = []
        self.snake.body_length = 0
        self.snake.direction = None
        self.play_again = False

        self.window.blit(game_over_text, text_surface)
        pygame.display.update()     

        while not self.play_again:
            pygame.time.delay(100)

            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN and event.key ==  pygame.K_SPACE:
                    self.play_again = True

    #This contains the core functionality of the game, including the main game loop. Pressing Escape or the Exit button will close the PyGame window.
    def main(self):
        self.setup()
        keys = pygame.key.get_pressed()

        while self.running:
            #This causes the player to lose if they go out of bounds.

            #Game now restarts when space button is pressed, need to add text informing the player.
            if self.snake.x > self.display_width or self.snake.x < 0 or self.snake.y > self.display_width or self.snake.y < 0:
                self.game_over()
                

            #The following code closes the game of the X button is clicked and controls movements for the snake when the arrow keys are pressed.
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
            
            if self.snake.x == self.food_x and self.snake.y == self.food_y:
                self.snake.body_length += 3
                self.food_eaten()

            self.control_body()
            self.snake.update()
            self.refresh(self.window)
            pygame.time.delay(100)

        pygame.quit()


play_game = Game()
play_game.main()

'''  
Chomp sound effect is unreliable: Sound takes too long to activate and sometimes doesn't play if two foods are eaten in quick succession.

After the player loses a game, the game should restart when the player presses the arrow keys again, there should be a text display that informs the user of this option.
'''
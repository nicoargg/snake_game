import pygame, random, sys
from pygame.color import Color
from pygame.draw import rect
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            snake_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(190,110,120),snake_rect)

    def snake_move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]


class Fruit:
    def __init__(self):
        self.x = random.randint(0,cell_number -1)
        self.y = random.randint(0,cell_number -1)
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.snake_move()
        self.eated()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def eated(self):
        if self.fruit.pos == self.snake.body[0]:
            


cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,100)

main_game = Main()

if __name__ == "__main__":
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    main_game.snake.direction = Vector2(-1,0)                
                
                
        
        
        screen.fill((145,220,40))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(90)

#Importin librarys
import pygame
from constants import *
from player import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Clear and fills the screen
        screen.fill(000)
        
        #Draws player
        for draw in drawable:
            draw.draw(screen)

        #updates player
        for updates in updatable:
            updates.update(dt)

        #updates screen
        pygame.display.flip()
        
        #Regulates fps
        dt = clock.tick(60) / 1000
        # print(player.position)

    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
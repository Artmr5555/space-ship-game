from random import randint
import pygame

pygame.init()

width = 1080
height = 720

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('SpaceShip')


class Ship:
    def __init__(self, x, y):
        self.color = (255, 150, 245)
        self.width = 80
        self.height = 80
        self.ship = pygame.image.load('spaceship.png')
        self.ship = pygame.transform.scale(self.ship, (self.width, self.height))
        self.image = win.blit(self.ship, [x, y])
        #self.draw = pygame.draw.rect(win, self.color,[x, y, self.width, self.height])


class Comet:
    def __init__(self, enemy_x, enemy_y):
        self.color = (255, 0, 0)
        self.width = 60
        self.enemy = pygame.image.load('enemy.png')
        self.enemy = pygame.transform.scale(self.enemy, (self.width, self.width))
        self.enemy_image = win.blit(self.enemy, [enemy_x, enemy_y])
        #self.draw = pygame.draw.rect(win, self.color, [enemy_x, enemy_y, self.width, self.width])

        def draw(self, enemy_x, enemy_y):
            self.draw1 = pygame.draw.rect(win, self.color, [enemy_x, enemy_y, self.width, self.width])
            self.draw2 = pygame.draw.rect(win, self.color, [enemy_x, enemy_y, self.width, self.width])
            self.draw3 = pygame.draw.rect(win, self.color, [enemy_x, enemy_y, self.width, self.width])


class Laser:
    def __init__(self, laser_x, laser_y):
        self.color = (0, 255, 0)
        self.width = 6
        self.height = 40
        self.draw = pygame.draw.rect(win, self.color, [laser_x, laser_y, self.width, self.height])


class Laser_enemy:
    def __init__(self, laser_enemy_x, laser_enemy_y):
        self.color = (255, 0, 0)
        self.width = 6
        self.height = 30
        self.draw = pygame.draw.rect(win, self.color, [laser_enemy_x , laser_enemy_y, self.width, self.height])


def game():
    x = ((width / 2) / 10) * 10
    y = height - 150
    laser_x = (((x + (Ship(x, y).width / 2)) / 10) * 10) - 3
    laser_y = height - 148
    enemy_x = (randint(100 , width -100)/10) * 10
    enemy_y = (randint(0, (height - 400)) / 10) * 10
    laser_enemy_x = enemy_x + 28
    laser_enemy_y = enemy_y + 5
    vel = 20
    vel_laser = 0
    font = pygame.font.SysFont("Times New Roman, Arial", 30, True)
    text = font.render('Game Over. Press SPACE to Continue or ENTER to Exit', True, (0, 0, 0))

    gameover = False
    run = True

    while run:
        laser_enemy = pygame.Rect(Laser_enemy(laser_enemy_x, laser_enemy_y).draw)
        ship = pygame.Rect(Ship(x, y).image)
        while gameover:
            if pygame.Rect.colliderect(laser_enemy, ship):
                win.fill((155, 0, 0))
                win.blit(text, (width / 6, height / 2))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game()
                            gameover = False
                        if event.key == pygame.K_KP_ENTER:
                            run = False
                            gameover = False


        pygame.time.delay(5)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vel_laser = - (Laser(laser_x, laser_y).height / 1)
                    if laser_y <= 0:
                        laser_x = ((x + (Ship(x, y).width / 2)) - 4)
                        laser_y = height - 148
                        pygame.display.update()

        comet = Comet(enemy_x, enemy_y).enemy_image
        laser = pygame.Rect(Laser(laser_x, laser_y).draw)

        if pygame.Rect.colliderect(laser, comet) == False:
            laser_y += vel_laser
        elif pygame.Rect.colliderect(laser, comet) == True:
            laser_y = height - 148
            vel_laser = 0
            laser_x = ((x + (Ship(x, y).width / 2)) - 2) + vel
            pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= vel
        if keys[pygame.K_d]:
            x += vel

        if laser_y == height - 148:
            laser_x = ((x + (Ship(x, y).width / 2)) - 2)

        if pygame.Rect.colliderect(laser, comet):
            enemy_x = ((randint(100, width - 100) / 10) * 10)
            enemy_y = (randint(0, (height - 400)) / 10) * 10
            laser_enemy_x = enemy_x + 28
            laser_enemy_y = enemy_y + 5

        if laser_enemy_y > height:
            laser_enemy_y = enemy_y + 5
        else:
            vel_l_enemy = (Laser_enemy(laser_enemy_x, laser_enemy_y).height * 2)
            laser_enemy_y += vel_l_enemy
            pygame.display.update()



        win.fill((50, 0, 80))
        Laser(laser_x, laser_y).draw
        Ship(x, y).image
        Laser_enemy(laser_enemy_x, laser_enemy_y).draw
        Comet(enemy_x, enemy_y).enemy_image

        pygame.display.update()


game()
pygame.quit()

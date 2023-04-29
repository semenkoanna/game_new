import pygame 
import os
pygame.init()
def abs_path():
    path_object = os.path.abspath(__file__ + "/..") 
    path_object = path_object.split("\\")
    path_object = "\\".join(path_object)
    return path_object
work_directory = abs_path()
os.chdir(work_directory)


window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Догонялки')

x1 = 350
y1 = 250

x2 = 150
y2 = 250

speed = 20


lol = pygame.transform.scale(pygame.image.load('images/chiken.png'), (100, 100))
lol2 = pygame.transform.scale(pygame.image.load('images/wolf.png'), (100, 100))
clock = pygame.time.Clock()
FPS = 60

background = pygame.transform.scale(pygame.image.load('images/background.jpg'), (700, 500))
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    window.blit(background,(0, 0))
    window.blit(lol, (x1,y1))
    window.blit(lol2, (x2, y2))


    if pygame.key.get_pressed()[pygame.K_LEFT] and x1 > 5:
        x1 -= speed
    if pygame.key.get_pressed()[pygame.K_RIGHT] and x1 < 595:
        x1 += speed
    if pygame.key.get_pressed()[pygame.K_UP] and y1 > 5:
        y1 -= speed
    if pygame.key.get_pressed()[pygame.K_DOWN] and y1 < 395:
        y1 +=speed


    if pygame.key.get_pressed()[pygame.K_a] and x2 > 5:
        x2 -= speed
    if pygame.key.get_pressed()[pygame.K_d] and x2 < 595:
        x2 += speed
    if pygame.key.get_pressed()[pygame.K_w] and y2 > 5:
        y2 -= speed
    if pygame.key.get_pressed()[pygame.K_s] and y2 < 395:
        y2 += speed



    pygame.display.update()
    clock.tick(FPS)
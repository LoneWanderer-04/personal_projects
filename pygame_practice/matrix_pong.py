import sys, pygame
pygame.init()

size = width, height = 1024, 768
speed = [1,1]
black = 0,155,0

screen = pygame.display.set_mode(size)

character_size = 10
up = (0, -character_size)
down = (0, character_size)
left = (-character_size, 0)
right = (character_size, 0)

paddle_1 = pygame.transform.scale((pygame.image.load('neo.png')), (100, 200))
paddle_1_rect = paddle_1.get_rect(topright=(width, 0))

paddle_2 = pygame.transform.scale(pygame.image.load('neo.png'), (100, 200))
paddle_2_rect = paddle_2.get_rect(topleft=(0,0))

bullet = pygame.transform.scale((pygame.image.load('bullet.png')), (100, 50))
bullet_rect = bullet.get_rect(center=(width/2, height / 2))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # paddle_1_rect = paddle_1_rect.move(speed)
    if pygame.key.get_pressed()[pygame.K_UP]:
        newpos = paddle_1_rect.move(up)
        if newpos.top > 0:
            paddle_1_rect = newpos
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        newpos = paddle_1_rect.move(down)
        if newpos.bottom < height:
            paddle_1_rect = newpos

    if pygame.key.get_pressed()[pygame.K_w]:
        newpos = paddle_2_rect.move(up)
        if newpos.top > 0:
            paddle_2_rect = newpos
    elif pygame.key.get_pressed()[pygame.K_s]:
        newpos = paddle_2_rect.move(down)
        if newpos.bottom < height:
            paddle_2_rect = newpos

    bullet_rect = bullet_rect.move(speed)
    if bullet_rect.left < 0 or bullet_rect.right > width:
        speed[0] = -speed[0]
    elif bullet_rect.colliderect(paddle_1_rect):
        speed[0] = -speed[0] - 0.1
        speed[1] = -speed[1]
    elif bullet_rect.colliderect(paddle_2_rect):
        speed[0] = -speed[0] + 0.1
        speed[1] = -speed[1]
    if bullet_rect.top < 0 or bullet_rect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    screen.blit(paddle_1, paddle_1_rect)
    screen.blit(pygame.transform.flip(paddle_2, True, False), paddle_2_rect)
    screen.blit(pygame.transform.flip(bullet, False, True), bullet_rect)
    pygame.display.flip()

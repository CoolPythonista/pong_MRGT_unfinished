# Загрузка модуля pygame.
import pygame




# Загрузка внутренних модулей Pygame
pygame.init()

# Разрешение окна СЦЕНЫ.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна СЦЕНЫ:
SCENE = pygame.display.set_mode(
    [SCREEN_WIDTH, SCREEN_HEIGHT],     # Разрешение окна программы.
    flags=pygame.SCALED,               # Интрукция для вертикальной синхронизации.
    vsync=True                         # Вертикальная синхронизация.
)
# Заголовок окна СЦЕНА:
pygame.display.set_caption('Pong')



# Блок для загрузки объектов:


ball = pygame.Rect(800 / 2 - 50, 600/2 - 50, 100, 100)
ball_speed_x = 5
ball_speed_y = 5

player = pygame.Rect(20, 0, 20, 100)



# Мышка

pygame.mouse.set_visible(False)




# Настройки FPS:
FPS = 60
clock = pygame.time.Clock()



# СЦЕНА:
running = True
while running:
    clock.tick(FPS)

    # Заливка фона сцены RGB
    SCENE.fill([35, 35, 35])

    #print(ball.x)

    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y


    if ball.x > 800 - 100:
        ball_speed_x *= -1

    if ball.x < 0 - 200:
        ball.x = 800 / 2 - 50
        ball.y = 600 / 2 - 50


    if ball.y > 600 - 100:
        ball_speed_y *= -1

    if ball.y < 0:
        ball_speed_y *= -1



    if ball.colliderect(player):
        ball_speed_x *= -1

    


    pygame.draw.ellipse(SCENE, [232, 143, 166], ball)

    pygame.draw.rect(SCENE, [132, 173, 184], player)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= 5

    if keys[pygame.K_s]:
        player.y += 5



    # Обработка событий в окне сцены:
    for event in pygame.event.get():

        # Нажатие на крестик окна завершит цикл СЦЕНЫ:
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()


# Выход из программы.
pygame.quit()










    

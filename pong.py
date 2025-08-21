# Загрузка модуля pygame.
import pygame
import os






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

enemy = pygame.Rect(800 - 20 - 20, 0, 20, 100)

# Ryuk

ryuk_frames = os.listdir('assets/ryuk')

ryuk_surfs = []
for frame in ryuk_frames:
    img = pygame.image.load(f'assets/ryuk/{frame}')
    ryuk_surfs.append(img)


# Звук/Sound

bgm = pygame.mixer.Sound('assets/bgm_1.mp3')
bgm.set_volume(0.2)
bgm.play()


ball_hit = pygame.mixer.Sound('assets/ball_hit.wav')
ball_hit.set_volume(0.2)


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


    if ball.x > 800 + 100:
        ball.x = 800 / 2 - 50
        ball.y = 600 / 2 - 50
        ball_speed_x = 5
        ball_speed_y = 5

    if ball.x < 0 - 200:
        ball.x = 800 / 2 - 50
        ball.y = 600 / 2 - 50
        ball_speed_x = 5
        ball_speed_y = 5


    if ball.y > 600 - 100:
        ball_speed_y *= -1

    if ball.y < 0:
        ball_speed_y *= -1



    if ball.colliderect(player):
        ball_speed_x *= -1.1
        ball_hit.play()

    if ball.colliderect(enemy):
        ball_speed_x *= -1.1
        ball_hit.play()


    pygame.draw.ellipse(SCENE, [232, 143, 166], ball)

    pygame.draw.rect(SCENE, [132, 173, 184], player)

    pygame.draw.rect(SCENE, [220, 220, 153], enemy)

    # AI
    enemy.y = ball.y


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










    

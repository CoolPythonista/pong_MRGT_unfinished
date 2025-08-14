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
pygame.display.set_caption('Mitsuki')

# Блок для загрузки объектов:




player = pygame.Rect(SCREEN_WIDTH/2 - 25, SCREEN_HEIGHT/2 - 25, 50, 50)

enemy = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 100, 200, 200)


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


    player.center = pygame.mouse.get_pos()


    pygame.draw.rect(SCENE, [235, 235, 235], player)

    


    if player.colliderect(enemy):
        pygame.draw.ellipse(SCENE, [255, 209, 244], enemy)
    else:
        pygame.draw.ellipse(SCENE, [245, 2, 128], enemy)




    # Обработка событий в окне сцены:
    for event in pygame.event.get():

        # Нажатие на крестик окна завершит цикл СЦЕНЫ:
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()


# Выход из программы.
pygame.quit()










    

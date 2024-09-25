import os                                                               #* Импонтируем библиотеку ос
import pygame                                                           #* Импонтируем библиотеку пайгейм
import math                                                             #* Импонтируем класс матиматика
import set                                                              #* Импонтируем библиотеку сет - это мой файл с расчётами и картой
import pygame.cursors


pygame.init()                                                           #* Инцизация всех классов


def mapping(a, b):                                                      #* Функция которая принимает значение а и b
        return (a // set.TILE) * set.TILE, (b // set.TILE) * set.TILE   #* возращает расчёт хо и уо

class Settings:                                                         #TODO Создаём класс Настройки для настройки игры
    def __init__(self):                                                 #! Создаём "магический метод" для создания объекта
        self.clock = pygame.time.Clock()                                #* Создаём часы 
        self.display_mode = (set.WIDTH, set.HEIGHT)                     #* Переменна для размера экрана
        self.display = pygame.display.set_mode(self.display_mode)       #* Создаём экран
        self.display_color = (0, 0, 0)                                  #* Цвет фона
        self.directory = os.path.dirname(__file__)                      #* Создаём полный путь
        self.game_active = True                                         #* Переменная для работы цикла игры
        self.type_cursor = pygame.SYSTEM_CURSOR_CROSSHAIR
        #TODO  self.type_cursor = pygame.SYSTEM_CURSOR_WAIT
        self.cursor = pygame.mouse.set_cursor(self.type_cursor)
        self.Fps_hide = True
        self.Map_hide = True
        self.go_up = False
        self.go_down = False
        self.go_left = False
        self.go_right = False
        self.turn_right = False
        self.turn_left = False

    def upload_map(self):                                               #TODO метод для загрузки карты
        for j, row in enumerate(set.text_map):                          #! Создаём цикл "for" где переменная j будет принимат индекс строки (начиная с 0), ещё принимаеться row которая будет содержать текущую строку из карты
            for i, char in enumerate(row):                              #! Создаём цикл "for" где переменная i будет принимат индекс строки (начиная с 0), переменная char которая будет содержать текущий символ из строки row
                if char == "W":                                         #* Если char равен W то ...
                    set.world_map.add((i * set.TILE, j * set.TILE))     #* в кардеж добовляем координаты стен

    def draw_map(self):
        for x, y in set.world_map:
            if x < set.WIDTH and y < set.HEIGHT:
                 pygame.draw.rect(self.display, (0, 0, 0), (x, y, set.TILE, set.TILE))
                 wall = pygame.draw.rect(self.display, (156, 156, 156), (x, y, set.TILE, set.TILE), 1)
                 if player.hitbox.colliderect(wall):

                    if player.hitbox.right >= wall.left and player.hitbox.right <= wall.left + player.speed:
                        player.hitbox.right = wall.left
                    if player.hitbox.left <= wall.right and player.hitbox.left >= wall.right - player.speed:
                        player.hitbox.left = wall.right                    
                    if player.hitbox.top <= wall.bottom and player.hitbox.top >= wall.bottom - player.speed:
                        player.hitbox.top = wall.bottom                    
                    if player.hitbox.bottom >= wall.top and player.hitbox.bottom <= wall.top + player.speed:
                        player.hitbox.bottom = wall.top
                    player.x, player.y = player.hitbox.topleft
                
    def ray_casting(self, sc, player_pos, player_angle):
        self.sc = sc
        cur_angle = player_angle - set.HALF_FOV
        xo, yo = player_pos
        for ray in range(set.NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            for depth in range(set.MAX_DEPTH):
                x = xo + depth * cos_a
                y = yo + depth * sin_a
                # pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
                if (x // set.TILE * set.TILE, y // set.TILE * set.TILE) in set.world_map:
                    depth *= math.cos(player_angle - cur_angle)
                    depth = max(depth, 0.00001)
                    proj_height = min(int(set.PROJ_COEFF / depth), 2 * set.HEIGHT)
                    c = 255 / (1 + depth * depth * 0.00002)
                    color_wall = (c - 8, c - 8, c - 8)
                    pygame.draw.rect(sc, color_wall, (ray * set.SCALE, set.HALF_HEIGHT - proj_height // 2, set.SCALE, proj_height))
                    break
                
                if capybara.live == True:
                    enemy_distance = math.sqrt((capybara.x - x) ** 2 + (capybara.y - y) ** 2)
                    if enemy_distance < capybara.size:
                        depth *= math.cos(player_angle - cur_angle)
                        depth = max(depth, 0.00001)
                        proj_height = min(int(set.PROJ_COEFF / depth), 2 * set.HEIGHT)
                        c = 255 / (1 + depth * depth * 0.00002)
                        color_enemy = (c - 2, c / 5, c / 6)
                        pygame.draw.rect(self.sc, color_enemy, (ray * set.SCALE, set.HALF_HEIGHT - proj_height // 2, set.SCALE, proj_height))
                        break
            cur_angle += set.DELTA_ANGLE


    def draw_sky(self):
        #sky_texture_scaled = pygame.transform.scale(sky.sky_texture, (set.WIDTH + 10, set.HALF_HEIGHT))
        #self.display.blit(sky_texture_scaled, (-5, 0))
        pygame.draw.rect(self.display,  (40, 49, 74), (0, set.HALF_HEIGHT, set.WIDTH, set.HALF_HEIGHT))

    def draw_floor(self):
        floor_texture_scaled = pygame.transform.scale(grass.grass_texture, (set.WIDTH, set.HALF_HEIGHT))  # Измените на правильную текстуру пола
        self.display.blit(floor_texture_scaled, (0, set.HALF_HEIGHT))
        #pygame.draw.rect(self.display, set.COLOR_FLOOR, (0, 0, set.WIDTH, set.HALF_HEIGHT))

settings = Settings()


class Textures():
    def __init__(self):
        self.sky = 'ceiling.jpg'
        self.wall = 'wall.jpg'
        self.grass = 'floot_white.jpg'
        self.sky_texture = pygame.image.load(settings.directory + '/image/' + self.sky).convert()
        self.wall_texture = pygame.image.load(settings.directory + '/image/' + self.wall).convert()
        self.grass_texture = pygame.image.load(settings.directory + '/image/' + self.grass).convert()

sky = Textures()
grass = Textures()

class Enemy():
    def __init__(self, size, x=0, y=0, speed=5, hp = 5):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.hp = hp
        self.live = True
        self.color = (12, 119, 43)

    def death_vraga(self):
        self.live = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw_enemy(self):
        pygame.draw.circle(settings.display, self.color, (int(self.x), int(self.y)), 12)

capybara = Enemy(5, 369, 280)

class Text_FPS():
    def __init__(self):
        font_link = settings.directory + 'Merchant Copy Doublesize.ttf'
        self.font = pygame.font.SysFont(font_link, 30)
        self.text_color = (255, 255, 255)
        self.text_obj = None
        self.update_text("FPS: 0")

    def update_text(self, text):
        self.text_obj = self.font.render(text, True, self.text_color)

    def draw_text(self, display):
        display.blit(self.text_obj, (50, 45))

fps_text = Text_FPS()


class Player:
    def __init__(self, x, y, angle=0, speed=1):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.hitbox = pygame.Rect(self.x, self.y, 12, 12)
        
    def draw(self, display):
        pygame.draw.circle(settings.display, (0, 250, 0), (int(self.x), int(self.y)), 12)

    def draw_direction_line(self, display):
        end_pos = (int(player.x + set.WIDTH * math.cos(player.angle)), int(player.y + set.WIDTH * math.sin(player.angle)))
        pygame.draw.line(settings.display, (20, 250, 64), player.pos, end_pos)

    @property
    def pos(self):
        return(self.x, self.y)

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        if settings.go_up == True:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        if settings.go_down == True:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if settings.go_left == True:
            self.x += self.speed * cos_a
            self.y += -self.speed * sin_a
        if settings.go_right == True:
            self.x += -self.speed * cos_a
            self.y += self.speed * sin_a
        if settings.turn_right == True:
            self.angle += 0.02
        if settings.turn_left == True:
            self.angle -= 0.02
        self.hitbox.topleft = (self.x, self.y)
            
    def hit(self):
        if capybara.hp <= 0:
            capybara.death_vraga()
        else:
            capybara.hp -= 1
            # print("Больно типа")

player = Player(set.WIDTH / 4 + 50, set.HEIGHT / 2 - 52)

settings.upload_map()

def map_on():
    player.draw(settings.display)
    player.draw_direction_line(settings.display)
    settings.draw_map()

while settings.game_active:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            settings.game_active = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                settings.game_active = False

            if event.key == pygame.K_w:
                settings.go_up = False
            if event.key == pygame.K_s:
                settings.go_down = False
            if event.key == pygame.K_a:
                settings.go_left = False
            if event.key == pygame.K_d:
                settings.go_right = False
            if event.key == pygame.K_LEFT:
                settings.turn_left = False
            if event.key == pygame.K_RIGHT:
                settings.turn_right = False

            if event.key == pygame.K_LSHIFT:
                player.speed = 3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                player.speed = 10
            if event.key == pygame.K_b:
                settings.Fps_hide = not settings.Fps_hide
            if event.key == pygame.K_m:
                settings.Map_hide = not settings.Map_hide
                
            if event.key == pygame.K_w:
                settings.go_up = True
            if event.key == pygame.K_s:
                settings.go_down = True
            if event.key == pygame.K_a:
                settings.go_left = True
            if event.key == pygame.K_d:
                settings.go_right = True
            if event.key == pygame.K_LEFT:
                settings.turn_left = True
            if event.key == pygame.K_RIGHT:
                settings.turn_right = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            capybara_rect = capybara.get_rect()
            player.hit()


    player.draw(settings.display)
    end_pos = (int(player.x + set.WIDTH * math.cos(player.angle)), int(player.y + set.WIDTH * math.sin(player.angle)))
    pygame.draw.line(settings.display, (20, 250, 64), player.pos, end_pos)
    settings.draw_map()
    settings.display.fill(settings.display_color)
    player.move()
    settings.draw_sky()
    settings.draw_floor()

    settings.ray_casting(settings.display, player.pos, player.angle)


    if settings.Map_hide == False:
        map_on()
        if capybara.live == True:
            capybara.draw_enemy()

    if settings.Fps_hide == False:
        fps = settings.clock.get_fps()
        fps_text.update_text(f'FPS: {int(fps)}')
        fps_text.draw_text(settings.display)

    pygame.display.flip()
    settings.clock.tick(60)
pygame.quit()


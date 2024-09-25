import math

WIDTH = 1536
HEIGHT = 864


HALF_HEIGHT = HEIGHT / 2
WIDTH_HALF = WIDTH / 2

player_pos = (WIDTH_HALF, HALF_HEIGHT)
player_speed = 2

text_map = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W...W.........................W",
    "W...WWWWWWW...WWWWWWW.WWWWW.WWW",
    "W.........W...W...............W",
    "WWWWWWWWW.W...W..WWWWWWWWWW...W",
    "W.......W.W...W..WW...WW......W",
    "W...WWWWW.WWWWW.......WW......W",
    "W.....................WW......W",
    "W...W.........................W",
    "W...W.WWWWWWWWWWWWW...WWWWWWW.W",
    "W...W..WW.........W........W..W",
    "W...W...W.WWWWWWW.WW.......W..W",
    "W...WWWWW.W.....W..WWW.....W..W",
    "WWWWW.......WWW.W....W.....W..W",
    "W.......WW.WWWW.WWWWWW.....WWWW",
    "W...........WWW...............W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


world_map = set()
textures = len(text_map)

TILE = 50

FOV = math.pi / 3  # Угол обзора (60 градусов в радианах)
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS  # Шаг угла между лучами
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # Дистанция между игроком и экраном
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS + 5

COLOR_FLOOR = (20, 155, 225) 
COLOR_CEILING = (67, 69, 97)  

TEXTURE_WIDTH =  236
TEXTURE_HEIGHT = 236
TEXTURE_SCALE = TEXTURE_WIDTH // TILE


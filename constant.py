import pygame


video = pygame.display.Info()
SIZE = 800, 600 # video.current_w, video.current_h
PLAYER_COORDINATES = SIZE[0] // 2, SIZE[1] // 2
SCREEN = pygame.display.set_mode(SIZE) # pygame.display.set_mode(flags=pygame.FULLSCREEN)

ALL_SPRITES = pygame.sprite.Group()     # группа для всех спрайтов
ENTITIES = pygame.sprite.Group()        # группа для сущностей
OBSTACLES = pygame.sprite.Group()       # группа для фоновых
WORLD = pygame.sprite.Group()           # группа для всего, кроме игрока
SOUND_PISTOL_SHOOT = pygame.mixer.Sound(file='sounds\\bang_08.ogg')
SOUND_MACHINE_GUN = pygame.mixer.Sound(file='sounds\\bang_06.ogg')
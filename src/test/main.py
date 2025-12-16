# Initialization, variables
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

WIDTH = 480
HEIGHT = 640
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.lives = 3

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH // 2, 100))
        self.health = 50

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -8

# main
def game():
    player = Player()
    enemy = Enemy()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    running = True
    
    while running:
        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(60)

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface((6, 6))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = dx
        self.dy = dy


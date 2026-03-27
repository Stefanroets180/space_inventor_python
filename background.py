import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        # Load and scale background to screen size for better performance
        original_image = pygame.image.load("background.jpg")
        screen_size = screen.get_size()
        self.image = pygame.transform.scale(original_image, screen_size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

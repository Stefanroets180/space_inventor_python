import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialise the ship and set it's initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.speed_up_scale = 1.1

        # Load ship's image & get a rectangle
        self.image = pygame.image.load('ships.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every ship should appear at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Save center ship coordinates
        self.center = float(self.rect.centerx)

        # Move flag
        self.moving_right = False
        self.moving_left = False
        
        # Touch/mouse control support
        self.touch_control = False
        self.target_x = None

    def update(self):
        """Update ship position considering the flag"""
        # Touch/mouse control - move ship toward target position
        if self.touch_control and self.target_x is not None:
            distance = self.target_x - self.center
            if abs(distance) > 5:  # Deadzone to prevent jitter
                if distance > 0 and self.rect.right < self.screen_rect.right:
                    self.center += min(self.ai_settings.ship_speed_factor, abs(distance))
                elif distance < 0 and self.rect.left > 0:
                    self.center -= min(self.ai_settings.ship_speed_factor, abs(distance))
        # Keyboard control
        else:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor

        # Update rect attribute based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship in current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place the ship at the center of bottom side"""
        self.center = self.screen_rect.centerx

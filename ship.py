import pygame

class Ship:
    """Manages Player Ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        # spawn ship bottom center 
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update position based on movement flags"""
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
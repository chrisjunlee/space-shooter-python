import sys, pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Manages game assets and behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        pygame.display.set_caption("Space Shoot")
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.bg_color
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        
    def run_game(self):
        """Start main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.screen_freq)
    
    def _check_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_handler(event)
            elif event.type == pygame.KEYUP:
                self._keyup_handler(event)
                

    def _update_screen(self):
        # Screen elements; the order matters!
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # render screen
        pygame.display.flip()


    def _keydown_handler(self, event):
        if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _keyup_handler(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
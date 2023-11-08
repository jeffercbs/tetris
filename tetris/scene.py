import pygame


class Scene(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.play = pygame.image.load("tetris/assets/start.png")
        self.image = pygame.display.get_surface().copy()
        self.sprites = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.background()
        self.switch = None
        self.timer = 0

    def background(self):
        self.image.fill((0, 0, 0))
        self.image.blit(self.play, self.play.get_rect(center=(150, 300)))

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and self.switch:
                    self.switch()

        # keep track of time
        self.timer += dt

        # update our own sprites and draw stuff
        self.sprites.update(events, dt)
        self.background()
        self.sprites.draw(self.image)

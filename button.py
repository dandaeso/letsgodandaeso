import pygame

class Button:
    def __init__(self, x, y, width, height, image1, image2, button_type=False):
        self.image1 = image1
        self.image2 = image2
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)  # 버튼을 중앙에 위치
        self.button_type = button_type

    def draw(self, surface,mx,my):
        if self.rect.collidepoint((mx, my)):
            surface.blit(self.image2, (self.rect.left, self.rect.top))
            #pygame.draw.rect(surface, (255, 0, 0), self.rect, 4)
        else:
            surface.blit(self.image1, (self.rect.left, self.rect.top))



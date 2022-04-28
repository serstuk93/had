import pygame

#button
class Button():
    def __init__(self,widthpos,heightpos , image , scale ):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (widthpos,heightpos)
        self.clicked = False

    def draw(self, surface):
        action = False

        #get mouse position
        position_mouse = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(position_mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))


        return action

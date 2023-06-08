import pygame

class Player():
    def __init__(self,imgl,imgr):
        self.imgl = imgl
        self.imgr = imgr
        
        self.img = imgr
        self.rect = self.img.get_rect()
        self.rect.width = self.img.get_width() 
        self.rect.height = self.img.get_height()    
                
        self.rect.top = 275
        self.rect.left = 300

        self.velocity = 7

    #method to track player movement
    def movement(self):
    
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]: 
            self.rect.left += self.velocity 
            self.img = self.imgr
        if key[pygame.K_LEFT]:
            self.rect.left -= self.velocity 
            self.img = self.imgl
    
    #method to draw the player
    def draw_player(self,screen):
        self.screen = screen
        self.screen.blit(self.img,(self.rect.left,self.rect.top))
        #the rectangle of the player (good to visualize collisions)
        #pygame.draw.rect(self.screen,(200,0,0),self.rect)

    

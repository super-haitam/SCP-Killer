import pygame
pygame.init
grass = pygame.image.load("assets/grass.png")
grass = pygame.transform.scale_by(grass,2)
dirt = pygame.image.load("assets/dirt.png")
dirt = pygame.transform.scale_by(dirt,2)
class Platform():
    def __init__(self):
        self.x = 0
        self.y = 0
        #the structure of the map (btw its a good way to make collisions and the easiet way to customize your levels "not only for platformers")
        self.game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
                        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                        ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]
    
    #method to check if there is a tile and draw it 
    def draw_platform(self,screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.tiles_rect = [] #so this is a list that contains the cells or (tiles) which can make collisions with the player
        for row in self.game_map:
            self.x = 0
            for tiles in row:
                if tiles == '1':
                    self.screen.blit(dirt,(self.x * 32,self.y * 32))
                if tiles == '2':
                    self.screen.blit(grass,(self.x * 32,self.y * 32))

                self.x += 1
            
            self.y += 1
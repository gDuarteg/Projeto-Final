
import pygame
import pygame.locals
import random


branco = (255,255,255)
marrom = (199,111,80)
cinza = (150,150,150)
vermelho = (230,0,0)
preto = (0,0,0)

#======================= CLASSES ====================================

class Aviao(pygame.sprite.Sprite):
    
    def __init__(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(200,100))
        self.rect.x = px
        self.rect.y = py

    def move(self):
        self.velx = 0
        self.vely = 0
        key = pygame.key.get_pressed()
        if self.rect.x >= 0:
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.velx = -8
        if self.rect.x <= 600:
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.velx = 8
        if self.rect.y > 0:
            if key[pygame.K_UP] or key[pygame.K_w]:
                self.vely = -8 
        if self.rect.y <= 500:
            if key[pygame.K_DOWN] or key[pygame.K_s]:
                self.vely = 8
        self.rect.x += self.velx
        self.rect.y += self.vely

class Balao(pygame.sprite.Sprite):
    def __init__(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def move(self):
        self.velx = 0
        self.vely = 0
        self.velx = -3
        self.rect.x += self.velx 
        self.rect.y += self.vely

class Fundilho(pygame.sprite.Sprite):
    def __init__(self,arquivo_imagem,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(200,100))
        self.rect.x = px
        self.rect.y = py
        
    def move(self):
        self.rect.x
        self.rect.y

class Tiros(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,5])
        self.image.fill(cinza)
        self.rect = self.image.get_rect()
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.rect.x = aviao.rect.x + 120
            self.rect.y = aviao.rect.y + 50
        self.rect.x += 12
#====================== INICIAÇÃO ===================================

pygame.init()

tiros = Tiros()

tela = pygame.display.set_mode((800, 600),0,32)

pygame.display.set_caption("Jogo A+")

fundo = pygame.image.load("imagem_fundo.jpg").convert()

relogio = pygame.time.Clock()

aviao_group = pygame.sprite.Group()
balao_group = pygame.sprite.Group()
tiro_group = pygame.sprite.Group()
    
aviao = Aviao("imagem_aviao.png",40,40)

aviao_group.add(aviao)

balao = Balao("imagem_balao.png",random.randrange(750,800),random.randrange(600))

balao_group.add(balao)
tiro_group = pygame.sprite.Group()

#======================= LOOP PRINCIPAL =============================
y=0
rodando = True
while rodando:
    
    relogio.tick(60)     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aviao_group.add(tiros)
                tiro_group.add(tiros)

    aviao.move()
    balao.move()
    tiros.move()
    
    tela.blit(fundo,(0,0))
    
    y-=1
    rel_x = y % fundo.get_rect().width
    tela.blit(fundo,(rel_x-fundo.get_rect().width,0))
    if rel_x<1920:
        tela.blit(fundo,(rel_x,0))
    
    aviao_group.draw(tela)         
    balao_group.draw(tela)          
    tiro_group.draw(tela)
    pygame.display.update()    
pygame.quit()

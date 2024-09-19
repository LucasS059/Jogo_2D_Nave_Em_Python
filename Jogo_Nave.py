import pygame # biblioteca pygame
import cria_objeto
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura_tela=1250
altura_tela=719
tela=pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Planetas")

# Carregar o efeito sonoro
efeito_sonoro=pygame.mixer.Sound("explode.ogg")

# Carregar a imagem de fundo
imagem_fundo = pygame.image.load("image/space.jpg")

# Carregando asteroide e outros objetos
aster = pygame.image.load("image/asteroid.png")
nave_alien1 = pygame.image.load("image/nave_alien.png")
cometa1 = pygame.image.load("image/cometa.png")
saturno1 = pygame.image.load("image/saturno.png")
bola_fogo1 = pygame.image.load("image/bola_fogo.png")
metal1 = pygame.image.load("image/metal.png")
marte1 = pygame.image.load("image/marte.png")
venus1 = pygame.image.load("image/venus.png")
meteorito1 = pygame.image.load("image/meteorito.png")
meteorito2 = pygame.image.load("image/meteorito2.png")



# diminuindo a escala do asteroide
asteroide=pygame.transform.scale(aster,(52,71))
nave_alien=pygame.transform.scale(nave_alien1,(52,71))
cometa=pygame.transform.scale(cometa1,(52,71))
saturno=pygame.transform.scale(saturno1,(52,71))
bola_fogo=pygame.transform.scale(bola_fogo1,(52,71))
metal=pygame.transform.scale(metal1,(52,71))
marte=pygame.transform.scale(marte1,(52,71))
venus=pygame.transform.scale(venus1,(52,71))
meteorito=pygame.transform.scale(meteorito1,(52,71))
meteorito_2=pygame.transform.scale(meteorito2,(52,71))

# Carregando nave
nav=pygame.image.load("image/fighter.png")
# diminuindo a escala da nave
nave=pygame.transform.scale(nav,(130,64))
nave=pygame.transform.flip(nave, True, False)

# criando sprites
# criando sprites com posições fixas
sprite1 = cria_objeto.objeto(asteroide, (500, 100))
sprite2 = cria_objeto.objeto(nave, (0, 250)) 
sprite3 = cria_objeto.objeto(nave_alien, (600, 150))
sprite4 = cria_objeto.objeto(cometa, (700, 200))
sprite5 = cria_objeto.objeto(saturno, (800, 250))
sprite6 = cria_objeto.objeto(bola_fogo, (900, 300))
sprite7 = cria_objeto.objeto(metal, (1000, 350))
sprite8 = cria_objeto.objeto(marte, (1100, 400))
sprite9 = cria_objeto.objeto(venus, (1200, 450))
sprite10 = cria_objeto.objeto(meteorito, (1300, 500))
sprite11 = cria_objeto.objeto(meteorito_2, (1400, 550))


# criando grupo de sprites para facilitar a manipulação dos mesmos
grupo_sprites=pygame.sprite.Group(sprite1,sprite2,sprite3,sprite4,sprite5, sprite6, sprite7, sprite8, sprite9, sprite10, sprite11)

# obtendo as dimensões da imagem
largura_imagem_fundo,altura_imagem_fundo=imagem_fundo.get_size()

# Posição inicial da imagem de fundo
posicao_x=0

# valor inicial da variável de temporização
tempo=0

#variaveis para a velocidade do asteroide
vel1 = 1

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tempo=tempo+1  # variável de ajuste do tempo
    if tempo==10:
        tempo=0
        # Atualizar a posição da imagem de fundo
        posicao_x=posicao_x+1

    # lendo as teclas
    teclas=pygame.key.get_pressed()

    # se UP foi pressionada
    if teclas[pygame.K_UP]:
        sprite2.rect.y-=5

    # se DOWN foi pressionada
    if teclas[pygame.K_DOWN]:
        sprite2.rect.y+=5

    if teclas[pygame.K_LEFT]:
        sprite2.rect.x-=5

    if teclas[pygame.K_RIGHT]:
        sprite2.rect.x+=5

    # mudando a posição dos sprites dos asteróides para que ele apareceça na tela sempre que desaparecer
    sprite1.rect.x-=vel1
    sprite3.rect.x-=vel1
    sprite4.rect.x-=vel1
    
    sprite5.rect.x-=vel1

    sprite6.rect.x-=vel1
    sprite7.rect.x-=vel1
    sprite8.rect.x-=vel1
    
    sprite9.rect.x-=vel1
    sprite10.rect.x-=vel1
    sprite11.rect.x-=vel1

    if sprite1.rect.x<-52:
        sprite1.rect.x=800
        sprite1.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 

    if sprite3.rect.x<-52:
        sprite3.rect.x=800
        sprite3.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 
    
    if sprite4.rect.x<-52:
        sprite4.rect.x=800
        sprite4.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 
    
    if sprite5.rect.x<-52:
        sprite5.rect.x=800
        sprite5.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 
    
    if sprite6.rect.x<-52:
        sprite6.rect.x=800
        sprite6.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 
    
    if sprite7.rect.x<-52:
        sprite7.rect.x=800
        sprite7.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 

    if sprite8.rect.x<-52:
        sprite8.rect.x=800
        sprite8.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 

    if sprite9.rect.x<-52:
        sprite9.rect.x=800
        sprite9.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 
    
    if sprite10.rect.x<-52:
        sprite10.rect.x=800
        sprite10.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 
    
    if sprite11.rect.x<-52:
        sprite11.rect.x=800
        sprite11.rect.y=random.uniform(1, 629) #sorteia a posição do asteróide
        vel1 = random.uniform(1, 10) # mudando a velocidade do asteroide de forma aleatoria 

    # atualizando sprites
    grupo_sprites.update()

    # Verificar se a imagem de fundo atingiu o final da tela
    if posicao_x>=largura_imagem_fundo:
        posicao_x=0   

    # Preencher a tela com a cor de fundo
    tela.fill((0,0,0))

    # Desenhar a imagem de fundo na tela
    tela.blit(imagem_fundo,(-posicao_x,0))

    # desenhando sprites na tela    
    grupo_sprites.draw(tela)

    # Atualizar a tela
    pygame.display.flip()

    # Atraso em ms
    pygame.time.delay(10)

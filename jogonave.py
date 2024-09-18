import pygame # biblioteca pygame
import cria_objeto
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura_tela=1250
altura_tela=800
tela=pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Planetas")

# Carregar o efeito sonoro
efeito_sonoro=pygame.mixer.Sound("explode.ogg")

# Carregar a imagem de fundo
imagem_fundo=pygame.image.load("nebulosa.jpg")

# Carregando asteroide
aster=pygame.image.load("asteroid.png")
lua1=pygame.image.load("lua.png")
ovo1=pygame.image.load("ovo.png")
homem_ferro1=pygame.image.load("hferro.png")
fogo1=pygame.image.load("fogo.png")
martelo1=pygame.image.load("martelo.png")
carro1=pygame.image.load("carro.png")
moto1=pygame.image.load("moto.png")
lixo1=pygame.image.load("lixo.png")
musk1=pygame.image.load("musk.png")


# diminuindo a escala do asteroide
asteroide=pygame.transform.scale(aster,(52,71))
lua=pygame.transform.scale(lua1,(52,71))
ovo=pygame.transform.scale(ovo1,(52,71))
homem_ferro=pygame.transform.scale(homem_ferro1,(52,71))
fogo=pygame.transform.scale(fogo1,(52,71))
martelo=pygame.transform.scale(martelo1,(52,71))
carro=pygame.transform.scale(carro1,(52,71))
moto=pygame.transform.scale(moto1,(52,71))
lixo=pygame.transform.scale(lixo1,(52,71))
musk=pygame.transform.scale(musk1,(52,71))


# Carregando nave
nav=pygame.image.load("fighter.png")
# diminuindo a escala da nave
nave=pygame.transform.scale(nav,(130,64))
nave=pygame.transform.flip(nave, True, False)

# criando sprites
sprite1=cria_objeto.objeto(asteroide,(500,100))
sprite2=cria_objeto.objeto(nave,(0,250))
sprite3=cria_objeto.objeto(lua,(500, 250))
sprite4=cria_objeto.objeto(ovo,(500, 340))
sprite5=cria_objeto.objeto(fogo,(500, 140))
sprite6=cria_objeto.objeto(martelo,(500, 190))
sprite7=cria_objeto.objeto(carro,(500, 267))
sprite8=cria_objeto.objeto(moto,(500, 234))
sprite9=cria_objeto.objeto(lixo,(500, 197))
sprite10=cria_objeto.objeto(musk,(500, 450))
sprite11=cria_objeto.objeto(homem_ferro,(500, 270))

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

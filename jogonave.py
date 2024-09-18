import pygame # biblioteca pygame
import cria_objeto
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura_tela=500
altura_tela=500
tela=pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Planetas")

# Carregar o efeito sonoro
efeito_sonoro=pygame.mixer.Sound("explode.ogg")

# Carregar a imagem de fundo
imagem_fundo=pygame.image.load("planetas.jpg")
# Carregando asteroide
aster=pygame.image.load("asteroid.png")
# diminuindo a escala do asteroide
asteroide=pygame.transform.scale(aster,(52,71))

# Carregando nave
nav=pygame.image.load("fighter.png")
# diminuindo a escala da nave
nave=pygame.transform.scale(nav,(130,64))
nave=pygame.transform.flip(nave, True, False)

# criando sprites
sprite1=cria_objeto.objeto(asteroide,(500,100))
sprite2=cria_objeto.objeto(nave,(0,250))

# criando grupo de sprites para facilitar a manipulação dos mesmos
grupo_sprites=pygame.sprite.Group(sprite1,sprite2)

# obtendo as dimensões da imagem
largura_imagem_fundo,altura_imagem_fundo=imagem_fundo.get_size()

# Posição inicial da imagem de fundo
posicao_x=0

# valor inicial da variável de temporização
tempo=0

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

    # mudando a posição dos sprites dos asteróides
    sprite1.rect.x-=1

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

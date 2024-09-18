import pygame

class objeto(pygame.sprite.Sprite):
    def __init__(self,imagem,posicao):
        super().__init__()
        # imagem associada ao sprite
        self.image=imagem
        # retângulo de colisão do sprite
        self.rect=self.image.get_rect()
        # posição do sprite (x,y)
        self.rect.topleft=posicao
        # Variável de controle para verificar se o sprite sofreu kill
        self.killed = False
    def mudar_imagem(self,nova_imagem):
        self.image = nova_imagem
        # Atualiza o retângulo de colisão
        self.rect = self.image.get_rect(center=self.rect.center)
    def kill(self):
        super().kill()
        # Atualiza a variável de controle quando o sprite sofre kill
        self.killed=True

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Inicio da declaração de variáveis:

largura = 640
altura = 480
x = largura/2
y = altura/2
x_azul = randint(40, 600)
y_azul = randint(50, 430)
fonte = pygame.font.SysFont("Arial", 40, True, False)
pontos = 0
#Fim da declaração de variáveis.

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Crazy Snake")
relogio = pygame.time.Clock()

while True:
    relogio.tick(100)
    tela.fill((255,255,255))
    mensagem = f"Pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, (255, 215, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 20
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_UP:
                y = y - 20
            if event.key == K_DOWN:
                y = y + 20

    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pygame.key.get_pressed()[K_UP]:
        y = y - 5
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 5
    ret_verde = pygame.draw.rect(tela, (0,255,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_verde.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
    tela.blit(texto_formatado, (420, 40))

    pygame.display.update()

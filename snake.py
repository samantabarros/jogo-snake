#* *************************************************************************************
# Autor: Samanta S. Barros
# Inicio: 01/05/2021
# Ultima alteracao: 20/08/2021
# Nome: Snake
# Funcao: Simular uma parte do funcionamento do famoso jogo da cobrinha usando python
#**************************************************************************************

import pygame
import random

pygame.init()  # necessário para escrever na tela

#azul = (38, 73, 130)

green = (38, 107, 35)
cor_comida = (0, 0, 0)
grey = (220, 220, 220)
cor_cobra = (14, 17, 199)
dimensoes = (600, 600)

# Valores iniciais
x = 300
y = 300
d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20

fonte = pygame.font.SysFont("hack", 30)
#fonte_dois = pygame.font.SysFont("comicsansms", 35)

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption("Snake da Kenzie")

tela.fill(green)  # pinta a tela de azul

clock = pygame.time.Clock()  # relogio - velocidade de atualização da tela

# funcao desenhar_cobra


def desenha_cobra(lista_cobra):
    tela.fill(green)  # limpar atela
    for unidade in lista_cobra:
        # desenha um retangulo  - [x, y, d, d] - define o retangulo
        pygame.draw.rect(tela, cor_cobra, [unidade[0], unidade[1], d, d])

# funcao mover_cobra


def mover_cobra(dx, dy, lista_cobra):

    for event in pygame.event.get():  # verifica as teclas que estão sendo pressionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # tecla esquerda
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:  # tecla direita
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:  # tecla pra cima
                dx = 0
                dy = -d  # eixo x diminue
            elif event.key == pygame.K_DOWN:  # tecla para baixo
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]  # o ultimo quadrado sempre vai para a frente

    return dx, dy, lista_cobra  # retorna a posição

# função verifica comida


def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):

    head = lista_cobra[-1]  # cabeça da cobra é o último elemento da lista

    # nova posição da cobra
    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        # Quando a cabeça da cobra encontra a comida ela aumenta uma unidade para frente
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20

    # desenha o retângulo que representa a comida, na tela
    pygame.draw.rect(tela, cor_comida, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra

# função verifica_parede


def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):

        raise Exception

# função verifica_mordeu_cobra


def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]  # deleta da lista a cabeça
    for x, y in corpo:
        if x == head[0] and y == head[1]:

            raise Exception

# função atualizar_pontos


def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra))
    escore = fonte.render("Pontos: " + pts, True, grey)
    tela.blit(escore, [500, 580])


# def game_over():
#     msg = fonte_dois.render("GAME OVER", True, grey)
#     dis.blit(msg, 0, 0)
#     return msg


while True:
    pygame.display.update()  # atualiza a tela
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(
        dx, dy, x_comida, y_comida, lista_cobra)

    print(lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)

    clock.tick(10)  # taxa de atualização da tela

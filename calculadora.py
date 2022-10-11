import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#variavéis
largura_tela = 640
altura_tela = 480

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Calculadora JOHNY")

fonte01 = pygame.font.SysFont("arialblack", 25)
fonte02 = pygame.font.SysFont('gadugi', 23, True, True)
fonte03 = pygame.font.SysFont('bahnschrift', 27, True, True)
fonte04 = pygame.font.SysFont("bahnschrift", 19)
fonte05 = pygame.font.SysFont("arialblack", 65)
fonte06 = pygame.font.SysFont("arialblack", 35)
corBRANCO = (255, 255, 255)
corPRETO = (0, 0, 0)

som_toque = pygame.mixer.Sound("som_tecla.wav")
                #botao 0            botao 1             botao 2                 botao 3 ...
botoes = [(385, 520, 355, 480), (0, 135, 155, 255), (135, 260, 155, 255), (260, 385, 155, 255), (0, 135, 255, 355), (135, 260, 255, 355), (260, 385, 255, 355), (0, 135, 355, 480), (135, 260, 355, 480), (260, 385, 355, 480)]

result02 = ""

apertou_operador = True
#funções
def gerar_rect(cor, eixoX, eixoY, tamanoX, tamanhoY):
    pygame.draw.rect(tela, cor, (eixoX, eixoY, tamanoX, tamanhoY))

def gerar_texto(texto, fonte, corRGB, posicao_X, posicao_Y):
    texto_ = fonte.render(texto, True, corRGB)
    tela.blit(texto_, (posicao_X, posicao_Y))

def mouse_button(minimoX, maxX, miniY, maxY):  #verifica se o cursos está dentrodo parametros
    if minimoX <= mouse_cursor[0] <= maxX and miniY <= mouse_cursor[1] <= maxY:
        return True
    else:
        return False

#Loop principal
while True:
    tela.fill((80, 80, 80))
    mouse_cursor = pygame.mouse.get_pos()

    #botao - ABRIR CALCULADORA
    if mouse_button(200, 445, 150, 190) == True:
        gerar_rect(corBRANCO,200, 150, 245, 40)
        gerar_texto("Abrir Calculadora", fonte01, corPRETO, 205, 150)
    else:
        gerar_rect(corPRETO, 200, 150, 245, 40)
        gerar_texto("Abrir Calculadora", fonte01, corBRANCO, 205, 150)

    #botao - CRÉDITOS
    if mouse_button(200, 445, 220, 260) == True:
        gerar_rect(corBRANCO, 200, 220, 245, 40)
        gerar_texto("Créditos", fonte01, corPRETO, 265, 220)
    else:
        gerar_rect(corPRETO, 200, 220, 245, 40)
        gerar_texto("Créditos", fonte01, corBRANCO, 265, 220)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            #CASO ABRA CALCULADORA
            if mouse_button(200, 445, 150, 190) == True:
                som_toque.play()
                while True:
                    parar = False
                    tela.fill((49,49,49))

                    mouse_cursor = pygame.mouse.get_pos()
                    #BOTAO DE VOLTAR
                    if mouse_button(10, 45, 10, 35) == True:
                        gerar_rect((105,105,105), 10, 10, 35, 25)
                        gerar_texto("<--", fonte04, corBRANCO, 10, 10)
                    else:
                        gerar_rect((70,70,70), 10, 10, 35, 25)
                        gerar_texto("<--", fonte04, corBRANCO, 10, 10)
                                #LINHAS, CORES E NUMEROS//LETRAS
                    gerar_rect((29,29,29), 0, 155, 385, 325) #rect 1 ao 9
                    gerar_rect((29, 29, 29), 385, 355, 137, 125) #rect do zero
                    gerar_rect((21, 67, 18), 385, 255, 137, 100) #verde
                    gerar_rect((140, 56, 16), 385, 155, 137, 100) #laranja
                    gerar_rect((96, 16, 140), 520, 155, 120, 325) #roxo
                    gerar_texto("  1    2    3", fonte05, corBRANCO, 0, 155) #do 1 a0 3
                    gerar_texto("  4    5    6", fonte05, corBRANCO, 0, 255)  # do 4 a0 6
                    gerar_texto("  7    8    9    0", fonte05, corBRANCO, 0, 365)  # do 7 a0 9 e 0
                    gerar_texto("  =", fonte05, corBRANCO, 385, 255) #simb ====
                    gerar_texto("  C   <-", fonte06, corBRANCO, 385, 179) #del C && del <-
                    gerar_texto("    +", fonte06, corBRANCO, 520, 169)
                    gerar_texto("    -", fonte06, corBRANCO, 525, 249)
                    gerar_texto("    /", fonte06, corBRANCO, 525, 329)
                    gerar_texto("    *", fonte06, corBRANCO, 525, 409)

                    #LINHAS DE DIVISÓRIA
                    pygame.draw.lines(tela, corPRETO, False, [(0, 155), (640, 155), (640, 480), (0, 480), (0, 155), (0, 255), (520, 255), (520, 355), (0, 355)], 3)
                    pygame.draw.lines(tela, corPRETO, False, [(135, 480), (135, 155), (260, 155), (260, 480), (385, 480), (385, 155), (520, 155), (520, 480)], 3)
                    pygame.draw.lines(tela, corPRETO, False, [(452, 255), (452, 155), (520, 155), (520, 235), (640, 235), (640, 315), (520, 315), (520, 395), (640, 395)], 3)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == MOUSEBUTTONDOWN:
                            if mouse_button(10, 45, 10, 35) == True: #VERIFICA BOTAO  VOLTARR!!!!
                                som_toque.play()
                                parar = True
                            for c in range(0, 10): #verifica os botoes apertados de 0 a 9
                                if mouse_button(*botoes[c]) == True:  # 0)

                                    result02 += f"{c}"
                                    apertou_operador = True
                                    som_toque.play()

                                #aritimeticos
                            if mouse_button(385, 520, 255, 355) == True: #======
                                calculo = eval(result02)
                                result02 = str(calculo)
                                som_toque.play()
                            if mouse_button(385, 452, 155, 255) == True: #CCC
                                result02 = ''
                                som_toque.play()
                                apertou_operador == True
                            if mouse_button(452, 520, 155, 255) == True: #<-
                                result02 = result02[:-1]
                                som_toque.play()
                                apertou_operador = True

                            if apertou_operador == True:
                                if  mouse_button(520, 640, 155, 235) == True: #+++
                                    result02 += "+"
                                    som_toque.play()
                                    apertou_operador = False

                                if mouse_button(520, 640, 235, 315) == True: #----
                                    result02 += "-"
                                    som_toque.play()
                                    apertou_operador = False

                                if mouse_button(520, 640, 315, 395) == True: #/////
                                    result02 += "/"
                                    som_toque.play()
                                    apertou_operador = False

                                if mouse_button(520, 640, 395, 480) == True: #***
                                    result02 += "*"
                                    som_toque.play()
                                    apertou_operador = False

                    #exibiçao
                    gerar_texto(f"{result02}", fonte06, corBRANCO, 20, 72)

                    if parar == True:
                        break
                    pygame.display.update()


            #CASO ABRA OS CRÉDITOS
            if mouse_button(200, 445, 220, 260) == True:
                som_toque.play()
                while True:
                    parar = False
                    tela.fill((49,49,49))#tela cinza
                    gerar_rect((80,80,80),20,20,600, 440)

                    #textos
                    gerar_texto("Criador - Johny B. Santos", fonte03, corBRANCO, 30, 40)
                    gerar_texto("Data de Criação - 07/10/2022 ", fonte03, corBRANCO, 30, 80)
                    gerar_texto("GitHub - Johny-007", fonte03, corBRANCO, 30, 120)
                    gerar_texto("Linkdln - Johny Barbosa Santos", fonte03, corBRANCO, 30, 160)
                    gerar_texto("Versão - 0.1", fonte03, corBRANCO, 30, 200)

                    mouse_cursor = pygame.mouse.get_pos()
                    if mouse_button(200, 445, 400, 440) == True:
                        gerar_rect(corBRANCO, 200, 400, 245, 40)
                        gerar_texto("Voltar", fonte01, corPRETO, 280, 400)
                    else:
                        gerar_rect(corPRETO, 200, 400, 245, 40)
                        gerar_texto("Voltar", fonte01, corBRANCO, 280, 400)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == MOUSEBUTTONDOWN:
                            if mouse_button(200, 445, 400, 440) == True:
                                som_toque.play()
                                parar = True
                    if parar == True:
                        break
                    pygame.display.update()

    pygame.display.flip()
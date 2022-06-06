# Importa a bibiioteca que irá rodar o jogo:
import pygame

# Classe com as funções que irão setar os parâmetros da tela:
class Tela(object):

    def fecharJogo(self):
        pygame.quit()

    def iniciaJogo(self):
        pygame.init()
        self.posicaoErrada = []

    def criarTela(self):
        self.janela = pygame.display.set_mode((800, 600))
        pygame.mouse.set_visible(1)

    def setImagem(self, nomeTela, x, y):
        tela = pygame.image.load(nomeTela)
        self.janela.blit(tela, (x, y))

    def pintarTela(self, cor):
        self.janela.fill(cor)

    def desenharBotao(self, cor, left, top, width, height, posicaoCorreta):
        if posicaoCorreta:
            self.button = pygame.Rect(left, top, width, height)
            pygame.draw.rect(self.janela, cor, self.button)
        else:
            self.posicaoErrada.append(pygame.Rect(left, top, width, height))
            pygame.draw.rect(self.janela, cor, self.posicaoErrada[-1])

    def criarTexto(self, fonte, tamanho, texto, verdadeiro, cor, x, y):
        myfont = pygame.font.SysFont(fonte, tamanho)
        nlabelComeco = myfont.render(texto, verdadeiro, cor)
        self.janela.blit(nlabelComeco, (x, y))

    def atualizarTela(self):
        pygame.display.flip()
        pygame.display.update()


    def escutaEvento(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.button.collidepoint(pos):
                        return True
                    elif len(self.posicaoErrada) > 0:
                        if self.posicaoErrada[0].collidepoint(pos):
                            return False
                        elif self.posicaoErrada[1].collidepoint(pos):
                            return False
                        elif self.posicaoErrada[2].collidepoint(pos):
                            return False
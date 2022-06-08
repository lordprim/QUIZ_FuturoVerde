# Importa informações da classe contida no documento Tela:
from PCA_QUIZ_UTIL.Tela import Tela

# Importa a função de random usada no embaralhamento das posições de respostas:
import random

# Classe do jogo:
class Jogo(object):
    numeroPergunta = -1
    # Perguntas e respostas listadas em um vetor:
    # Resposta certa é sempre o primeiro valor da lista:
    questoes = [
        ["O que é TI Verde?",
         ["Movimento para redução no impacto ambiental", "Hardware sustentáveis", "Movimento para redução de custos para empresas", "Troca de funcionários dentro da empresa"]],
        ["Qual a norma do relacionada ao TI Verde?",
         ["ISO 14001", "ISO 9001", "ISO 14000", "ISO 27001"]],
        ["Modelo de trabalho considerado uma medida sustentável?",
         ["Trabalho remoto", "Escalas temporárias de trabalho", "Alteração no quadro de funcionários na empresa", "Todos os funcionários locais"]],
        ["Qual seria a boa prática em relação a TI Verde?",
         ["Redução de Custos com a energia", "Acrescento de servidores locais", "Compra de novos computadores e periféricos", "Alteração no número de impressoras"]],
        ["O que não é uma implementação do TI Verde?",
         ["Migrar serviços para Data Centers Locais", "Investir em sistemas de refrigeração", "Preferir aplicativos mais eficientes", "Investir em energia limpa"]],
        ["O que é Deep it?",
         ["Melhorar o desempenho sem que haja desperdício de energia", "Um termo para troca de equipamentos antigos por novos", "Um sistema que busca emular", "Atualização do Sistema Operacional, para uma melhor performance"]],
        ["Qual das opções não é considerada Tecnologia Verde?",
         ["Todas são considerados tecnologias verdes", "Carros Elétricos e Hibridos", "Bioinseticidas", "Arquitetura Sustentável"]],
        ["Quais vantagens de adotar a TI verde na empresa?",
         ["Diminui custos da empresa/maior desempenho de seus funcionários.", "Diminui a produtividade de cada funcionario da empresa.", "Nenhuma das alternativas anteriores.", "Arquitetura Sustentável"]],
        ["Qual das informações a seguir não é uma prática de TI verde?",
         ["Uso de folhas de papel.", "Usar lâmpadas fluorescentes.", "Desligar os equipamentos quando não estão sendo usados.", "Monitorar automaticamente a energia disponível nas máquinas."]],
        ["Qual das informações a seguir é uma boa prática para discarte de eletrônicos?",
         ["Repasse/doação.", "Descarte na lixeira de lixo.", "Abandono em um ambiente público.", "Colocar junto de outros reciclaveis orgânicos."]],
    ]
    # Variável de pontos:
    pontucao = -1
    # Variável de erros:
    erros = 0

    # Função para inicialização da tela do jogo:
    def iniciarJogo(self):
        self.tela = Tela()
        self.tela.iniciaJogo()
        self.tela.criarTela()

    # Função para setar imagem/botão/texto na tela de inicio do jogo:
    def criarTelaInicio(self):
        # Apresentação da imagem na tela de inico, junto dos valores do eixo X e Y que define a posição da imagem:
        self.tela.setImagem("quiz_image.jpg", -75, -55)
        # Definições de cores usadas dentro da função:
        corAmarela = (255, 182, 4)
        corPreta = (0, 0, 0)
        # Criação do botão na tela:
        self.tela.desenharBotao(corAmarela, 330, 525, 150, 45, True)
        # Criação do texto na tela:
        self.tela.criarTexto("arial", 40, "Começar", 1, corPreta, 340, 525)

    # Função para apresentar as perguntas na tela:
    def criarTelaPergunta(self):
        # Criação dos botões na tela:
        posicaoBotoes = [165, 265, 365, 465]
        # Ferramenta para criar as respostar de forma random:
        random.shuffle(posicaoBotoes)
        corBranco = (255, 255, 255)
        corAmarela = (255, 182, 4)
        corPreta = (0, 0, 0)
        # Ferramenta para pintar o fundo da tela de branco:
        self.tela.pintarTela(corBranco)
        self.tela.criarTexto("arial", 35, self.questoes[self.numeroPergunta][0], 1, corPreta, 35, 70)
        self.tela.criarTexto("arial", 20, ("Pontos: " + str(self.pontucao)), 1, corPreta, 700, 10)
        self.tela.criarTexto("arial", 20, ("Erros: " + str(self.erros)), 1, corPreta, 700, 30)
        # Função para gerar as perguntas de forma aleatório e as repostas de forma randomica, não permitindo que a resposta fique na mesma posição:
        for i in range(4):
            self.tela.desenharBotao(corAmarela, 10, posicaoBotoes[i], 780, 35, i == 0)
            self.tela.criarTexto("arial", 30, self.questoes[self.numeroPergunta][1][i], 1, corPreta, 12, posicaoBotoes[i])

    # Função para a criação da tela de fim de jogo no caso de vitória:
    def criarTelaFinalWin(self):
        corBranco = (255, 255, 255)
        corPreta = (0, 0, 0)
        corAzul = (72,209,204)
        self.tela.setImagem("TelaFinal.png", 0, 0)
        self.tela.desenharBotao(corAzul, 260, 525, 270, 50, True)
        self.tela.criarTexto("arial", 40, "Jogar novamente", 1, corBranco, 268, 525)
        self.tela.criarTexto("arial", 40, "Parabéns, você venceu!!!", 1, corPreta, 215, 470)

    def criarTelaFinalLose(self):
        corBranco = (255, 255, 255)
        corPreta = (0, 0, 0)
        corAzul = (72,209,204)
        self.tela.setImagem("TelaFinal.png", 0, 0)
        self.tela.desenharBotao(corAzul, 260, 525, 270, 50, True)
        self.tela.criarTexto("arial", 40, "Jogar novamente", 1, corBranco, 268, 525)
        self.tela.criarTexto("arial", 40, "Você perdeu!!!", 1, corPreta, 290, 470)

# Inicio do jogo:
jogo = Jogo()
jogo.iniciarJogo()
jogo.criarTelaInicio()

# Laço de repetição utilizado durante o jogo:
while True:
    # Função para atualização das informações na tela:
    jogo.tela.atualizarTela()
    # Função que permite pegar a posição/colisão/clique do mouse:
    if jogo.tela.escutaEvento():
        # Função utilizada para encontrar o fim do jogo, não permitindo haver mais perguntas:
        if jogo.numeroPergunta >= len(jogo.questoes) -1:
            # Soma da pontuação:
            jogo.pontucao += 1
            # Atualização da pergunta na tela quando selecionada a resposta certa:
            jogo.criarTelaPergunta()
            # Função para conta de repostas certas, podendo assim apresentar a tela de vitória.
            if jogo.pontucao == 10:
                jogo.criarTelaFinalWin()
                jogo.numeroPergunta = -1
                jogo.pontucao = -1
                jogo.erros = -1
        else:
            # Funções caso a resposta seja certa troque a pergunta:
            jogo.numeroPergunta += 1
            jogo.pontucao += 1
            jogo.criarTelaPergunta()
    # Contabilização de respostas erradas, podendo assim gerar a tela de fim de jogo caso seja respondido 5 perguntas erradas:
    elif jogo.erros == 5:
        jogo.criarTelaFinalLose()
        jogo.numeroPergunta = -1
        jogo.pontucao = -1
        jogo.erros = 0

    else:
        # Função caso a resposta selecionada seja a errada.
        jogo.erros += 1
        jogo.criarTelaPergunta()


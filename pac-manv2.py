"""
    IMPORTANDO AS BLIBLIOTECA 
    
"""

import random
import math
from colorama import Fore

"""
## PAC MAN
## REGRAS DO JOGO 

* Fugir dos fanstamas que estão sempre perseguindo o personagem
* Se uns dos fantasma conseguir capturar o Pac Man o jogo acaba (Game Over)
* Depois de algumas rodadas o item sagrado irá surgir em um ponto especifico do mapa
* Se o jogador conseguir capturar o item sagrado, o jogo vai para a proxima fase
* Sempre que o jogador passa de fase a dificuldade do jogo aumenta
* Divita-se !

## Integrates do grupo

* Aylton Silva Torres
* Charles Alberto Tomaz
* Eduardo Alcântara de Souza
* Julio Cesar Viana da Silva 
* Wesley Pinheiros  

"""

def print_logo():# Definindo a função para imprimir o logo do jogo
    # Definindo a variável 'logo' com o logo do jogo em formato de string de várias linhas    
    logo = """
         ______     ________    ________         ____   ____    ________    ___      __
        |   __  |  |   __   |  |    ____|       |    \\_/    |  |   __   |  |   \\    /  |
        |  |__| |  |  |__|  |  |   |            |   _   _   |  |  |__|  |  |    \\__/   |
        |    ___|  |   __   |  |   |            |  | | | |  |  |   __   |  |           |
        |  |       |  |  |  |  |   |____        |  | |_| |  |  |  |  |  |  |  |\\       |
        |__|       |__|  |__|  |________|       |__|     |__|  |__|  |__|  |__| \\______|
    """
    # Imprimindo o logo com a cor amarela usando Fore.YELLOW do Colorama
    print(Fore.YELLOW + logo)
    print("PAC-MAN") # Imprimindo o nome do jogo

def iniciar_jogo(): # Definindo a função para iniciar o jogo
    print("Iniciar game") # Imprimindo uma mensagem indicando o início do jogo
    input("Pressione Enter para iniciar o jogo...") # Esperando o jogador pressionar Enter para começar
    print(Fore.LIGHTGREEN_EX + " ") # Imprimindo uma linha vazia com cor verde clara

"""
CONTRUINDO AS REGRAS DO JOGO 

"""

# Função para calcular a distância entre duas posições
def distancia(pos1, pos2):
    # Calcula a distância 
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Imputs do personagem principal
def mover_pacman(labirinto, direcao):
    nova_posicao = pacman[:] # Cria uma cópia da posição atual do Pac-Man
    
    # Move o Pac-Man na direção especificada pelo jogador
    if direcao == 'w':  # Mover para cima
        nova_posicao[0] -= 1
    elif direcao == 's':  # Mover para baixo
        nova_posicao[0] += 1
    elif direcao == 'a':  # Mover para esquerda
        nova_posicao[1] -= 1
    elif direcao == 'd':  # Mover para direita
        nova_posicao[1] += 1
    
    # Verificar se a nova posição é válida
    if (0 <= nova_posicao[0] < len(labirinto)) and (0 <= nova_posicao[1] < len(labirinto[0])) and (labirinto[nova_posicao[0]][nova_posicao[1]] == 1):
        return nova_posicao # Retorna a nova posição se for válida
    else:
        return pacman  # Se a nova posição não for válida, permanece na posição atual


# Função para verificar a colisão do Pac-Man com o item "i"
def verificar_colisao_com_item(labirinto):
    global pacman
    if pacman == item:
        return True
    return False

# Função para capturar a entrada do jogador
def capturar_entrada():
    direcao = input(Fore.YELLOW + "Digite a direção para mover o PAC-MAN (w para cima, s para baixo, a para esquerda, d para direita): ")
    return direcao

# Funções para mover o fantasma na direção do PAC-MAN
def mover_fantasma(posicao, alvo, labirinto):
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direções: direita, esquerda, baixo, cima
    melhor_direcao = None
    menor_distancia = float('inf')

    for direcao in direcoes:
        nova_posicao = [posicao[0] + direcao[0], posicao[1] + direcao[1]]
        if 0 <= nova_posicao[0] < len(labirinto) and 0 <= nova_posicao[1] < len(labirinto[0]):
            if labirinto[nova_posicao[0]][nova_posicao[1]] == 1:
                dist = distancia(nova_posicao, alvo)
                if dist < menor_distancia:
                    menor_distancia = dist
                    melhor_direcao = direcao

    if melhor_direcao and random.random() < 0.83:  # Escolha entre ir na direção do pacman e direção aleatória
        nova_posicao = [posicao[0] + melhor_direcao[0], posicao[1] + melhor_direcao[1]]
        if labirinto[nova_posicao[0]][nova_posicao[1]] == 1:  # Verificar se a nova posição é válida
            return nova_posicao
        else:
            return posicao  # Se a nova posição não for válida, permanece na posição atual
    else:
        # Fica parado
        return posicao

class Agente:
    def __init__(self, nome="Fantasma Verde"):
        # Inicialização do agente com seu estado e nome
        self.state = "parado"
        self.nome = nome # Nome do agente

    def update_state(self, nova_posicao, posicao_anterior, posicao_pacman):
        # Atualiza o estado do agente com base na nova posição, posição anterior e posição do PAC-MAN
        if nova_posicao == posicao_anterior:
            # Quando o fantasma permanece na mesma posição que anteriormente
            self.state = "parado"
        elif nova_posicao == posicao_pacman:
            # Quando o fantasma fica na mesma posição do PAC-MAN
            self.state = "ataque"
        else:
            # Quando o fantasma muda para uma posição próxima à do PAC-MAN
            self.state = "seguir"

    def perform_action(self):
        # Executa a ação com base no estado atual do agente
        if self.state == "parado":
            # Se o agente estiver parado, imprime uma mensagem indicando isso
            print(Fore.GREEN +self.nome,": Estou parado.")
        elif self.state == "seguir":
            # Se o agente estiver seguindo o jogador, imprime uma mensagem indicando isso
            print(Fore.GREEN + self.nome,": Estou seguindo o jogador.")
        elif self.state == "ataque":
            # Se o agente estiver em modo de ataque, imprime uma mensagem indicando isso
            print(Fore.GREEN + self.nome,": Capturei o jogador.")

class Agente2:
    def __init__(self, nome="Fantasma Vermelho"):
        # Inicialização do agente com seu estado e nome
        self.state = "parado" # Estado inicial do agente
        self.nome = nome # Nome do agente

    def update_state(self, nova_posicao, posicao_anterior, posicao_pacman):
        if nova_posicao == posicao_anterior:
            # Quando o fantasma permanece na mesma posição que anteriormente
            self.state = "parado"
        elif nova_posicao == posicao_pacman:
            # Quando o fantasma fica na mesma posição do PAC-MAN
            self.state = "ataque"
        else:
            # Quando o fantasma muda para uma posição próxima à do PAC-MAN
            self.state = "seguir"

    def perform_action(self):
        if self.state == "parado":
            print(Fore.RED + self.nome,": Estou parado.")
            print (" ")

        elif self.state == "seguir":
            print(Fore.RED + self.nome,": Estou seguindo o jogador.")
            print (" ")

        elif self.state == "ataque":
            print(Fore.RED + self.nome, ": Capturei o jogador.")
            print (" ")

# Função para imprimir o labirinto com o PAC-MAN e os fantasmas
def imprimir_labirinto(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if [i, j] == pacman:
                print(Fore.YELLOW+"P", end=" ") # Imprime o PAC-MAN em amarelo
            elif [i, j] == fantasma1:
                print(Fore.GREEN+"F", end=" ") # Imprime o Fantasma Verde em verde
            elif [i, j] == fantasma2:
                print(Fore.RED +"F", end=" ") # Imprime o Fantasma Vermelho em vermelho
            elif [i, j] == item:  # Verificar se a posição é a do item "i"
                print(Fore.LIGHTMAGENTA_EX + "i", end=" ")  # Usar a cor lilás para o item "i"
            elif labirinto[i][j] == 0:
                print(Fore.WHITE+"#", end=" ") # Imprime paredes em branco
            else:
                print(Fore.WHITE+".", end=" ") # Imprime caminhos em branco
        print()

# Variável para controlar a rodada inicial para a próxima partida
rodada_inicial = 6 # Define a rodada inicial para a próxima partida como 6

"""
CONTRUINDO A LOGICA DO JOGO

"""

while True:
    print_logo()
    iniciar_jogo()

    # Definição do labirinto (representado por uma matriz)
    labirinto = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Posições iniciais do PAC-MAN e dos fantasmas
    pacman = [4, 5]
    fantasma1 = [1, 1]
    fantasma2 = [1, 9]

    # Variáveis para controle
    rodadas = 0 # Contador de rodadas
    item = None # Posição do item especial no labirinto (inicialmente nulo)
    vitoria = False # Flag para indicar se o jogador venceu

    agente1 = Agente() # Agente 1 (fantasma verde)
    agente2 = Agente2() # Agente 2 (fantasma vermelho)

    # Loop principal do jogo
    while pacman != [-1, -1]: # Enquanto o Pac-Man não for capturado

        # Imprimir o mapa atualizado
        print(Fore.BLUE + "Mapa: ")
        imprimir_labirinto(labirinto)
        print()

        # Armazenar as posições anteriores dos fantasmas
        posicao_anterior_fantasma1 = fantasma1[:]
        posicao_anterior_fantasma2 = fantasma2[:]

        # Mover o fantasma 1 na direção do Pac-Man e atualizar seu estado
        fantasma1 = mover_fantasma(fantasma1, pacman, labirinto)
        agente1.update_state(fantasma1, posicao_anterior_fantasma1, pacman)

        # Verificar se o fantasma 1 capturou o Pac-Man
        if fantasma1 == pacman:
            pacman = [-1, -1] # Definir a posição do Pac-Man como fora do labirinto

        # Mover o fantasma 2 na direção do Pac-Man e atualizar seu estado
        fantasma2 = mover_fantasma(fantasma2, pacman, labirinto)
        agente2.update_state(fantasma2, posicao_anterior_fantasma2, pacman)

        # Verificar se o fantasma 2 capturou o Pac-Man
        if fantasma2 == pacman:
            pacman = [-1, -1] # Definir a posição do Pac-Man como fora do labirinto

        # Capturar a entrada do jogador (movimento do Pac-Man)
        direcao = capturar_entrada()

        # Mover o Pac-Man na direção especificada e atualizar o mapa
        pacman = mover_pacman(labirinto, direcao)

        # Realizar ações dos agentes (fantasmas)
        agente1.perform_action()
        agente2.perform_action()

        # Incrementar o contador de rodadas
        rodadas += 1
        
        # Verifica se a rodada atual está dentro da progressão
        if rodadas == rodada_inicial and item is None:
            # Gerar posição aleatória para o item até que esteja em uma posição válida
            while True:
                item_row = random.randint(0, len(labirinto) - 1)
                item_col = random.randint(0, len(labirinto[0]) - 1)
                # Verificar se a posição gerada não é uma parede, posição do jogador ou dos fantasmas
                if labirinto[item_row][item_col] == 1 and [item_row, item_col] != pacman and [item_row, item_col] != fantasma1 and [item_row, item_col] != fantasma2:
                    item = [item_row, item_col]
                    break

        # Verificar colisão com o item "i"
        if verificar_colisao_com_item(labirinto):
            vitoria = True
            break

    # Verificar o resultado do jogo
    if vitoria:
        print(Fore.LIGHTCYAN_EX + "Parabéns! Você encontrou o item 'i'. Você venceu o jogo!")
        print(" ")
        # Atualiza a rodada inicial para a próxima partida
        rodada_inicial += 1
    else:
        print(Fore.LIGHTGREEN_EX + "PAC-MAN CAPTURADO!")
        print(" ")
        print(Fore.WHITE + "Obrigado por jogar !")
        print(" ")
        break

    # Perguntar ao jogador se ele deseja jogar novamente
    jogar_novamente = input(Fore.WHITE + "Gostaria de jogar novamente em uma dificuldade maior ? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        break
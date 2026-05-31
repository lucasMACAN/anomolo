# CHAMEI A BIBLIOTECA DE FUNÇÕES ESPECÍFICAS DO JOGO
import Funcoes_jogo

# CLASSE PERSONAGEM, CRIAÇÃO DE PERSONAGEM
# E INTERAÇÃO COM O CENÁRIO
class PERSONAGEM:
    def __init__(self, nome):
        self.nome = nome
        self.sanidade = 100
        self.escolha = 0

    # FUNÇÃO DECISAO_QUARTO(): FUNÇÃO USADA PARA DECIDIR O QUE
    # O USUÁRIO VAI FAZER QUANDO ESTIVER DENTRO DO QUARTO
    def DECISAO_QUARTO(self):
        Funcoes_jogo.LIMPAR()
        print("Você acorda em um quarto desconhecido.")
        input("aperte ENTER para continuar")
        Funcoes_jogo.LIMPAR()

        print("-------------MENU-------------")
        print("(1) ir para o CORREDOR")
        print("(2) olhar o ESPELHO\n")
        self.escolha = int(input("> "))
        Funcoes_jogo.LIMPAR()   # PARA GARANTIR A LIMPEZA DO TERMINAL (NECESSÁRIO)

        if self.escolha == 2:
                Funcoes_jogo.ESPELHO()
                self.escolha = 0

    # FUNÇÃO DECISAO_CORREDOR(): FUNÇÃO USADA PARA DECIDIR O QUE
    # O USUÁRIO VAI FAZER QUANDO ESTIVER NO CORREDOR 
    def DECISAO_CORREDOR(self):
        Funcoes_jogo.LIMPAR()
        print("Um corredor longo e silencioso.")
        input("aperte ENTER para continuar")
        Funcoes_jogo.LIMPAR()

        print("-------------MENU-------------")
        print("(1) voltar ao QUARTO")
        print("(2) ir para a COZINHA\n")
        self.escolha = int(input("> "))
        Funcoes_jogo.LIMPAR()   # PARA GARANTIR A LIMPEZA DO TERMINAL (NECESSÁRIO)

        if self.escolha == 1:
            self.DECISAO_QUARTO()
            
        elif self.escolha == 2:
            self.DECISAO_COZINHA()
    
    # FUNÇÃO DECISAO_COZINHA(): FUNÇÃO USADA PARA DECIDIR O QUE
    # O USUÁRIO VAI FAZER QUANDO ESTIVER DENTRO DA COZINHA
    def DECISAO_COZINHA(self):
        Funcoes_jogo.LIMPAR()
        print("A cozinha está vazia.")
        input("aperte ENTER para continuar")
        Funcoes_jogo.LIMPAR()

        print("-------------MENU-------------")
        print("(1) voltar ao CORREDOR")
        print("(2) abrir a GELADEIRA\n")
        self.escolha = int(input("> "))
        Funcoes_jogo.LIMPAR()   # PARA GARANTIR A LIMPEZA DO TERMINAL (NECESSÁRIO)

        if self.escolha == 1:
            self.DECISAO_CORREDOR()

        elif self.escolha == 2:
            print("Há apenas um bilhete, está escrito: Você já esteve aqui antes.")
            input("aperte ENTER para continuar")

# DECISAO() O MÉTODO RESPONSÁVEL POR CHAMAR AS FUNÇÕES PRINCIPAIS
    def DECISAO(self):
        # LIMPANDO O TERMINAL POR CONTA DAS INFO QUE APARECE
        # QUANDO ELE É INICIADO
        Funcoes_jogo.LIMPAR()

        if self.escolha == 0:   # COLOQUEI ZERO APENAS PARA A FUNÇÃO "ENTENDER" QUE É UM CENÁRIO DIFERENTE
            self.DECISAO_QUARTO()

        elif self.escolha == 1:
            self.DECISAO_CORREDOR()

        elif self.escolha == 2:
            self.DECISAO_COZINHA()

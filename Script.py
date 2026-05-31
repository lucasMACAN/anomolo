# CHAMEI A BIBLIOTECA DE FUNÇÕES ESPECÍFICAS DO JOGO
import Funcoes_jogo

# CLASSE PERSONAGEM, CRIAÇÃO DE PERSONAGEM
# E INTERAÇÃO COM O CENÁRIO
class PERSONAGEM:
    def __init__(self, nome):
        self.nome = nome
        self.sanidade = 100
        self.escolha = 0
        self.jogando = True
    
    def SAIR(self):
        self.jogando = False    

    def DECISAO_CONFIG(self):
        Funcoes_jogo.LIMPAR()
        print("-------------MENU-------------")
        print("(1) voltar ao jogo")
        print("(2) SALVAR o jogo")
        print("(3) SAIR do jogo")
        self.escolha = int(input("> "))
        

    # FUNÇÃO DECISAO_QUARTO(): FUNÇÃO USADA PARA DECIDIR O QUE
    # O USUÁRIO VAI FAZER QUANDO ESTIVER DENTRO DO QUARTO
    def DECISAO_QUARTO(self):
        Funcoes_jogo.LIMPAR()
        print("Você acorda em um quarto desconhecido.")
        input("aperte ENTER para continuar")
        Funcoes_jogo.LIMPAR()

        print("-------------MENU-------------")
        print("(1) ir para o CORREDOR")
        print("(2) olhar o ESPELHO")
        print("(0) CONFIGURAÇÃO\n")
        self.escolha = int(input("> "))
        Funcoes_jogo.LIMPAR()   # PARA GARANTIR A LIMPEZA DO TERMINAL (NECESSÁRIO)

        if self.escolha == 1:
            self.DECISAO_CORREDOR()

        if self.escolha == 2:
                Funcoes_jogo.ESPELHO()
                self.escolha = 0

        # SE A ESCOLHA FOR 0, ELE VAI ABRIR AS CONFIGURAÇÕES 
        elif self.escolha == 0:
            self.DECISAO_CONFIG()

            # CASO A ESCOLHA SEJA "(0) voltar ao jogo" O JOGO DEFINIRÁ
            # QUE O "self.escolha" SE TORNE "0" QUE FORA DESSE MÉTODO
            # O QUARTO É O 0
            if self.escolha == 1:
                self.escolha = 0
            
            elif self.escolha == 2:
                self.escolha = 0
                Funcoes_jogo.SALVAR(self) # CHAMEI A FUNÇÃO DE SALVAR QUE CRIEI DENTRO DE Funcoes_jogo.py
            
            elif self.escolha == 3: # PARA SAIR DO JOGO
                self.escolha = 10

    # FUNÇÃO DECISAO_CORREDOR(): FUNÇÃO USADA PARA DECIDIR O QUE
    # O USUÁRIO VAI FAZER QUANDO ESTIVER NO CORREDOR 
    def DECISAO_CORREDOR(self):
        Funcoes_jogo.LIMPAR()
        print("Um corredor longo e silencioso.")
        input("aperte ENTER para continuar")
        Funcoes_jogo.LIMPAR()

        print("-------------MENU-------------")
        print("(1) voltar ao QUARTO")
        print("(2) ir para a COZINHA")
        print("(0) CONFIGURAÇÃO\n")
        self.escolha = int(input("> "))
        Funcoes_jogo.LIMPAR()   # PARA GARANTIR A LIMPEZA DO TERMINAL (NECESSÁRIO)

        if self.escolha == 1:
            self.DECISAO_QUARTO()
            
        elif self.escolha == 2:
            self.DECISAO_COZINHA()

        # SE A ESCOLHA FOR 0, ELE VAI ABRIR AS CONFIGURAÇÕES 
        elif self.escolha == 0:
            self.DECISAO_CONFIG()

            # CASO A ESCOLHA SEJA "(1) voltar ao jogo" O JOGO DEFINIRÁ
            # QUE O "self.escolha" SE TORNE "1" QUE É O CORREDOR

            if self.escolha == 2:
                self.escolha = 1
                Funcoes_jogo.SALVAR(self) # CHAMEI A FUNÇÃO DE SALVAR QUE CRIEI DENTRO DE Funcoes_jogo.py
            
            elif self.escolha == 3: # PARA SAIR DO JOGO
                self.escolha = 10
    
    # FUNÇÃO DECISAO_COZINHA(): FUNÇÃO USADA PARA DECIDIR O QUE
    # O USUÁRIO VAI FAZER QUANDO ESTIVER DENTRO DA COZINHA
    def DECISAO_COZINHA(self):
        Funcoes_jogo.LIMPAR()
        print("A cozinha está vazia.")
        input("aperte ENTER para continuar")
        Funcoes_jogo.LIMPAR()

        print("-------------MENU-------------")
        print("(1) voltar ao CORREDOR")
        print("(2) abrir a GELADEIRA")
        print("(0) CONFIGURAÇÃO\n")
        self.escolha = int(input("> "))
        Funcoes_jogo.LIMPAR()   # PARA GARANTIR A LIMPEZA DO TERMINAL (NECESSÁRIO)

        if self.escolha == 1:
            self.DECISAO_CORREDOR()

        elif self.escolha == 2:
            print("Há apenas um bilhete, está escrito: Você já esteve aqui antes.")
            input("aperte ENTER para continuar")
            self.DECISAO_COZINHA()
        
        # SE A ESCOLHA FOR 0, ELE VAI ABRIR AS CONFIGURAÇÕES 
        elif self.escolha == 0:
            self.DECISAO_CONFIG()

            # CASO A ESCOLHA SEJA "(1) voltar ao jogo" O JOGO DEFINIRÁ
            # QUE O "self.escolha" SE TORNE "2" QUE É A COZINHA
            if self.escolha == 1:
                self.escolha = 2
            
            elif self.escolha == 2:
                Funcoes_jogo.SALVAR(self) # CHAMEI A FUNÇÃO DE SALVAR QUE CRIEI DENTRO DE Funcoes_jogo.py
                self.DECISAO_COZINHA()
            
            elif self.escolha == 3: # PARA SAIR DO JOGO
                self.escolha = 10

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
        
        elif self.escolha == 3:
            self.DECISAO_CONFIG()

        elif self.escolha == 10:
            self.SAIR()           

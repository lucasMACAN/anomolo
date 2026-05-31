# CHAMEI A FUNÇÃO RUN() DA BIBLIOTECA "SUBPROCESS"
# SUBSTITUTO DO "OS.SYSTEM"
from subprocess import run

# IMPORTANDO A BIBLIOTECA "JSON"
import json

# CRIEI A VARIÁVEL FORA PARA QUE O SALVAR()
# E O CARREGAR() POSSA PEGAR O VALOR
arquivo_salvo = "SAVE.json"

# REDUZI A FUNÇÃO PARA FICAR MAIS LIMPO E PRÁTICO
def LIMPAR():
    run('cls', shell = True) # PEDE PARA LIMPAR O TERMINAL

# FUNÇÃO ESPELHO(): AÇÃO DENTRO DO JOGO
def ESPELHO():
    print("Seu reflexo sorri.")
    input("aperte ENTER para continuar")
    LIMPAR()

def SALVAR(jogador):
    
    # SALVANDO OS ATRIBUTOS DO OBJETO, NESSE CASO O JOGADOR
    with open(arquivo_salvo, "w") as save:
        json.dump(vars(jogador), save)

def CARREGAR(jogador):
    try:
        with open(arquivo_salvo, "r") as save:
            dados = json.load(save) # PEGA O ARQUIVO QUE EU SALVEI E APELIDEI COMO "save"
            LIMPAR()
            print("Arquivo carregado com SUCESSO")
            input("aperte ENTER para continuar") 
            LIMPAR()

    except FileNotFoundError:
        LIMPAR()
        print("Arquivo de save NÃO encontrado")
        input("aperte ENTER para continuar")
        LIMPAR()

        jogador.escolha = dados['escolha']

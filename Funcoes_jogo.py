# CHAMEI A FUNÇÃO RUN() DA BIBLIOTECA "SUBPROCESS"
# SUBSTITUTO DO "OS.SYSTEM"
from subprocess import run

# REDUZI A FUNÇÃO PARA FICAR MAIS LIMPO E PRÁTICO
def LIMPAR():
    run('cls', shell = True) # PEDE PARA LIMPAR O TERMINAL

# FUNÇÃO ESPELHO(): AÇÃO DENTRO DO JOGO
def ESPELHO():
    print("Seu reflexo sorri.")
    input("aperte ENTER para continuar")
    LIMPAR()


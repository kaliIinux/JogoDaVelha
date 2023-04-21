import inquirer
from matriz_class import Matriz


def regras():
    
    """
    Regras para que o usuário possa
    entender como funciona o jogo.
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    print("JOGO DA VELHA\n")
    print("Olá jogador! Caso nunca tenha jogado antes, vou lhe passar algumas regras antes de começar:\n")
    print("1- Para escolher uma posição, é necessário informar"
          "a linha e coluna que deseja jogar, seguindo a numeração"
          "da matriz;\n")
    print("2- Só é permitido digitar números inteiros de 1 à 3;\n")
    print("3- Vence o jogador que conseguir formar primeiro uma ")
    print("linha com três símbolos iguais, seja ela na horizontal,"
          "vertical ou diagonal;\n")
    print("4- Caso ninguém consiga formar a sequência de três"
          "símbolos iguais, o jogo acaba em 'Velha';\n")
    print("*Lembre-se, o bot também pode ganhar a partida, então fique atento!\n")
    print("Boa jogatina!\n")
    
def message_start():
    
    """
    Printa a mensagem de bem vindo e mostra
    o desenho da matriz.
    """
    
    print("*"*27)
    print("BEM VINDO AO JOGO DA VELHA!")
    print("*"*27)

    print("   1   2   3 ")
    print("1 [ ] [ ] [ ]\n2 [ ] [ ] [ ]\n3 [ ] [ ] [ ]\n")

def menu():
    
    """
    Menu onde o usuário pode escolher
    se quer jogar, ver as regras ou sair
    do programa.
    """
    
    while True:
        questions = [
        inquirer.List('option',
                    message="",
                    choices=['JOGAR','REGRAS', 'SAIR'],
                ),
        ]
        answers = inquirer.prompt(questions)

        if answers['option'] == 'JOGAR':
            print("\x1b[2J\x1b[1;1H", end="")
            main()
            
        elif answers['option'] == 'REGRAS':
            print("\x1b[2J\x1b[1;1H", end="")
            regras()
            
        else:
            print("\x1b[2J\x1b[1;1H", end="")
            exit()
            
def main():
    
    """
    Estrutura do jogo da velha,
    onde importo o objeto, os
    métodos e as funções para
    realizar a lógica do jogo
    """
    
    message_start()

    matriz = Matriz()
    
    count = 0
    
    while True:
        
        escolha = matriz.user_choice()
        
        if matriz.validacao() == True:
            break

        elif escolha == True:
            matriz.bot_choice()
            count += 1

        if count >= 5:
            matriz.messagem_velha()
            break
        
        else:
            matriz.jogada()

if __name__ == "__main__":
    menu()
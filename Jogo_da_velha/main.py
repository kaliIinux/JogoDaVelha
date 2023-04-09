from random import randint
import inquirer

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

def matriz():
    
    """
    Variável matriz, onde serão feitas
    todas as alterações ao longo do jogo.
    
    Retorna a própria matriz.
    """
    
    m = [['','',''],
    ['','',''],
    ['', '', '']
    ]
    return m

def user_choice(m):

    """
    Função que define o chute do 
    usuário na matriz do jogo da velha 
    """
    
    while True:
        
        line = int(input("Digite a linha: ")) -1
        column = int(input("Digite a coluna: ")) -1

        if m[line][column] == 'X' or m[line][column] == 'O':
            print("Opção inválida, tente novamente")
            
        else: 
            m[line][column] = 'X'
            return True

def bot_choice(m):
    
    """
    Função que define o chute do
    computador na matriz do jogo da velha
    """
    
    i = 0
    
    while True:
        
        line_sort = randint(0, 2)
        column_sort = randint(0, 2)
        
        if m[line_sort][column_sort] == 'X' or m[line_sort][column_sort] == 'O':
            i += 1
            
        else:
            m[line_sort][column_sort] = 'O'
            break

        if i >= 9:
            break
                   
def validacao(m):
    
    """
    Realizar a validação na matriz,
    se o jogador ganhou ou perdeu.

    Retorna um booleano para realizar
    outr validação no main.
    """
    
    if m[0][0] == m[0][1] == m[0][2] == 'X':
        print("Você ganhou!")
        return True
            
    elif m[1][0] == m[1][1] == m[1][2] == 'X':
        print("Você ganhou!")
        return True
        
    elif m[2][0] == m[2][1] == m[2][2] == 'X':
        print("Você ganhou!")
        return True
    
    elif m[0][0] == m[1][0] == m[2][0] == 'X':
        print("Você ganhou!")
        return True
    
    elif m[0][1] == m[1][1] == m[2][1] == 'X':
        print("Você ganhou!")
        return True
    
    elif m[0][2] == m[1][2] == m[2][2] == 'X':
        print("Você ganhou!")
        return True
        
    elif m[0][0] == m[1][1] == m[2][2] == 'X':
        print("Você ganhou!")
        return True
    
    elif m[0][2] == m[1][1] == m[2][0] == 'X':
        print("Você ganhou!")
        return True
        
    elif m[0][0] == m[0][1] == m[0][2] == 'O':
        print("Você perdeu!")
        return True
        
    elif m[1][0] == m[1][1] == m[1][2] == 'O':
        print("Você perdeu!")
        return True
    
    elif m[2][0] == m[2][1] == m[2][2] == 'O':
        print("Você perdeu!")
        return True
    
    elif m[0][0] == m[1][0] == m[2][0] == 'O':
        print("Você perdeu!")
        return True
    
    elif m[0][1] == m[1][1] == m[2][1] == 'O':
        print("Você perdeu!")
        return True
    
    elif m[0][2] == m[1][2] == m[2][2] == 'O':
        print("Você perdeu!")
        return True
    
    elif m[0][0] == m[1][1] == m[2][2] == 'O':
        print("Você prerdeu!")
        return True
        
    elif m[0][2] == m[1][1] == m[2][0] == 'O':
        print("Você perdeu!")
        return True

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
            exit()
            
def main():
    
    """
    Estrutura do jogo da velha,
    onde importo as outras funções
    e realizo a lógica do jogo.
    """
    
    message_start()

    m = matriz()
    
    count = 0
    
    while True:
        
        if validacao(m=m) == True:
            break
        
        user_choice(m)
        count += 1
        
        bot_choice(m)
            
        if count >= 5:
            print("\x1b[2J\x1b[1;1H", end="")
            print("Velha!\n")
            print("    1    2    3  ")
            print(f"1 {m[0]}\n2 {m[1]}\n3 {m[2]}\n")
            break
        
        else:
            print("\x1b[2J\x1b[1;1H", end="")
            print("    1    2    3  ")
            print(f"1 {m[0]}\n2 {m[1]}\n3 {m[2]}\n") 

if __name__ == "__main__":
    menu()
from random import randint


def message_start():
    print("*"*25)
    print("  Welcome to tic tac toe  ")
    print("*"*25)

    print("[] [] []\n[] [] []\n[] [] []\n")

def user_choice():

    """
    Função que define o chute do 
    usuário na matriz do jogo da velha 
    """

    m = [['','',''],
    ['','',''],
    ['', '', '']
    ]

    while True:
        line = int(input("Digite a linha: ")) -1
        column = int(input("Digite a coluna: ")) -1

        if m[line][column] == 'X' or m[line][column] == 'O':
            print("Opção inválida, tente novamente")

        else: 
            m[line][column] = 'X'
            print(f" {m[0]}\n {m[1]}\n {m[2]}\n")

def bot_choice():
    i = 0

    while True:
        line_sort = randint(0, 2)
        column_sort = randint(0, 2)

def main():

    message_start()

    while True:
        user_choice()

if __name__ == "__main__":
    main()

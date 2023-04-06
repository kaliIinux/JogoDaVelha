from random import randint


def message_start():
    print("*"*25)
    print("  Welcome to tic tac toe  ")
    print("*"*25)

    print("   1   2   3 ")
    print("1 [ ] [ ] [ ]\n2 [ ] [ ] [ ]\n3 [ ] [ ] [ ]\n")

def matriz():
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
    
    if m[0][0] == m[0][1] == m[0][2] == 'X':
        print("Você ganhou!")
            
    elif m[1][0] == m[1][1] == m[1][2] == 'X':
        print("Você ganhou!")
        
    elif m[2][0] == m[2][1] == m[2][2] == 'X':
        print("Você ganhou!")
        
    elif m[0][0] == m[1][0] == m[2][0] == 'X':
        print("Você ganhou!")
        
    elif m[0][1] == m[1][1] == m[2][1] == 'X':
        print("Você ganhou!")
        
    elif m[0][2] == m[1][2] == m[2][2] == 'X':
        print("Você ganhou!")
        
    elif m[0][0] == m[1][1] == m[2][2] == 'X':
        print("Você ganhou!")
    
    elif m[0][2] == m[1][1] == m[2][0] == 'X':
        print("Você ganhou!")
    
    elif m[0][0] == m[0][1] == m[0][2] == 'O':
        print("Você perdeu")
            
    elif m[1][0] == m[1][1] == m[1][2] == 'O':
        print("Você perdeu!")
        
    elif m[2][0] == m[2][1] == m[2][2] == 'O':
        print("Você perdeu!")
        
    elif m[0][0] == m[1][0] == m[2][0] == 'O':
        print("Você perdeu!")
        
    elif m[0][1] == m[1][1] == m[2][1] == 'O':
        print("Você perdeu!")
        
    elif m[0][2] == m[1][2] == m[2][2] == 'O':
        print("Você perdeu!")
        
    elif m[0][0] == m[1][1] == m[2][2] == 'O':
        print("Você prerdeu!")
    
    elif m[0][2] == m[1][1] == m[2][0] == 'O':
        print("Você perdeu!")

def main():

    message_start()

    m = matriz()
    
    count = 0
    
    while True:
        
        validacao(m=m)
        
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
            print(m[0][0], m[0][1], m[0][2])
        

if __name__ == "__main__":
    main()
from random import randint

class Matriz:

    """
    Classe onde defino o meu objeto
    matriz e seus métodos.
    """

    def __init__(self):
        self.__matriz = [['','',''], ['','',''], ['', '', '']]

    def user_choice(self):

        """
        Função que define o chute do 
        usuário na matriz do jogo da velha 
        """

        line = int(input("Digite a linha: ")) -1
        column = int(input("Digite a coluna: ")) -1

        while True:

            if self.__matriz[line][column] == 'X' or self.__matriz[line][column] == 'O':
                break

            else: 
                self.__matriz[line][column] = 'X'
                return True
        
    def bot_choice(self):
    
        """
        Função que define o chute do
        computador na matriz do jogo da velha
        """
    
        i = 0
        
        while True:
            
            line_sort = randint(0, 2)
            column_sort = randint(0, 2)
            
            if self.__matriz[line_sort][column_sort] == 'X' or self.__matriz[line_sort][column_sort] == 'O':
                i += 1
                
            else:
                self.__matriz[line_sort][column_sort] = 'O'
                break

            if i >= 9:
                break

    def validacao(self):

        """
        Método que realiza a validação no objeto,
        se o jogador ganhou ou perdeu.
        Retorna um booleano para realizar
        outra validação no main.
        """

        if self.__matriz[0][0] == self.__matriz[0][1] == self.__matriz[0][2] == 'X':
            print("Você ganhou!")
            return True
                
        elif self.__matriz[1][0] == self.__matriz[1][1] == self.__matriz[1][2] == 'X':
            print("Você ganhou!")
            return True
            
        elif self.__matriz[2][0] == self.__matriz[2][1] == self.__matriz[2][2] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.__matriz[0][0] == self.__matriz[1][0] == self.__matriz[2][0] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.__matriz[0][1] == self.__matriz[1][1] == self.__matriz[2][1] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.__matriz[0][2] == self.__matriz[1][2] == self.__matriz[2][2] == 'X':
            print("Você ganhou!")
            return True
            
        elif self.__matriz[0][0] == self.__matriz[1][1] == self.__matriz[2][2] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.__matriz[0][2] == self.__matriz[1][1] == self.__matriz[2][0] == 'X':
            print("Você ganhou!")
            return True
            
        elif self.__matriz[0][0] == self.__matriz[0][1] == self.__matriz[0][2] == 'O':
            print("Você perdeu!")
            return True
            
        elif self.__matriz[1][0] == self.__matriz[1][1] == self.__matriz[1][2] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.__matriz[2][0] == self.__matriz[2][1] == self.__matriz[2][2] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.__matriz[0][0] == self.__matriz[1][0] == self.__matriz[2][0] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.__matriz[0][1] == self.__matriz[1][1] == self.__matriz[2][1] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.__matriz[0][2] == self.__matriz[1][2] == self.__matriz[2][2] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.__matriz[0][0] == self.__matriz[1][1] == self.__matriz[2][2] == 'O':
            print("Você prerdeu!")
            return True
            
        elif self.__matriz[0][2] == self.__matriz[1][1] == self.__matriz[2][0] == 'O':
            print("Você perdeu!\n")
            return True
    
    def messagem_velha(self):

        """
        Método para exibir a matriz e 
        a mensagem de velha.
        """
        
        print("\x1b[2J\x1b[1;1H", end="")
        print("Velha!\n")
        print("    1    2    3  ")
        print(f"1 {self.__matriz[0]}\n2 {self.__matriz[1]}\n3 {self.__matriz[2]}\n")

    def jogada(self):

        """
        Método para printar a matriz
        enquanto o jogo não termina.
        """
        
        print("\x1b[2J\x1b[1;1H", end="")
        print("    1    2    3  ")
        print(f"1 {self.__matriz[0]}\n2 {self.__matriz[1]}\n3 {self.__matriz[2]}\n")
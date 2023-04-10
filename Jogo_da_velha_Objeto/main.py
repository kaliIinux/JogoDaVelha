from random import randint
import inquirer

class Matriz:
    
    """
    Classe matriz, onde serão feitas
    todas as alterações ao longo do jogo.
    """
    
    def matriz(self):
    
        self.__matriz = [['','',''],
                ['','',''],
                ['', '', '']
                ]
        
    def user_choice(self):
        
        while True:
            
            line = int(input("Digite a linha: ")) -1
            column = int(input("Digite a coluna: ")) -1

            if self.matriz[line][column] == 'X' or self.matriz[line][column] == 'O':
                print("Opção inválida, tente novamente")
                
            else: 
                self.matriz[line][column] = 'X'
                return True
    def bot_choice(self):

    
        i = 0
        
        while True:
            
            line_sort = randint(0, 2)
            column_sort = randint(0, 2)
            
            if self.matriz[line_sort][column_sort] == 'X' or self.matriz[line_sort][column_sort] == 'O':
                i += 1
                
            else:
                self.matriz[line_sort][column_sort] = 'O'
                break

            if i >= 9:
                break
                   
    def validacao(self):
        
        """
        Realizar a validação na matriz,
        se o jogador ganhou ou perdeu.

        Retorna um booleano para realizar
        outr validação no main.
        """
        
        if self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 'X':
            print("Você ganhou!")
            return True
                
        elif self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 'X':
            print("Você ganhou!")
            return True
            
        elif self.matriz[2][0] == self.matiz[2][1] == self.matriz[2][2] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 'X':
            print("Você ganhou!")
            return True
            
        elif self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 'X':
            print("Você ganhou!")
            return True
        
        elif self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 'X':
            print("Você ganhou!")
            return True
            
        elif self.matriz [0][0] == self.matriz[0][1] == self.matriz[0][2] == 'O':
            print("Você perdeu!")
            return True
            
        elif self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 'O':
            print("Você perdeu!")
            return True
        
        elif self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 'O':
            print("Você prerdeu!")
            return True
            
        elif self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 'O':
            print("Você perdeu!")
            return True
        
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
            exit()
            
def main():
    
    """
    Estrutura do jogo da velha,
    onde importo as outras funções
    e realizo a lógica do jogo.
    """
    
    message_start()

    matriz = Matriz([['','',''],
                ['','',''],
                ['', '', '']
                ]
        )
    
    count = 0
    
    while True:
        
        if matriz.validacao == True:
            break
        
        matriz.user_choice
        count += 1
        
        matriz.bot_choice
            
        if count >= 5:
            print("\x1b[2J\x1b[1;1H", end="")
            print("Velha!\n")
            print("    1    2    3  ")
            print(f"1 {matriz.matriz[0]}\n2 {matriz.matriz[1]}\n3 {matriz.matriz[2]}\n")
            break
        
        else:
            print("\x1b[2J\x1b[1;1H", end="")
            print("    1    2    3  ")
            print(f"1 {matriz.matriz[0]}\n2 {matriz.matriz[1]}\n3 {matriz.matriz[2]}\n") 

if __name__ == "__main__":
    menu()
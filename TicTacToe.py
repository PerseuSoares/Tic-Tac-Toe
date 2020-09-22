# Jogo da Velha

"""         Board

    top-L | top-M | top-R
    ----- + ----- + -----
    mid-L | mid-M | mid-R
    ----- + ----- + -----
    low-L | low-M | low-R
"""

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

class TicTacToe:
    """Simula o funcionamento do jogo da velha."""

    def __init__(self):
        self.num = 0

    def printBoard(self):
        """Mostra o Tabuleiro."""
        print('>>>JOGO DA VELHA<<<\n')
        print(' ' + board['top-L'] + '  |  ' + board['top-M'] + '  |  ' + board['top-R'])
        print('--- + --- + ---')
        print(' ' + board['mid-L'] + '  |  ' + board['mid-M'] + '  |  ' + board['mid-R'])
        print('--- + --- + ---')
        print(' ' + board['low-L'] + '  |  ' + board['low-M'] + '  |  ' + board['low-R'])

    def xTurn(self, turnX):
        """Atribui o valor 'X' para a posição informada"""

        if turnX not in board.keys():
            while turnX not in board.keys():
                print("Posição não existe. Insira uma posição válida.")
                turnX = input('X turn: ')
            if board[turnX] == 'X' or board[turnX] == 'O':
                while board[turnX] == 'X' or board[turnX] == 'O':
                    print('Posição Ocupada. Tente outra posição.')
                    turnX = input('X turn: ')
                board[turnX] = 'X'
        else:
            if board[turnX] == 'X' or board[turnX] == 'O':
                while board[turnX] == 'X' or board[turnX] == 'O':
                    print('Posição Ocupada. Tente outra posição.')
                    turnX = input('X turn: ')
                board[turnX] = 'X'
            else:
                board[turnX] = 'X'


    def oTurn(self, turnO):
        """Atribui o valor 'O' para a posição informada"""

        if turnO not in board.keys():
            while turnO not in board.keys():
                print("Posição não existe. Insira uma posição válida.")
                turnO = input('X turn: ')
            if board[turnO] == 'X' or board[turnO] == 'O':
                while board[turnO] == 'X' or board[turnO] == 'O':
                    print('Posição Ocupada. Tente outra posição.')
                    turnO = input('O turn: ')
                board[turnO] = 'O'
        else:
            if board[turnO] == 'X' or board[turnO] == 'O':
                while board[turnO] == 'X' or board[turnO] == 'O':
                    print('Posição Ocupada. Tente outra posição.')
                    turnO = input('O turn: ')
                board[turnO] = 'O'
            else:
                board[turnO] = 'O'

    def verification(self):
        """Verifica todas as possibilidades de vitória e a possibilidade de ninguém ter ganhado."""

        if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
            print('Fim de Jogo! X Ganhou!')
            return True
        if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X':
            return True
        if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X':
            return True
        if board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X':
            return True
        if board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X':
            return True
        if board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X':
            return True
        if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
            return True
        if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X':
            return True

        if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
            return True
        if board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O':
            return True
        if board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O':
            return True
        if board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O':
            return True
        if board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O':
            return True
        if board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O':
            return True
        if board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
            return True
        if board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O':
            return True

        if self.num == 9:
            return True

    def instructions(self):
        """Intruções do jogo"""
        print("Informe a posição que deseja marcar de acordo com o tabuleiro abaixo:\n\n" + "\
             top-L | top-M | top-R\n\
             ----- + ----- + -----\n\
             mid-L | mid-M | mid-R\n\
             ----- + ----- + -----\n\
             low-L | low-M | low-R")

    def count(self):
        """Contador para informar o fim do jogo"""
        self.num = self.num + 1

game = TicTacToe()

def main():
    """Função de execução do game"""
    while not game.verification():
        game.printBoard()
        game.instructions()
        if game.num % 2 == 0:
            game.xTurn(input('Digite a posição.\nX Turn: '))
        else:
            game.oTurn(input('Digite a posição.\nO Turn: '))
        game.count()
        game.verification()
        game.printBoard()

main()
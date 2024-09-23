from modulo import *

if __name__ == '__main__':
    usuario = Pessoa('',0,0.0)

    usuario.nome = input('Informe seu nome: ')
    usuario.idade = int(input('Informe sua idade: '))
    usuario.altura = input('Informe sua altura: ')


    print(str(usuario))
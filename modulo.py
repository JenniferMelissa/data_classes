#dataclasses
#javalizacao dos atributos da classe
#importa a biblioteca dataclasses e cria a classe
#O que faz: tipa os atributos, pois python é uma linguagem nao tipada, e com essa bilbioteca, consigo tipar os atributos
#desvatagem: ainda asim precisa definir construtor e valores, entao acaba complicado um pouco a forma de fazer

from dataclasses import dataclass 

@dataclass
class Pessoa:
    #atributos
    nome: str
    idade: int
    altura: float

    def __str__(self):
        return f'Ola meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} metros de altura.'
    
    def __del__(self):
        print(f'O objeto {self.altura} foi eliminado com sucesso.')
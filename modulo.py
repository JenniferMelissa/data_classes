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
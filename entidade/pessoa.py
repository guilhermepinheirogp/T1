from abc import ABC, abstractmethod
from entidade.endereco import Endereco

class Pessoa(Endereco, ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, idade: int, rua: str, numero: int, complemento: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(idade, int):
            self.__idade = idade
        self.__endereco = Endereco(rua, numero, complemento)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

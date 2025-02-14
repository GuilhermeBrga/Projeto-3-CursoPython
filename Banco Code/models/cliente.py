from datetime import date

from utils.helper import data_str, str_data

class Cliente:

    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo_cliente: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_data(data_nascimento)
        self.__data_cadastro: date = date.today()
        
        Cliente.contador += 1


    @property
    def codigo_cliente(self: object) -> int:
        return self.__codigo_cliente
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def email(self: object) -> str:
        return self.__email
    
    @property
    def cpf(self: object) -> str:
        return self.__cpf
    
    @property
    def data_nascimento(self: object) -> str:
        return data_str(self.__data_nascimento)
    
    @property
    def data_cadastro(self: object) -> str:
        return data_str(self.__data_cadastro)
    
    def __str__(self: object) -> str:
        return f"Código: {self.codigo_cliente} \nNome: {self.nome} \nData de nascimento: {self.data_nascimento} \nData de cadastro: {self.data_cadastro}\n"
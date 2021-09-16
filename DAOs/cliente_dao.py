from DAOs.dao import DAO
from entidade.cliente import Cliente


#cada entidade terá uma classe dessa, implementação bem simples
class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str)):
            super().add(cliente.cpf, cliente)
# update é NOVO
    def update(self, cliente: Cliente):
        if((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str)):
            super().update(cliente.cpf, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if(isinstance(key, str)):
            return super().remove(key)

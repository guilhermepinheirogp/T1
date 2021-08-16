from entidade.limpeza import Limpeza
from telas.telaLimpeza import TelaLimpeza
#from controladores.controladorSistema import ControladorSistema


class ControladorLimpeza:
    def __init__(self, controlador_sistema):
        self.__tela_limpeza = TelaLimpeza()
        self.__limpezas = []
        self.__controlador_sistema = controlador_sistema

    def inclui_limpeza(self): # VISTO
        dados_limpeza = self.__tela_limpeza.pega_dados_limpeza()
        limpeza = Limpeza(dados_limpeza["nome"], dados_limpeza["cpf"], dados_limpeza["idade"], dados_limpeza["rua"], dados_limpeza["numero"],
                          dados_limpeza["complemento"], dados_limpeza["matricula"], dados_limpeza["salario"])
        if self.pega_limpeza_por_matricula(dados_limpeza["matricula"]) is None:
            self.__limpezas.append(limpeza)
            self.__tela_limpeza.mostra_mesagem('Funcionário da Limpeza adicionado com sucesso!')
        else:
            self.__tela_limpeza.mostra_mesagem('Não foi possível cadastrar o funcionário pois a matrícula já existe!')

    def exclui_limpeza(self): # VISTO
        self.listar_limpezas()
        matricula_funcionario_excluido =  self.__tela_limpeza.seleciona_limpeza()
        for funcionario_limpeza in self.__limpezas:
            if funcionario_limpeza.matricula == matricula_funcionario_excluido:
                self.__limpezas.remove(self.pega_limpeza_por_matricula(matricula_funcionario_excluido))
                self.__tela_limpeza.mostra_mesagem('Funcionário da Limpeza excluído com sucesso!')
                self.listar_limpezas()
            else:
                self.__tela_limpeza.mostra_mesagem('Não foi possível excluir o funcionário, pois a matrícula informada não está na lista!')

    def altera_limpeza(self):
        self.listar_limpezas()
        matricula_funcionario_alterado = self.__tela_limpeza.seleciona_limpeza()
        for funcionario_limpeza in self.__limpezas:
            if funcionario_limpeza.matricula == matricula_funcionario_alterado:
                novos_dados = self.__tela_limpeza.pega_dados_para_alterar_limpeza()
                funcionario_limpeza.nome = novos_dados["nome"]
                funcionario_limpeza.idade = novos_dados["idade"]
                funcionario_limpeza.endereco.rua = novos_dados["rua"]
                funcionario_limpeza.endereco.numero = novos_dados["numero"]
                funcionario_limpeza.endereco.complemento = novos_dados["complemento"]
                funcionario_limpeza.salario = novos_dados["salario"]
                self.__tela_limpeza.mostra_mesagem('Funcionário da limpeza alterado com sucesso!\n')
                self.listar_limpezas()
            else:
                self.__tela_limpeza.mostra_mesagem('Não foi possível alterar o funcionário, pois a matrícula informada não está na lista!')

    def listar_limpezas(self): # visto
        self.__tela_limpeza.mostra_mesagem("LISTA DE FUNCIONÁRIO".center(30, '-'))
        for limpeza in self.__limpezas:
            self.__tela_limpeza.mostra_mesagem(f'Nome: {limpeza.nome} | CPF: {limpeza.cpf} | Idade: {limpeza.idade}\nRua: {limpeza.endereco.rua} | Número: {limpeza.endereco.numero} | Complemento: {limpeza.endereco.complemento}\nMatrícula: {limpeza.matricula} |Salário: {limpeza.salario}')
        if len(self.__limpezas) == 0:
            self.__tela_limpeza.mostra_mesagem("No momento a lista de funcionários de limpeza está vazia.")

    def pega_limpeza_por_matricula(self, matricula: int): # VISTO
        for limpeza in self.__limpezas:
            if limpeza.matricula == matricula:
                return limpeza
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        opcoes = {0: self.retornar, 1: self.inclui_limpeza, 2: self.altera_limpeza, 3: self.exclui_limpeza, 4: self.listar_limpezas}
        continua = True
        while continua:
            opcoes[self.__tela_limpeza.tela_opcoes()]()

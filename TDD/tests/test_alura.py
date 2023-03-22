import pytest
from pytest import mark
from TDD.codigo_base_alura_mexido import Funcionario


class TestClass:
    # def precisa ser test_ e uma explicação(verbosa) bem fina do que vai ser feito
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # metodo pra testes: give-when-then = Dado(contexto)-Quando(ação)-Então(desfecho)
        # metodo pra testes 2: Arrange-Act-Assert = Organizar-Agir-Averiguar

        entrada = '13/03/2000'  # Given-contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-então

    def test_quando_sobrenome_recebe_leonardo_wons_deve_retornar_wons(self):

        entrada = 'leonardo wons'  # given
        esperado = 'wons'

        funcionario_teste_nome = Funcionario(entrada, '11/11/1111', 1111)

        resultado = funcionario_teste_nome.sobrenome()  # when

        assert resultado == esperado  # then

    @mark.skip  # pular este teste
    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):

        entrada_salario = 100000  # given
        entrada_nome = 'leonardo wons'
        esperado = 90000

        funcionario_teste_decrescimo = Funcionario(entrada_nome, '11/11/1111', entrada_salario)

        funcionario_teste_decrescimo.decrescimo_salario()  # when
        resultado = funcionario_teste_decrescimo.salario

        assert resultado == esperado  # then

    @mark.calcula_bonus
    def test_quando_calcular_bonus_recebe_1000_retorna_100(self):

        entrada = 1000  # given
        esperado = 100

        funcionario_teste_bonus = Funcionario('Leonardo wons', '11/11/1111', entrada)

        resultado = funcionario_teste_bonus.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcula_bonus
    def test_quando_calcular_bonus_recebe_100000_retorna_exception(self):
        with pytest.raises(Exception):

            entrada = 100000  # given

            funcionario_teste_bonus = Funcionario('Leonardo wons', '11/11/1111', entrada)

            resultado = funcionario_teste_bonus.calcular_bonus()  # when

            assert resultado  # then

    def test_quando_str_recebe_nome_nacimento_salario_retorna_str_formatada(self):

        nome, data_nascimento, salario = 'Leonardo wons teste', '11/22/3333', 1000  # guiven
        esperado = 'Funcionario(Leonardo wons teste, 11/22/3333, 1000)'

        funcionario_teste_str = Funcionario(nome, data_nascimento, salario)

        resultado = funcionario_teste_str.__str__()  # when

        assert resultado == esperado  # then

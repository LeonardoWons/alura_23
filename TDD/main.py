# PRIMEIRA AULA
"""
    -------- meu codigo -----------
    from codigo_base_alura import Funcionario


    def teste_idade(nome, dia: int, mes: int, ano: int, salario: int):

        funcionario_teste = Funcionario(nome, f'{dia}/{mes}/{ano}', salario)
        print(f'Teste = {funcionario_teste.idade()}')


    x = 'lslndfaksndkjasnkdnasknkdaskdjan'
    lista_nomes = []
    for i in x:
        lista_nomes.append(i)

    for nome in lista_nomes:
        teste_idade(nome, 2, 2, 2000, 1111)

    -------- meu codigo -----------

    -------- codigo da alura -----------
    
    from codigo.bytebank import Funcionario
    
    def teste_idade():
        funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
        print(f'Teste = {funcionario_teste.idade()}')
    
        funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
        print(f'Teste = {funcionario_teste1.idade()}')
    
        funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
        print(f'Teste = {funcionario_teste2.idade()}')
    
    teste_idade()
    
    -------- codigo da alura -----------

    não achei nada de interessante, foi mostrado alguns metodos muito lentos e estranhos(provavelmente como exemplo) mas fiz de um modo que eu acho melhor.

"""

# SEGUNDA AULA
"""
    utilizando o pytest, criar diretorio nome= tests, arquivo __init__.py e o arquivo para os testes(ex: testes_alura) 
    
    Agora sim fizemos teste, não muito elaborado, mas é um começo, esta tudo explicado como usar na tests/test_alura
"""

# TERCEIRA AULA
"""
    codigo = Test-driven development
    Depois de receber uma tarefa, primeiro fazer os testes, fazer um codigo para passar no teste feito e depois refatorar deixando mais legivel e nas normas
    
    Fiz meu primeiro codigo, achei muito interessante, principalmennte a ideia de deixar o codigo bem limpo "só para passar" no teste
"""

# QUARTA AULA
"""
    Fiz um teste que o resultado é um erro(Exception) customizado, foi bem simples, mas é algo novo e legal
    
    Aprendi a organizar os testes:
    - Caso queira ativar testes que possui uma palavra igual = pytest -k palavra
    - Utilizando MARK(tags) = em cima do def utilizar @mark.nome_da_tag. no terminal = pytest -m nome_da_tag
    
    Marks que ja existem no pytes = pytest --markers
    
    Fazer arquivo pytest.ini para colocar os markers personalizados
"""

# QUINTA AULA
"""
    Configuração de "cobertura" dos testes, se tem teste para tudo (pytest-cov), no terminal = pytest --cov
    pytest --cov=codigo tests/  (codigo = diretorio com o codigo) (tests = nome da pasta onde esta os testes)
    pytest --cov=codigo tests/ --cov-report term-missing (para ver qual linha esta faltando ser "coberta")

    pytest --cov=codigo tests/ --cov-report html cria uma pasta com index.html, possui uma visualização mais bonita 
        e organizada o navegador (podendo mudar o nome do diretorio na .coveragerc)

    para não fazer testes 'inuteis' como teste do return __str__, precisa criar um arquivo .coveragerc(assim como o pytest.ini)
    no .coveragerc precisa colocar a função que não é para ser testada
    
    no .coveragerc pode colocar o caminho da pasta q vai ser feita a checagem
    
    pytest --junitxml nome.xml (reports) 
    pytest --cov-report xml    (cobertura)
"""
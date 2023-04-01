# Curso tres
# Todas as aulas (acabei esquecendo de escrever as outras aulas kkk)
"""
    Versionamento, criando versoes para que possa adicionar novos recursos, sem perder quem usava antes da atualização:

    AcceptHeaderVersioning = passar a versão no cabeçalho
    URLPathVersioning = adiciona a versao no endereço URL, utilizando uma variavel para pegar a versao depois
    NamespaceVersioning = a versão fica na URL v1/alunos/, possuindo uma URL para cada versao
    HostNameVersioning = versão no dominio v1.exemplo.com/alunos
    QueryParameterVersioning = transfere a versao atraves de um GET alunos/?version=1

    Vamos utilizar o QueryParameter, precisa setar no settings.py

    foi adiciona as permisões de alguns usuarios no django ADMIN, junto com a configuração de passar isto para a API

    Refatorando codigo duplicado, passando permissoes padroes no settings.py para todas as views

    Setamos os metodos que podem ser usado em cada viewset (GET, PUT, DELETE, etc), por padrão todos são permitidos

    Setamos a quantidade que cada user pode fazer uma requisição throttling

    A gloria de Rest de Richardson:
        Lama XML: HTPP com transporte para iterações remotas, sem utilizar qualquer mecanismo da web(endpoint)
        endpoit = .../cria-curso, .../deleta-curso, etc

        Nivel 1: introdução de recursos individuais para cada modelo em vez de ficar tudo em um endpoint
        Nivel 2: Intruduz conjunto padrao de verbos(GET, DELETE, ETC)
        Nivel 3: Buscar uma forma de fazer um protocolo auto-documentado(documentação, cabeçalho, etc)

    implementar nivel 3, foi feito um modo de voltar o local(.../curso/id) no momento que o curso é criado

    Foi instalado o node.js para consumir(utilizar) o projeto da escola (deu erro kkk)

    CORS autorização do compartilhamento de dados entre API's e sites

"""
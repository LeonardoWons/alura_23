# curso 1 flask
# Primeira aula
"""
    Foi mostrado apenas os primeiros passos, instalação e configuração base.
    Primeira aula foi realmente só inntrodução e como eu ja sei mais que o basico, não aproveitei nada.
"""

# Segunda aula
"""
    Foi mostrado como utilizar variaveis dentro do HTML e como setar as variaveis no codigo.
    {{....}}: usado para facilitar a exibição de código python como um output
    
    Foi mostrado como escrever for dentro do HTML 
    {%....%}: usado para inserir estruturas Python dentro de um arquivo html;
    
    {% for i in list %} 
        {{ i }} 
    {% endfor %} 
    
    {#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML.
    
    Escrevendo if no html
    {% if lista %}
      <p>Temos {{ len(lista) }} apostilas no nosso site. </p>
    {% else %}
      <p>Nenhuma apostila aqui... </p>
    {% endif %}
    
    Foi criado uma classe Jogo para deixar mais completo as informaçoes de cada jogo.
"""

# Terceira aula
"""
    Como utilizar input no html, salvar no python para depois utilizar
    Tudo isto utilizando um formulario, foi mostrado como configurar, requisitar e redirecionar. 
"""

# Quarta aula
"""
    Foi mostrado algo novo, nunca tinha utilizado Bootstrap, é muito bom pra algo rapido, só pra ter uma ideia
    
    Algo muito legal foi a adição do template.html, para tirar as partes duplicadas do html utilizando a tag:
    {% extends "template.html" %}
    {% block nome_pro_bloco %}
    {% endblock %}
    
    utilizando o {{url_for('static', filename='nome_arquivo.css')}} podemos encontrar o arquivo independente de quantas pastas tem antes. (normalmente utilizado no stylesheet)
"""

# Quinta/sexta aula
"""
    coisas novas nessa aula, achei bem proveitoso, primeira vez que faço um sistema de login no flask
    
    Sistema de segurança utilizando login e senha, com retenção de informaçoes utilizando o session(cookies)
    (precisa utilizar app.secret_key = 'alguma_senha' para funcionar)
    
    Com o metodo flash() podemos mostrar uma msg unica rapidamente
    No html precisa adicionar linhas de cod, mas esta no login.html
    
    Adicionei um botão chamado login para redirecionar para pagina de login
        
    query strings, mandando variaveis para proxima pagina no url ex: /pagina?variavel=var
    
    dinamizando as rotas para os nomes das funçoes e nao para o nome de rota, url_for('função')
    
    criação de usuarios para caso "vase" a senha, valide o nome do user
"""

# ------------------------------------------------------------------------------------------------------- #

# curso dois
# Primeira aula
"""
    Na primeira aula foi mostrado a instalação e config do mysql e como conectar no programa.    
    ORM é um mapeamento para escrever na linguagem desejada e ser 'traduzida' para codigo SQL.
    
    No projeto jogoteca foi feito CR (create and read)
"""

# Segunda aula
"""
    Primeiros reestrutiramos o codigo, seprando em varios arquivos para deixar mais legivel e organizado
    aprendemos a como passar variaveis de HTML > python e vice-versa
    depois terminamos de fazer o CRUD (update and delete)
"""

# Terceira aula
"""
    Utilização de imagens para os jogos e salvando no servidor, como salvar e onde salvar
"""

# Quarta aula
"""
    Colocamos javascript para trocar a capa quando receber uma capa nova
    concertando o erro de CACHE
    deletando imagens duplicadas
"""

# Quinta aula
"""
    eu ja tiha colocado botao para login, em vez de /login na url, porem isso foi feito agora no curso
    implementamos o Flask WTF para nao colocar itens nulos no formulario
    Junto com a melhoria nos formularios foi preciso adicionar um token de segurança CSRF
    CSRF é um token criado toda vez q envia um form e o servidor compara o token, se for igual, está seguro.
"""

# Sexta aula
"""
    Ultima aula, começamos refatorando a aplicação, apenas organização e style
    Depois fizemos a criptografia das senhas utilizando o flask_bcrypt
"""
import os

SECRET_KEY = 'senha_super_secreta'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='admi',
        servidor='localhost',
        database='jogoteca'
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
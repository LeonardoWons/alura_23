from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo='random',
            data_lancamento='2003-01-01',
            tipo='F',
            likes=1,
            dislikes=0,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_quais_campos_estao_sendo_serializados(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'titulo', 'data_lancamento', 'tipo', 'likes'})

    def test_verifica_conteudo_dos_campos_serializados(self):
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)

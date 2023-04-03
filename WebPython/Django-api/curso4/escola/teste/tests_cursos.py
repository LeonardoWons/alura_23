from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.creat(
            codigo_curso='CTT1',
            descricao='Curso teste 1',
            nivel='B'
        )
        self.curso_2 = Curso.objects.creat(
            codigo_curso='CTT2',
            descricao='Curso teste 2',
            nivel='A'
        )

    def test_verificar_requisicao_get_para_listar_cursos(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_verificar_requisicao_post_para_criar_cursos(self):
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'I'
        }
        response = self.client.post(self.list_url, data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_deletar_curso_um_com_metodo_delete(self):
        response = self.client.delete('/curso/1/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_deletar_curso_um_sem_metodo_delete(self):
        response = self.client.delete('/curso/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_atualizar_descricao_do_curso_um(self):
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso teste 1 atualizado',
            'nivel': 'A'
        }
        response = self.client.put('/curso/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):

    def setUP(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('livia', password='meuamor')

    def test_autenticacao_user_com_credencias_corretas(self):
        """ DOCSTRING para explicar teste """
        user = authenticate(username='livia', password='meuamor')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """ DOCSTRING para explicar teste """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_get_autorizada(self):
        """ DOCSTRING para explicar teste """
        self.client.force_login(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_autenticacao_de_user_com_username_incorreto(self):
        """ DOCSTRING para explicar teste """
        user = authenticate(username='liviaa', password='meuamor')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_de_user_com_senha_incorreto(self):
        """ DOCSTRING para explicar teste """
        user = authenticate(username='livia', password='naomeama')
        self.assertFalse((user is not None) and user.is_authenticated)

from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='003', descricao='Curso teste', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='004', descricao='Curso teste 2', nivel='I'
        )
    
    def test_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {
            'codigo_curso':'005',
            'descricao': 'Curso teste 3',
            'nivel': 'A',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put(self):
        data = {
            'codigo_curso':'005',
            'descricao': 'Curso teste 1',
            'nivel': 'I',
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
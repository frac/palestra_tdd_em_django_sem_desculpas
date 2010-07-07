"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class ModelTest(TestCase):
    def test_modelexistence(self):
        """
        verifica se os models que eu quero estao la
        """
        try:
            from foobar.forum.models import Topico
        except  ImportError:
            self.fail('O modelo topico nao foi criado ainda')



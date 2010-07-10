
---------

.. raw:: pdf

  PageBreak simplePage
    
Olá!
----


Por que testes?
---------------

Em uma palavra
--------------

Medo
----

Err..
-----

Tranquilidade
-------------

Tranquilidade de refatorar
---------------------------

.. raw:: pdf

  PageBreak longPage
    
Felicidade é um codigo com boa cobertura
----------------------------------------

O ecosistema de testes no python
-----------------------------------

* tipos

* sabores

* testrunners


.. raw:: pdf

  PageBreak longPage



Tipos de testes
---------------

    * Doctest

    * unittest

Sabores de testes
-----------------

    * Unitarios 

    * Funcionais

    * De Regressão

    * Exótiocos
     
        * static source analysis
        * smoke test
        * load test

TestRunners
-----------
Mais liberdade de como rolar os testes

    * nose ou py.test




.. raw:: pdf

  PageBreak simplePage


Opnião Imparcial
----------------

Porque doctests são fedorentos e unittest.TestCase comanda
----------------------------------------------------------

.. raw:: pdf

  PageBreak longPage


Doctest
-------

    * Eu não gosto

    * Não tem onde colocar

    * utf8

    * Difícil de debugar


unittest.TestCase
-----------------

    * Tem o setUp e tearDown

    * Padrão

    * #coding:utf8 (quase sempre resolve)


.. raw:: pdf

  PageBreak simplePage



Porque o django.tests.TestCase comanda todos os batatais
---------------------------------------------------------


.. raw:: pdf

  PageBreak longPage


    
django TestCase
---------------

    * Test Client

    * um monte de assert úteis
    
    * Test Client
    
    * fixtures e urls
    
    * Test Client
    
    * mail
    
    * e tem o Test Client


Test Client
-----------
    
    * é o windmill / selenium de pobre

    * Testa gets and posts e amigos

    * Metodo para login no auth

    * context, forms e templates

    * Tem o twill também

    * Ótimo para functional tests

.. raw:: pdf

  PageBreak longPage




nose
----




.. raw:: pdf

  PageBreak simplePage

Use Django TestCase sempre que possível
---------------------------------------

Porque você deveria estar testando
-----------------------------------

.. raw:: pdf

  PageBreak longPage

Confiabilidade
---------------------

Código sem testes é quebrado conforme foi planejado
  -- Jacob Kaplan-Moss


Django 1.1
----------

 * startapp cria um tests.py

 * Testes transacionados 
    
    * 30 x mais rápidos



 


.. raw:: pdf

  PageBreak simplePage
    

Eu adoraria estar testando mas...


.. raw:: pdf

  PageBreak excusePage


Eu meio que sei o que é TDD
----------------------------


.. raw:: pdf

  PageBreak longPage


TDD
-------

Só escreve código quando teste falha

Só escreve teste quando tudo passa


.. raw:: pdf

  PageBreak excusePage
    


Eu nunca fiz muitos testes no Django
------------------------------------

.. raw:: pdf

  PageBreak longPage

Como fazer
-------------------------

.. code-block:: bash

    $ django-admin.py startproject foobar
    $ cd foobar/
    $ chmod +x manage.py
    $ vi settings.py

.. raw:: pdf

  PageBreak longPage

settings.py
-----------

.. code-block:: python

    import os
    PROJECT_PATH = os.path.abspath(
                        os.path.split(__file__)[0])
    ...
    config database
    ...
    TEMPLATE_DIRS = (                                                                                                                                           
        os.path.join(PROJECT_PATH,'templates'),                                                                                                                 
    ) 


.. raw:: pdf

  PageBreak simplePage

nose
----

django-nose
-----------

.. raw:: pdf

  PageBreak longPage

settings.py
-----------


.. code-block:: python
    
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    
    INSTALLED_APPS = (
        ...
        'south', # migracoes
        'django_nose', # depois do south 
    )

.. raw:: pdf

    PageBreak longPage

Hora de testar
---------------

.. code-block:: python
    

    ./manage.py test

    ------------------------------------
    Ran 0 tests in 0.000s

    OK
    Destroying test database 'default'...    

TDD
-------

Só escreve código quando teste falha

Só escreve teste quando tudo passa



Passou 
--------------------------

Escreve testes


Mais Testes, então
---------------------

.. code-block:: bash
    


    ./manage.py startapp forum
    cd forum/
    mkdir tests
    touch tests/__init__.py
    mv tests.py tests/test_topico.py


vi tests/test_topico.py
------------------------

.. code-block:: python

    #coding:utf8
    from django.test import TestCase                                                                                                                            
                                                                                                                                                                
    class TopicoTest(TestCase):                                                                                                                                  


Teste de importação
------------------------

.. code-block:: python

    def test_existe(self):                                                                                                                          
      """ O topico esta la? """                                                                                                                                                 
      try:                                                                                                                                                
        from foobar.forum.models import Topico                                                                                                         
      except ImportError:                                                                                                                                
        self.fail('Não consegui importar') 


Inclui a app no projeto
------------------------

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'foobar.forum',
    )
    


.. raw:: pdf

    PageBreak longPage

Testa
------------------------

.. code-block:: python

    F
    ====================================
    FAIL: O topico esta la?
    ------------------------------------
    Traceback (most recent call last):
      File "test_topico", line 18, in test_existe
        self.fail('Não consegui importar')
    AssertionError: Não consegui importar
    ------------------------------------
    Ran 1 test in 0.003s


TDD
-------

Só escreve código quando teste falha

Só escreve teste quando tudo passa

Falhou
--------------------------

Escreve código 

forum/models.py
---------------

.. code-block:: python

    class Topico(models.Model):                                                                                                                                 
        """representa um topico"""   
        pass

testa
-----        

.. code-block:: python

    .
    ------------------------------------
    Ran 1 test in 0.014s
        


Pera!
-----

Voce gastou 8 slides para escrever um pass?




test_extensions
---------------

.. raw:: pdf

  PageBreak longPage

settings.py
-----------


.. code-block:: python
    
    INSTALLED_APPS = (
        ...
        'south', # migracoes
        'django_nose', # depois do south 
        'test_extensions', # depois do south
    )




.. raw:: pdf

  PageBreak excusePage
    

Mas TDD é muito lento 
---------------------

e por lento eu quero dizer chato
--------------------------------

.. raw:: pdf

  PageBreak longPage

TDD: Eu queria ter isso
-----------------------


.. raw:: pdf

  PageBreak excusePage
    


Toda vez que eu tento da pau
------------------------------------

.. raw:: pdf

  PageBreak longPage

TDD: smartpants
-----------------------

I don't do test-driven development; I do stupidity-driven testing. When I do something stupid, I write a test to make sure I don't do it again." --titus brown pycon '07

    * write code to solve some problem

    * watch code break in some obvious way

    * write a test that tests that specific breakage

    * lather, rinse, repeat.



.. raw:: pdf

  PageBreak excusePage
    



O teste é mais complicado que o problema
-----------------------------------------

.. raw:: pdf

  PageBreak longPage

Longo sim complicado nao
------------------------

login test client

.. code-block:: python

    >>> client
    >>> foo[3]

.. raw:: pdf

  PageBreak excusePage
    

    
Eu conserto os testes depois
----------------------------

ou
--

Se um teste falha e' mais fácil apagar o teste
----------------------------------------------

.. raw:: pdf

  PageBreak longPage

amanha
-----------------------
    * Vai doer

        * MUITO

    por que?


.. raw:: pdf

  PageBreak excusePage


Agora é tarde demais meu projeto já existe
------------------------------------------------------------

.. raw:: pdf

  PageBreak longPage

pera olha so
-----------------------

    * regression tests

    * test_utils



.. raw:: pdf

  PageBreak excusePage



tem um monte de assertions diferentes, né?
----------------------------------------------

.. raw:: pdf

  PageBreak longPage


O!
-----------------------



Modo mais fácil:
----------------

.. code-block:: python

    >>> from django.test import TestCase
    >>> In [2]: TestCase.assert<tab><tab>


asserts
----------------

.. code-block:: python


    TestCase.assert_                TestCase.assertAlmostEqual      
    TestCase.assertAlmostEquals     TestCase.assertContains         
    TestCase.assertEqual            TestCase.assertEquals           
    TestCase.assertFalse            TestCase.assertFormError        
    TestCase.assertNotAlmostEquals  TestCase.assertNotContains      
    TestCase.assertNotEqual         TestCase.assertNotEquals        
    TestCase.assertRaises           TestCase.assertRedirects        
    TestCase.assertTemplateNotUsed  TestCase.assertTemplateUsed     
    TestCase.assertTrue             TestCase.assertNotAlmostEqual   

.. raw:: pdf

  PageBreak simplePage

vamos separar
-------------

.. raw:: pdf

  PageBreak longPage


Asserts básicas
----------------

Essas você deve usar bastante

.. code-block:: python

    TestCase.assertTrue
    TestCase.assertFalse

    TestCase.assertEqual
    TestCase.assertNotEqual

Asserts amigáveis
-----------------

Essas facilitam a vida

.. code-block:: python
    
    TestCase.assertContains
    TestCase.assertNotContains

    def test_welcome(self):
      resp = self.client.get('/welcome/',{})
      self.assertContains(resp, '<h1>Oi</h1>',200)


Asserts amigáveis (cont)
-------------------------

.. code-block:: python
    

    TestCase.assertRedirects
    TestCase.assertTemplateUsed
    TestCase.assertTemplateNotUsed
    TestCase.assertFormError



WTF?
-----------------------

.. code-block:: python

    TestCase.assertAlmostEqual      
                 
    TestCase.assertNotAlmostEqual          

    
.. raw:: pdf

  PageBreak longPage

verifique que não são quase iguais?
-----------------------------------

sério?

Sim
-----------------------------------

.. code-block:: python

    a = 1.21
    b = 1.22
    self.assertAlmostEqual(a,b,2)
    self.assertNotAlmostEqual(a,b,3)

    
.. raw:: pdf

  PageBreak longPage


           
                    
Assets que eu não uso
-----------------------

.. code-block:: python

                        
    TestCase.assertRaises                   


Como testo exceptions
-----------------------

.. code-block:: python

    try:                                                                                                                                                
        foobar.bang():
        self.fail('Bang tem que explodir')                                                                                                          
    except ExplodingException:                                                                                                                                
         pass











.. raw:: pdf

  PageBreak longPage


Testar não é dificil, Voceê só precisa começar
-----------------------------------------------

.. code-block:: python

    referencias

    Tdd em django
    @fractal
    petrich@gmail.com
    creative commons (by) (sa)



Testar não é dificil, Voceê só precisa começar
-----------------------------------------------

.. code-block:: python

    referencias

    Tdd em django
    @fractal
    petrich@gmail.com
    creative commons (by) (sa)

.. header::

        TDD em django sem desculpas

.. footer::

    .. class:: special

    ((cc)  @fractal (by) (nc) (sa))


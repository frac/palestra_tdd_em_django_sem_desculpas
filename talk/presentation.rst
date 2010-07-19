
---------

.. raw:: pdf

  PageBreak simplePage
    
Olá!
----

2 coisas importantes para dizer
--------------------------------

Primeira: Estamos em 2010
----------------------

Segunda: Somos todos adultos
-----------------------------

Somos quase todos adultos
--------------------------

Somos todos quase adultos
--------------------------

.. raw:: pdf

  PageBreak simplePage


Código sem testes é código já quebrado quando foi planejado
  -- Jacob Kaplan-Moss


    
Então, chega de desculpas:
---------------------------

Testar não é dificil, Só precisa começar
-----------------------------------------------


.. raw:: pdf

  PageBreak simplePage


Mas....
----------------------------------


.. raw:: pdf

  PageBreak excusePage


Eu não preciso de testes automatizados
---------------------------------------

.. raw:: pdf

  PageBreak longPage

Ciência da computação é tanto sobre computadores quanto como a astronomia é sobre telescópios
---------------------------------------------------------------------------------------------
 -- E W Dijkstra


Test Driven Development é tanto sobre testes assim quanto a ciência da computação é sobre computadores
------------------------------------------------------------------------------------------------------------

TDD é sobre desenvolvimento e qualidade
----------------------------------------

Código evolve
--------------

Código evolve constantemente
-----------------------------

Se o seu código não tem testes refatorar ele é ou difícil ou um pesadelo
------------------------------------------------------------------------- 

Tranquilidade de refatorar
---------------------------

Felicidade é um código com boa cobertura

.. raw:: pdf

  PageBreak excusePage


Eu nao sei nada sobre testes
-----------------------------------------------



.. raw:: pdf

  PageBreak longPage
    

O ecossistema de testes no python
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

    * Unitários 

    * Funcionais

    * De Regressão

    * Exóticos
     
        * static source analysis
        * smoke test
        * load test

TestRunners
-----------

Mais liberdade de como rolar os testes

    * Padrão

    * nose ou py.test ou outros


Eu uso em 99% das vezes
------------------------

   * Django.test.TestCase
   
   * Unitario

   * Funcional

   * Regressao

   * nose / django-nose




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


Mais Testes, ent�o
---------------------

.. code-block:: bash
    


    ./manage.py startapp forum
    cd forum/

Como eu testo no django
------------------------

.. code-block:: bash

    rm tests.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_topico.py


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




.. raw:: pdf

  PageBreak excusePage
    

Mas TDD é muito lento 
---------------------

e por lento eu quero dizer chato
--------------------------------

.. raw:: pdf

  PageBreak longPage


Continous testing
-----------------


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

  PageBreak longPage



.. code-block:: bash

    $ ./manage.py runtester    

ou ainda 

.. code-block:: bash

    $ ./manage.py runtester forum    



.. raw:: pdf

  PageBreak excusePage
    


Eu começo com tdd mas acabo desistindo no meio
-----------------------------------------------

.. raw:: pdf

  PageBreak simplePage

2 jeitos de comecar com TDD
---------------------------

.. raw:: pdf

  PageBreak longPage


Primeiro: Eu queria ter isso TDD
---------------------------------

Você escreve nos testes a API que voce queria ter


Segundo: SDT
-----------------------

Eu não faço TDD eu faco Stupidity-driven testing. Quando eu faco algo estúpido, eu escrevo um teste para garantir que eu não vou repetir isso de novo
    --titus brown pycon '07


Em suma
-------

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

Essas facilitam a vida para testes funcionais

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


Testar não é dificil, Você só precisa começar
-----------------------------------------------

.. code-block:: python

    referencias

    Tdd em django
    @fractal
    petrich@gmail.com
    creative commons (by) (sa)



Testar não é dificil, Você só precisa começar
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


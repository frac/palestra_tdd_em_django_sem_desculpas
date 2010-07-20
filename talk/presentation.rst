
---------

.. raw:: pdf

  PageBreak simplePage
    
Olá!
----

2 coisas importantes para dizer
--------------------------------

Primeira: Estamos em 2010
--------------------------

Segunda: Somos todos adultos
-----------------------------

Somos quase todos adultos
--------------------------

Somos todos quase adultos
--------------------------

Alguma metodologia de testes você tem que estar usando
-------------------------------------------------------

.. raw:: pdf

  PageBreak simplePage


Código sem testes é código já quebrado quando foi planejado
-----------------------------------------------------------
  -- Jacob Kaplan-Moss


    
Então, chega de desculpas:
---------------------------

Testar não é díficil, Só precisa começar
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


Se o seu código não tem testes refatorar ele é um pesadelo
----------------------------------------------------------

.. code-block:: bash
    
    $ cat  `find . | grep "py$" \
             | grep -v migration` | wc 
    47260  137031 4541546
 

Tranquilidade de refatorar
---------------------------

Felicidade é um código com boa cobertura

.. code-block:: bash

    $ cat  `find . | grep "py$" \
             | grep test` | wc 
    34108   89535 3902868



.. raw:: pdf

  PageBreak excusePage


Eu não sei nada sobre testes
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

    * Outros (load, fuzz..)

TestRunners
-----------

Mais liberdade de como rolar os testes

    * Padrão

    * nose 

    * py.test
    
    * outros


Meu estilo
------------------------

   * Django.test.TestCase
   
   * Unitário (um por modelo)

   * Funcional (um por app)

   * Regressão (um método por erro)

   * nose / django-nose




.. raw:: pdf

  PageBreak excusePage


Eu meio que sei o que é TDD
----------------------------


.. raw:: pdf

  PageBreak longPage


TDD
-------


TDD
-------

Só escreve **código** quando testes falham



TDD
-------

Só escreve **código** quando testes falham

Só escreve **teste** quando testes passam


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

Só escreve código quando testes falham

Só escreve teste quando testes passam



Passou 
--------------------------

Escreve testes


Mais Testes, então
---------------------

.. code-block:: bash
    


    ./manage.py startapp forum
    cd forum/

Meu estilo (v.2)
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
---------------

.. code-block:: python
    

    ./manage.py test

    ------------------------------------
    Ran 0 tests in 0.000s

    OK
    Destroying test database 'default'...    

.. raw:: pdf

  PageBreak longPage

Opa?
-----------
0 testes?

nose
----

Acha testes para você sem que você tenha que por eles no __init__.py

Dá pra chamar o pdb no ponto em que falha ( --pdb-failures) (ou ipdb)


django-nose
-----------

.. code-block:: bash

   $ pip install nose
   $ pip install django-nose

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





Testa de novo
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

Só escreve código quando testes falham

Só escreve teste quando testes passam

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

  PageBreak simplePage

Não quando você se acostuma
-----------------------------

O que me anima a fazer TDD
---------------------------

.. raw:: pdf

  PageBreak longPage

Continous testing
-----------------

Toda vez que você salva um arquivo ele rerola os testes

Não confundir com Continous Integration

test_extensions
---------------

Faz isso para você

Ainda é um pouco tosco

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


Rodando o servidor
---------------------

.. code-block:: bash

    $ ./manage.py runtester    

ou ainda 

.. code-block:: bash

    $ ./manage.py runtester forum    



.. raw:: pdf

  PageBreak excusePage
    


Eu começo com TDD mas acabo desistindo no meio
-----------------------------------------------

.. raw:: pdf

  PageBreak simplePage

2 formas sustentáveis para começar e continuar com TDD
------------------------------------------------------


Primeiro: 
----------

.. raw:: pdf

  PageBreak longPage


TDD:Eu queria ter isso
-------------------------

Você escreve nos testes a API que você queria ter


Eu queria que fosse assim:
-----------------------------------

.. code-block:: bash

     def test_metodos(self):
       topico = Topico()
       self.assertTrue(hasattr(topico, 'titulo'))
       self.assertTrue(hasattr(topico, 'replies'))

Testa
------

.. code-block:: bash

    F.
    =================================================
    FAIL: test_metodos (test_forum.TestForum)
    -------------------------------------------------
    Traceback (most recent call last):
        self.assertTrue(hasattr(topico, 'titulo'))
    AssertionError

    --------------------------------------------------
    Ran 2 tests in 0.002s
    FAILED (failures=1)

Implementa
----------

.. code-block:: python

  class Topico(models.Model):
    """representa um topico"""
    titulo = models.CharField(max_length=64)
  class Resposta(models.Model):
    '''Uma resposta no topico'''
    topico = models.ForeignKey(Topico, 
                     related_name='replies')

Testa
------

.. code-block:: bash
    
    ..
    --------------------------------------------------
    Ran 2 tests in 0.002s

    OK

Prós e Cons
-----------

 * Não é exatamente TDD

 * Funciona
  
 * Mais rápido

 * Você está perdendo cobertura


.. raw:: pdf

  PageBreak simplePage


Segundo: SDT
-----------------------

.. raw:: pdf

  PageBreak longPage


SDT
-----------------------

Eu não faço TDD eu faco Stupidity-driven testing. Quando eu faco algo estúpido, eu escrevo um teste para garantir que eu não vou repetir isso de novo
    --Titus Brown pycon '07


Em suma
-------

Escreve código para solucinar um problema

Se o código quebrar de alguma forma besta

Escreve um teste para isso nunca vai acontecer de novo

goto 10


Prós e Cons
-----------

 * Não é TDD

 * Funciona mas beira Cowboyismo
  
 * Cobertura só sobre o código mais frágil

 * Lembra teste de regressão 



Por que lembra um teste de regressão? 
-------------------------------------

Porque é.

São testes de regressão para você mesmo.

.. raw:: pdf

  PageBreak excusePage
    

Escrever testes é mais complicado que o problema
--------------------------------------------------


.. raw:: pdf

  PageBreak longPage


Longo sim, complicado não
--------------------------

Especialmente longo para testes funcionais

Espera para eu mostrar o django_test_utils, o utlimo bastião dos preguiçosos


.. raw:: pdf

  PageBreak excusePage
    

    
Eu conserto os testes depois
----------------------------

.. raw:: pdf

  PageBreak simplePage

PFFFFFFFFFF!
------------
.. raw:: pdf

  PageBreak longPage


Continous integration
-----------------------

Toda vez que voce comita servidor rola os testes


Hudson
-------
:(


Pony-build
-----------------------------------------

Python!

Não precisa do hudson :)

.. raw:: pdf

  PageBreak excusePage

Agora é tarde demais para TDD, meu projeto já existe
--------------------------------------------------------------

.. raw:: pdf

  PageBreak longPage

Pera! Olha só
-----------------------

    * Testes de Regressão

    * test_utils

Testes de Regressão
-------------------

Garante que um erro que aconteceu nunca mais volte a acontecer

Usado por todos os grandes projetos de software livre

Mesmo você não vai fazer mais nenhuma forma de teste você tem que fazer esta

Testes de Regressão
-------------------

Encontrou um erro escreve um teste que falha por causa do erro

Quando o teste falha corrige o erro


django-test-utils
------------------

Você começa o servidor

.. code-block:: bash

    ./manage.py testmaker -a forum

E navega enquanto ele faz os testes

.. raw:: pdf

  PageBreak excusePage



Mas eu não conheco todas as assertions
----------------------------------------------

.. raw:: pdf

  PageBreak longPage


Bico
-----------------------



Modo mais fácil:
----------------

no ./manage shell

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
      resp = self.client.get('/',{})
      self.assertContains(resp,'<h1>Oi</h1>'
                            ,200)


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

Não quase iguais?
-----------------------------------

.. code-block:: python

    a = 1.21
    b = 1.22
    #sao iguais ate a primeira casa
    self.assertAlmostEqual(a,b,1)
    #diferentes depois da segunda casa
    self.assertNotAlmostEqual(a,b,2)

    
.. raw:: pdf

  PageBreak longPage


           
                    
Assets que eu não uso
-----------------------

.. code-block:: python

                        
    TestCase.assertRaises                   


Testo assim:
-----------------------

.. code-block:: python

    try:                                                                                                                                                
        foobar.bang():
        self.fail('Bang tem que explodir')                                                                                                          
    except ExplodingException:                                                                                                                                
         pass


.. raw:: pdf

  PageBreak simplePage


Testar não é díficil, Você só precisa começar
-----------------------------------------------

Dúvidas?
--------


Referências
-----------

.. code-block:: python

    github.com/ericholscher/django-test-utils
    github.com/ctb/pony-build

    Tdd em django sem desculpas
    @fractal
    petrich@gmail.com
    creative commons (by) (sa)




.. header::

        TDD em django sem desculpas

.. footer::

    .. class:: special

    ((cc)  @fractal (by) (nc) (sa))


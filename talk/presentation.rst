
---------

.. raw:: pdf

  PageBreak longPage
    

Código sem testes é código já quebrado quando foi planejado
-----------------------------------------------------------

    -- Jacob Kaplan-Moss 

    um dos criadores do django

Estamos em 2010
--------------------------


.. raw:: pdf

  PageBreak imagePage
    
2010 > 1960
--------------

.. image:: images/2550229291_d3af218c74_b.jpg
    :width: 590px

2010 > 1999
--------------

.. image:: images/3528603529_c8c948638b_o.jpg
    :width: 590px

.. raw:: pdf

  PageBreak longPage

Alguma buzzword "ágil" você tem que estar usando
-------------------------------------------------------

    
Buzzwords são quintessenciais 
------------------------------
Buzzwords trazem sinergia viral e o empowerment das melhores práticas para a cauda longa



3 anos atrás
-------------

equipe:  >40 pessoas numa mesma sala

escopo: Webapp em Tomcat

buzzwords: Bodyshop típico: cmms.. (< 1999)


2.5 anos atrás
-----------------

equipe:  5 pessoas espalhadas pelo mundo

escopo: Modificações no nível de uma distro

buzzwords: Scrum, cultura de testes, sprints, entregas semanais 


.. raw:: pdf

  PageBreak simplePage

5 > 40 
-----------------------

.. raw:: pdf

  PageBreak longPage

Metodologias ágeis:
-------------------

Extreme Programing(XP)

Scrum

Kanban

Feature Driven Develelopment (FDD)


Práticas ágeis:
---------------

Test Driven Development (TDD)

Behavior Driven Development (BDD)

Code refactoring

Continuous Integration

Pair Programming

Planning poker


.. raw:: pdf

  PageBreak simplePage

TDD
----

Sustentável

Fácil

Não depende da gerência



    

TDD não é díficil. Díficil é não fazer quando voce acostuma
------------------------------------------------------------


.. raw:: pdf

  PageBreak simplePage


    
Então, chega de desculpas:
---------------------------


.. raw:: pdf

  PageBreak excusePage


Eu não sei nada sobre testes
-----------------------------------------------



.. raw:: pdf

  PageBreak longPage
    

O ecossistema de testes no python
-----------------------------------

* Tipos

* Sabores

* TestRunners


.. raw:: pdf

  PageBreak longPage



Tipos de testes
---------------

Doctest 
-------

.. code-block:: python

    def add(a,b):
      """
      testa a soma
      >>> add(1,2)
      3
      """
      return a + b


Unittest
--------


unittest.TestCase 
        
django.test.TestCase


django.test.TestCase
--------------------

.. code-block:: python

    from django.test import TestCase
    
    class SimpleTest(TestCase):
      def test_adicao(self):
        """
        Testa que a adicao de 1 + 1 da 2.
        """
        self.assertEqual(1 + 1, 2)

Sabores de testes
------------------------------

Unitários 
----------
Nível de função

.. code-block:: python

    self.assertTrue(add(1,2),3)


Integração
----------
Entre Módulos

.. code-block:: python

    r = self.client.get('/foo')
    self.assertRedirects(r,'/login/')
    self.client.login(user_name='foo'
                          ,password='bar')
    r = self.client.get('/foo')
    self.assertEquals(r.status_code,200)
    

De Regressão
-------------

Correção de erros


TestRunners
-----------

Acha e Roda os testes

    * Padrão

    * py.test
    
    * nose 

    * outros


Meu estilo
------------------------

   * Django.test.TestCase
   
   * Unitário 
        Um TestCase por modelo
        
        Um ou mais testes por função

   * Integração 
        Um por TestCase por conjunto de apps

   * Regressão 
        Um teste por erro

   * nose / django-nose
        Acha testes



.. raw:: pdf

  PageBreak excusePage


Eu não preciso de testes automatizados
-------------------------------------------


.. raw:: pdf

  PageBreak longPage

Código evolve 
-----------------------------


Se o seu código não tem testes refatorar ele é um pesadelo
----------------------------------------------------------


Imagina isso 
-------------

.. code-block:: bash
    
    $ cat  `find . | grep "py$" \
             | grep -v migration` | wc -l
    47260 
      
Agora isso:
-----------

.. code-block:: bash

    $ cat  `find . | grep "py$" \
             | grep test` | wc -l 
    34108


Tranquilidade de refatorar
---------------------------

Felicidade é um código com boa cobertura



.. raw:: pdf

  PageBreak excusePage


Eu meio que não sei o que é TDD
--------------------------------


.. raw:: pdf

  PageBreak longPage


Ciência da computação é tanto sobre computadores quanto como a astronomia é sobre telescópios
---------------------------------------------------------------------------------------------
 -- E W Dijkstra


Test Driven Development é tanto sobre testes assim quanto a ciência da computação é sobre computadores
------------------------------------------------------------------------------------------------------------

TDD é sobre desenvolvimento e qualidade
----------------------------------------

Testes são um subproduto
-------------------------


TDD
-------


TDD
-------

Só escreve **código** quando testes falham



TDD
-------

Só escreve **código** quando testes falham

Só escreve **testes** quando testes passam


.. raw:: pdf

  PageBreak excusePage
    


Eu nunca fiz muitos testes no Django
------------------------------------

.. raw:: pdf

  PageBreak longPage

Como fazer: Instala o django
-----------------------------

.. code-block:: bash

    $ easy_install pip
    $ pip install django


Cria o projeto
---------------

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
    DATABASES = {'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/foobar.db', } }

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

Só escreve **código** quando testes falham

Só escreve **testes** quando testes passam



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
    touch tests/test_models.py


vi tests/test_models.py
------------------------

.. code-block:: python

    #coding:utf8
    from django.test import TestCase                                                                                                                            
                                                                                                                                                                
    class ModelTest(TestCase):                                                                                                                                  


Teste de importação
------------------------

.. code-block:: python

    def test_existe(self):                                                                                                                          
      """ O topico esta la? """                                                                                                                                                 
      try:                                                                                                                                                
        from foobar.forum.models import Topico                                                                                                         
      except ImportError:                                                                                                                                
        self.fail('Nao existe topico') 


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

0 testes!
---------

nose
----

Acha testes para você sem que você tenha que por eles no __init__.py

Dá pra chamar o pdb no ponto em que falha ( --pdb-failures) (ou ipdb)


django-nose
-----------

.. code-block:: bash

   $ pip install nose
   $ pip install django-nose
   $ pip install NoseNotify #opcional

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
    NOSE_ARGS = [ '--with-notify',
        #'--pdb-failures',
    ]





Testa de novo
------------------------

.. code-block:: python

    F
    ====================================
    FAIL: O topico esta la?
    ------------------------------------
    Traceback (most recent call last):
      File "test_models", line 18, in test_existe
        self.fail('Nao existe topico')
    AssertionError: Nao existe topico
    ------------------------------------
    Ran 1 test in 0.003s


TDD
-------

Só escreve **código** quando testes falham

Só escreve **testes** quando testes passam

Falhou
--------------------------

Escreve código 

vi forum/models.py
--------------------

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

A primeira vez é lento
-----------------------

.. raw:: pdf

  PageBreak longPage


Entenda o que você esta testando
---------------------------------

.. code-block:: python

      try:                                                                                                                                                
        from foobar.forum.models import Topico                                                                                                         
      except ImportError:                                                                                                                                
        self.fail('Nao existe topico') 

Não teste a framework
------------------------------------

Teste a **lógica da sua** applicação

.. raw:: pdf

  PageBreak simplePage


Facilitadores
---------------------------

.. raw:: pdf

  PageBreak longPage

Continous testing
-----------------

Toda vez que você salva um arquivo ele rerola os testes


django test extensions
-----------------------

Faz isso para você

Ainda é um pouco tosco

.. raw:: pdf

  PageBreak longPage


django-test-extensions
-----------------------

.. code-block:: bash

    $ pip install django-test-extensions    



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


Automagicamente
-----------------------------------------------------------

.. code-block:: bash

    nosetests --verbosity 1 --with-notify forum
    .....
    -------------------------------------------
    Ran 5 tests in 0.457s

    OK
    Destroying test database 'default'...
    Creating test database 'default'...


Bonus combo
------------

django-test-extensions com NoseNotify

    .. image:: notify.png
       :width: 80%


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

no ./manage shell (com ipython instalado)

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

    assertTrue(True)
    assertFalse(False)

    assertEqual(1,1)
    assertNotEqual(1,2)

Asserts amigáveis
-----------------

Essas facilitam a vida para testes funcionais

.. code-block:: python
    
    assertContains(response,texto,status)
    assertNotContains(response,texto,status)
    
exemplo
------------------

.. code-block:: python
        
    def test_welcome(self):
      resp = self.client.get('/',{})
      self.assertContains(resp,'<h1>Oi</h1>'
                            ,200)


Asserts amigáveis (cont)
-------------------------

.. code-block:: python
    

    assertRedirects(response,nova_url)
    assertTemplateUsed(response,template)
    assertTemplateNotUsed(response,template)
    assertFormError(response,form,fields,errors)



WTF?
-----------------------

.. code-block:: python

    assertAlmostEqual      
                 
    assertNotAlmostEqual          

    
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


           
                    
Asserts que eu não uso
-----------------------

.. code-block:: python

                        
    assertRaises                   


Testo assim:
-----------------------

.. code-block:: python

    try:                                                                                                                                                
        foobar.bang():
        self.fail('Bang tem que explodir')                                                                                                          
    except ExplodingException:                                                                                                                                
        pass


.. raw:: pdf

  PageBreak excusePage

Agora é tarde demais para TDD, meu projeto já existe
--------------------------------------------------------------

.. raw:: pdf

  PageBreak longPage

Pera! Olha só
-----------------------

    * Testes de Regressão
    
    * django_test_utils


Seu melhor amigo
-------------------

Garante que um erro que aconteceu nunca mais volte a acontecer

Usado por todos os grandes projetos de software livre

Mesmo você não vai fazer mais nenhuma forma de teste você tem que fazer esta

Testes de Regressão
-------------------

Encontrou um erro 
------------------

.. code-block:: python

  [24/Jul/2010 11:14:51] "GET / HTTP/1.1" 404 1946

Escreve um teste que falha por causa do erro
---------------------------------------------

.. code-block:: bash

   $ vi forum/test_regression.py


cont
-----

.. code-block:: python
    
    #coding:utf8
    from django.test import TestCase

    class TestRegression(TestCase):
        """testes de regressao"""


cont+=1
--------

.. code-block:: python

    def test_regress_home(self):
      """Home precisa existir"""
      r = self.client.get('/', {})
      self.assertEqual(r.status_code, 200)
 

Testa e falha
---------------------------

.. code-block:: python

    ..E
    ================================================
    ERROR: Home precisa existir
    ------------------------------------------------
    Traceback (most recent call last):
      File "foobar/forum/tests/test_regresssion.py", 
                    line 10, in test_regress_home
        r = self.client.get('/', {})
       ...
        raise TemplateDoesNotExist(name)
    TemplateDoesNotExist: 404.html



Corrige o erro
--------------


.. code-block:: python

    from django.views.generic.simple import direct_to_template
    urlpatterns = patterns('',
        ...
        (r'^$', direct_to_template, {'template': 'index.html'}),
        ...
    )

.. code-block:: bash

   $ vi templates/index.html

Roda os testes e passa
----------------------

.. code-block:: python

    nosetests --verbosity 1
    ....
    -----------------------
    Ran 4 tests in 0.025s

    OK



Garantia que erros antigos não vão retornar para te assombrar
--------------------------------------------------------------



.. raw:: pdf

  PageBreak excusePage
    


Toda vez que eu começo com TDD mas acabo desistindo no meio
------------------------------------------------------------

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

django_test_utils, o utlimo bastião dos preguiçosos


django-test-utils
------------------

.. code-block:: bash

    $ pip install django-test-utils

settings.py
-----------

.. code-block:: python
    
    INSTALLED_APPS = (
        ...
        'south', # migracoes
        'django_nose', # depois do south 
        'test_extensions', # depois do south
        'test_utils', # depois do south
        ...
    )



Você começa o servidor
----------------------

.. code-block:: bash

    $ ./manage.py testmaker -a forum


Cria testes para você
---------------------------------


.. code-block:: bash

    Handling app 'forum'
    Logging tests to foobar/forum/tests/forum_testmaker.py
    Appending to current log file
    Inserting TestMaker logging server...
    Validating models...
    0 errors found

    Django version 1.2.1, using settings 'foobar.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.



Quando você termina
---------------------------------

.. code-block:: bash

    $ cd forum/tests
    $ ls forum*
    forum_testdata.serialized  
    forum_testmaker.py  



Testes gerados
---------------------------------

.. code-block:: python

    def test_forum_127958317459(self):
      r = self.client.get('/forum/', {})
      self.assertEqual(r.status_code, 200)
      self.assertEqual(
        unicode(r.context["paginator"]), u"None")
      self.assertEqual(
        unicode(r.context["object_list"]), 
          u"[<Topico: Topico object>, <Topico: Topico object>]")
      .....


.. raw:: pdf

  PageBreak excusePage
    
.. raw:: pdf

  PageBreak excusePage
    

Não, não! Escrever testes é mais complicado que o problema, mesmo!
------------------------------------------------------------------------------



.. raw:: pdf

  PageBreak simplePage

Mocks e Stubs
---------------

Minta descaradamente para seu código
------------------------------------

.. raw:: pdf

  PageBreak longPage


Imagina algo assim:
-------------------

.. code-block:: python
    
    def calcula_queijo(request):
        sanduba = request.session["sanduba"]
        ....

Não perca tempo
----------------------------------------

Colocar algo no session do request em um test case é chato



Hora de mockear
----------------

Existem muitas ferramentas de mock para python

Escolha uma e vai fundo.

Não esqueça de RTFM

Eu uso o fudge

Instalar e usar
----------------

.. code-block:: bash

   pip install fudge
    
Seu teste
----------

.. code-block:: python

    import fudge
    ...
      def teste(self)
        request = fudge.Fake().has_attr(
                  session={'sanduba': Sanduba() })
        calcula_queijo(request)
        

.. raw:: pdf

  PageBreak excusePage

    
Eu conserto os testes depois
----------------------------

.. raw:: pdf

  PageBreak simplePage

PFFFFFFFFFF!
------------



.. raw:: pdf

  PageBreak simplePage


TDD não é díficil. Díficil é não fazer quando voce acostuma
-------------------------------------------------------------

Créditos
--------

.. code-block:: python

    http://www.flickr.com/photos/blue-moose/3528603529

Dúvidas?
--------

Agradecimentos
---------------

http://associacao.python.org.br/

Nos vemos na PythonBrasil[6] em Curitiba 

Outubro 21 a 23 

Referências
-----------

.. code-block:: python

    http://code.google.com/p/python-nose/
    http://github.com/jbalogh/django-nose
    http://github.com/garethr/django-test-extensions
    http://github.com/ericholscher/django-test-utils
    http://github.com/ctb/pony-build

    Tdd em django sem desculpas
    @fractal
    petrich@gmail.com
    creative commons (by) (sa)




.. header::

        TDD em django sem desculpas

.. footer::

    .. class:: special

    ((cc)  @fractal (by) (nc) (sa))


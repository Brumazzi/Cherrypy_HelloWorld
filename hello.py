#!/usr/bin/env python2
# *-* coding:utf-8 *-*

import cherrypy
from route import Route

# instancia das rotas
route = Route()

# classe da aplicação principal
class Hello(object):
    def __init__(self):
        # gerando as rotas
        # "Arquivo" + "Caminho" + "Apelido"
        route.new_route('index.html','html/','index')
        route.new_route('dependence.html','html/','dependence')

    def index(self):
        # recolhe e retorna a rota
        # passando o apelido para a busca
        return route.call('index')

    def home(self):
        # recolhe e retorna a rota
        # passando o apelido para a busca
        return route.call('dependence')

    # "metodo.exposed = True"
    # Faz com que seja possivel visualizar a página
    # caso seja "False", a página não aparece
    index.exposed = True
    home.exposed = True

# Inicia o servidor
cherrypy.quickstart(Hello())

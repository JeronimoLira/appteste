# Qualquer projeto com kivy, onde o App será usado no celular, se for fazer requisição https, que é o caso de todos os links 
# firebase, é necessário importar "os" e "certifi", ou seja, em outras palavras: essas bibliotecas são necessárias sempre que 
# precisarmos fazer requisiçoes (requests) https. 
import requests
import os
import certifi

import kivy
from telas import *
from tl_botoes import *
from kivy.app import App
from kivy.lang import Builder

os.environ["SSL_CERT_FILE"] = certifi.where()

GUI = Builder.load_file("main.kv")
class MainApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_start(self):
            pass

    def build(self):        
        return Builder.load_file("main.kv")


MainApp().run()
    
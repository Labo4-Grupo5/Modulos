# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:04:33 2016

@author: Alejandro
"""

from scipy import signal
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib import animation

class Diccionario(dict):
    def __getattr__(self, nombre):
        return self[nombre]

    def __setattr__(self, nombre, valor):
        self[nombre] = valor

class Experimento(object):
    def __init__(self, nombre='Sin título',descripcion = '-',
                 **parametros):
        self.nombre = nombre
        self.descripcion = descripcion
        self._parametros = Diccionario(parametros)
        self._datos = Diccionario()
        self._imagenes = Diccionario()
    
    def listar_parametros(self):
        params = sorted(self.parametros)
        print('Pámetros generales:')
        print('---------------------------------------')
        for param in params:
            print(param, ':', self.parametros[param])            
        print('----------------------------------------')
        
    def listar_archivos(self):
        pass

    def guardar_experimento(self, nombre='log.txt'):        
        pass
    
    def cargar_experimento(self, nombre='log.txt'):
        pass
    
    def guardar_datos(self, datos, nombre='temp.csv', **params):        
        pass
    
    def cargar_datos(self, nombre='temp.csv'):       
        pass
    
    def guardar_imagen(self, imagen, nombre='temp.jpg', **params):
        pass
    
    def cargar_imagen(self, nombre='temp.jpg'):
        pass        
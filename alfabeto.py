import json
from tkinter import N

my_json_string = """{
   "alfabeto": [

      {
         "id": 1,
         "letra":"a"
      },

      {
         "id":2,
         "letra":"b"
      },

      {
         "id": 3,
         "letra":"c"
      },

      {
         "id":4,
         "letra":"d"
      },

      {
         "id":5,
         "letra":"e"
      },

      {
         "id":6,
         "letra":"f"
      },
      {
         "id": 7,
         "letra":"g"
      },

      {
         "id":8,
         "letra":"h"
      },

      {
         "id": 9,
         "letra":"i"
      },

      {
         "id":10,
         "letra":"j"
      },

      {
         "id":11,
         "letra":"k"
      },
      {
         "id": 12,
         "letra":"l"
      },

      {
         "id":13,
         "letra":"m"
      },

      {
         "id": 14,
         "letra":"n"
      },

      {
         "id":15,
         "letra":"o"
      },

      {
         "id":16,
         "letra":"p"
      },
            {
         "id":17,
         "letra":"q"
      },

      {
         "id": 18,
         "letra":"r"
      },

      {
         "id":19,
         "letra":"s"
      },

      {
         "id":20,
         "letra":"u"
      },
      {
         "id": 21,
         "letra":"v"
      },

      {
         "id":22,
         "letra":"w"
      },

      {
         "id": 23,
         "letra":"x"
      },

      {
         "id":24,
         "letra":"y"
      },
            {
         "id":25,
         "letra":"z"
      }
   ]
}
"""
to_python = json.loads(my_json_string)

#-----------------------------------------------------------------------------------
alfabeto = to_python["alfabeto"]

timer_geral = 0
numero_repetiçao = 1
print("selecione um numero de 1 a 25")
grid_lados = int(input())
limite_grid = 0
lista_letras_1 = []
repetiçao_geral = 0
repetiçao_na_lista = 1

def localizar_letras(numero_repetiçao):
   for letras in alfabeto:
         if numero_repetiçao == letras['id']:
            lista_letras_1.append(letras['letra'])
            numero_repetiçao += 1

            


while timer_geral < grid_lados:
   
   localizar_letras(1 + repetiçao_geral)
   timer_geral += 1
   while len(lista_letras_1) < 25:
      for letra_repetiçao in alfabeto:
         if repetiçao_na_lista == letra_repetiçao['id']:
            lista_letras_1.append(letra_repetiçao['letra'])
      repetiçao_na_lista += 1
   
   repetiçao_na_lista = 1
   print(lista_letras_1)
   lista_letras_1 = []
   repetiçao_geral = repetiçao_geral + 1



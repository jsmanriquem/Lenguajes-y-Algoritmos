# -*- coding: utf-8 -*-
"""Número primo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b5ImRi2-YyBpTp393udwwRryzSwDS1ZM
"""

def primo(n):
  if n==1:
    return False
  for x in range(2, n):
    if n % x ==0:
      return False
    return True

cant=0
n=2
lim=float(input("escribir la cantidad de números primos que desea ver en panatalla:  "))

while lim > cant:
  if primo(n) :
    cant +=1
    print(cant, n)

  n +=1
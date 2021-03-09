# -*- coding: utf-8 -*-


# importação das bibliotecas matplotlib (gráficos)
# e numpy (arrays)
import matplotlib.pyplot as plt
import numpy as np

# definição das funções
def f(x):
  return (np.power(x,2)+x-6)

def g1(x):
  return (6 - np.power(x,2))

def g2(x):
  return (np.sqrt(6 - x))

# intervalo de x e o passo
x = np.arange(-4.0, 4.0, 0.01)

# exibição dos gráficos
plt.figure()
plt.subplot(211)
plt.grid()
plt.plot(x, f(x),'r-',label='f(x)')
plt.plot(x, g1(x),'g--',label='g1(x)')
plt.legend()

plt.subplot(212)
plt.grid()
plt.plot(x,f(x),'r-',label='f(x)')
plt.plot(x,g2(x),'b-.',label='g2(x)')
plt.legend()
plt.show()

# estudo da convergência das duas funções
print('\n')
print("Função g1")
xk = 1.5
for i in range(0,5):
  print("x",i," = ",xk)
  xk = g1(xk)

print('\n')
print("Função g2")
xk = 1.5
for i in range(0,5):
  print("x",i," = ",xk)
  xk = g2(xk) 

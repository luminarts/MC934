import matplotlib.pyplot as plt
import math 
import numpy as np

def softplus(x):
  return np.log(1+np.exp(x))

def softplus_1st_derivative(x):
  return (np.exp(x)/(1 + np.exp(x)))

def tangent(x, x0):
  return softplus(x0) + softplus_1st_derivative(x0) * (x - x0)

def limite_quadratico_superior(x, x0):
  return tangent(x, x0) + L/2 * (x - x0)**2

x = np.linspace(-4, 5, num=20)
x0 = np.array([1])
L = 0.25


plt.plot(x, softplus(x), label='f(x)')

plt.plot(x, tangent(x, x0), color='red', label='Tangente em x0')

plt.plot(x, limite_quadratico_superior(x, x0), color='purple', label='Limite quadrático superior')

plt.scatter(x0, softplus(x0), color='red', label='Ponto x0')

plt.xlim([-4, 4])


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Função Softplus')
plt.legend()
plt.show()
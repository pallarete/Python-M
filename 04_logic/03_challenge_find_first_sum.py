"""
Dado un array de números y un número goal, encuentra los dos 
primeros números del array que sumen el número goal y devuelve
sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
import os
os.system('cls')
# Vale aqui guia las iteraciones marcando la longitud de la misma
# gracias a los rangos
nums = [4,5,6,2]
goal = 8
def encuentra_sumatoria(nums, goal):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == goal:
        return [i, j]  
  return None # no se encontro ninguna combinacion

nums = [4,5,6,2]
goal = 8
resultado = encuentra_sumatoria(nums, goal)
print(resultado)
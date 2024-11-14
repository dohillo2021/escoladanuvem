#calculo da distância entre dois pontos
#distancia = raiz de (x2 - x1) **2 + (y2 - y1) **2

import math

x1, y1 = map(float, input("Digite as coordenadas x1 e y1: ").split())
x2, y2 = map(float, input("Digite as coordenadas x1 e x2: ").split())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")
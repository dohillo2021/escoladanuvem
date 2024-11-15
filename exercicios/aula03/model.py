from sklearn.linear_model import LinearRegression
import numpy as np

horas_estudo = np.aray([1,2,3,4,5]).reshape(-1,1)
notas = np.array([40,50,60,70,80])

#Modelo treina
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)

#Pergunto ao usuário final
horas = float(input("Digite o número de horas estudadas: "))

#Previsão de horas
nota_prevista = modelo.predict([[horas]])

print(f"Com {horas} de estudo, a nota prevista é {nota_prevista[0]:.2f}")


#Esse código verifica a idade se é maior de idade, se é adolescente ou se é uma criança

idade = int(input("Digite a sua idade: "))

#Se a idade da pessoa for maior que 18 anos ela é maiuor de idade
if idade >= 18:
    print("Você é amior de idade")

#Se a idade de pessoa for maior que 12 anos e menor que 18 anos é adolescente
elif 12 <= idade < 18:
    print("Você é adoelescente")

#Se não for nenhuma dessas é uma criança

print("Você é uma criança")

#Utilizamos estrutura de controle. o modelo de ML ele nasce através de ifs e else
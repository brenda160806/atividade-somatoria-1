#1.receber a variavel peso {float}
peso = float (input('digite o seu peso: '))

#2.receber a variavel altura {float}
altura = float(input('digite a sua altura: '))

#.3 realizar o calculo de imc = (peso / altura) 
imc = (peso / (altura ** 2))

#4. imprimir o resultado do imc
print(f' oseu indicie de massa corporea: {imc:.2f}')
 #operacaoes usadas : divisao (/) e potencia (**)

 #classifica o imc e exibw a mensagem correspondente
if imc < 18.5:
    print("classificacao: abaixo do peso")
    print("orientacao: e importante buscar orientacao medica para avaliar sua saude nutricional.")
elif 18.5 <= imc <= 24.9:
    print("classificacao: peso normal")
    print("orientacao: parabens! seu peso esta dntro da faixa considerada saudavel.")
elif 25 <= imc <= 29.9:
    print("classificacao: obesidade grau 1")
    print("orientacao:e importante procurar orientacao medica para avaliar opcoes de tratamento e adotar mudancas no estilo de vida.")
elif 35<= imc <= 39.9:
    print("classificao: obesidade grau 2")
    print("orientacao: procure um profissional de saude para uma avaliacao completa e orientacoes adequadas. ")
else:
    print("classificacao: obesidade grau 3 (morbida)")
    print("orientacao: busque acompanhamento medico especializado para um plano de tratamentopersonalizado..")

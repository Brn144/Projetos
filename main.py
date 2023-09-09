'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n1 = float(input("Digite o primeiro numero: ")) 

n2 = float(input("Digite o segundo numero: ")) 

soma = n1 + n2 

subtracao = n1 - n2 

divisao = n1 / n2 

multiplicacao = n1 * n2

potencia = n1 ** n2

operacao = str(input("Qual operação você deseja fazer? <+, -, /, *, **> ")) 



if operacao == "+": 
    print("O resultado de {} {} {} = {:.2f}".format(n1, operacao, n2, soma))  

elif operacao == "-":
    print("O resultado de {} {} {} = {}".format(n1, operacao, n2, subtracao)) 
    
elif operacao == "/":
    print("O resultado de {} {} {} = {}".format(n1, operacao, n2, divisao)) 
    
elif operacao == "*":
    print("O resultado de {} {} {} = {}".format(n1, operacao, n2, multiplicacao)) 

elif operacao == "**":
    print("O resultado de {} {} {} = {}".format(n1, operacao, n2, potencia))
    
else:
    print("Error")


 
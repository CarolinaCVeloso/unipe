salario = float((input("Qual o salário que será reajustado? ")))

if salario >= 500 and salario <=1500 :
    print("O salário reajustado é: " + str(salario * 1.40))
elif salario >=1501 and salario <=2500:
    print("O salário reajustado é: " + str(salario * 1.50))
elif salario >=2501 and salario <=3000:
    print("O salário reajustado é: " + str(salario * 1.60))
else:
    print("Salario não se encaixa!!")

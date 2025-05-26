nome=input("escreva seu nome")
peso=float(input("escreva sua peso"))
altura=float(input("escreva sua altura"))
IMC= peso / (altura*altura)
print(IMC)
if IMC<=18.5:
    print("abaixo do pesso")
elif IMC>=19.5 and  IMC <=24.9:
    print(f"pesso normal  {IMC}  ✅ Tudo ok")
elif IMC>=25.0 and IMC <=29.9:
    print(f"sobrepeso {IMC} ⚠️Cuidado com a Saúde ")
elif IMC>=30.0 and IMC <=34.9:
    print(f"obesidade grau 1 {IMC} ⚠️Cuidado com a Saúde ")
elif IMC>=35.5 and IMC <=39.9:
    print(f"obesidade grau 2  {IMC} ⚠️Cuidado com a Saúde")
else: 
    print(f"obesidade grau 3  {IMC} ⚠️Cuidado com a Saúde") 
 


print(f"Seu nome {nome} seu imc é: {IMC}")
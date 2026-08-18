idade = int(input("Quantos anos você tem? "))

if idade < 18 :
    print("Você é maior de idade.")
    
elif idade >= 18 and idade < 60:
    print ("Você é adulto.")
    
elif idade > 15:
    print ("você é menor de idade.")
    
elif idade == 60:
    print ("Feliz aniversário.")
    
else:
    print("Você é um idoso.")
    

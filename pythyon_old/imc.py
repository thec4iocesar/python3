#IMC = PESO / (ALTURA * ALTURA)

peso = 75
altura = 1.67

imc = (peso)/(1.67*1.67)

print ('seu imc e')
print (imc)
print ('de acordo com nossos especialistas, voce...')

if imc <= 18.5:
        classificacao_de_gordice='esta muito magro'
elif imc <= 24.9:
        classificacao_de_gordice='esta no shape'
elif imc <= 29.9:
        classificacao_de_gordice='possui tetas'
elif imc <= 34.9:
         classificacao_de_gordice='esta gordito'
elif imc <= 39.9:
        classificacao_de_gordice='esta obeso'
else:
      classificacao_de_gordice='esta em Stewy Mode, vai morrer'
	  
print (classificacao_de_gordice)

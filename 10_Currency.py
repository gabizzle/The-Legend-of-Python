# Currency

pesos = int(input("Enter amount in pesos: "))
soles = int(input("Enter amount in soles: "))
reais = int(input("Enter amount in reais: "))

pesos_usd = pesos * 0.055
soles_usd = soles * 0.26
reais_usd = reais * 0.22

total = pesos_usd + soles_usd + reais_usd

print(total)
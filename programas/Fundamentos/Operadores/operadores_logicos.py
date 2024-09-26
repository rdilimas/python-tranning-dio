#uma sequencia do tipo lista ou str em python é conciderada false
contatos_emergencia = []

x = not 1000 > 1500

print(x)

y = not contatos_emergencia
print(y)

z = not "saque 1500;"
print(z)

w = not ""
print(w)



##########################

saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print("Autoriza Saque: " , exp)

exp_2 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print("Autoriza Saque 2: " , exp_2)
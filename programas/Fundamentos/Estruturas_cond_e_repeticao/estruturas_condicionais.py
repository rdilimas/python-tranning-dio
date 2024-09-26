MAIOR_IDADE    = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade: "))

####if's
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH.")

#### if, else
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Menor de idade, não pode tirar a CNH.")    

#### if, elif, else
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer apenas as aulas tericas.")
else:
    print("Menor de idade, não pode tirar a CNH.")    


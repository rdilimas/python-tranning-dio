nome = "Robson"
idade = 34
profissao = "Programador"
linguagem = "Python"


#Old Style -- caiu em desuso... 
print("Olá, meu chamo %s. Eu tenho %d anos de idade," 
      " trabalho como %s e estou matriculado no curso de %s." % 
      (nome, idade, profissao, linguagem))


#Metodo Format
print("Olá, meu chamo {}. Eu tenho {} anos de idade," 
      " trabalho como {} e estou matriculado no curso de {}."
      .format(nome, idade, profissao, linguagem))


#Metodo Format 2
print("Olá, meu chamo {3}. Eu tenho {2} anos de idade," 
      " trabalho como {1} e estou matriculado no curso de {0}."
      .format(linguagem, profissao, idade, nome))

#Metodo Format 3
print("Olá, meu chamo {nome}. Eu tenho {idade} anos de idade," 
      " trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#Metodo Format 4
pessoa = {"nome": "Robson", "idade": 34, "profissao" : "Programador", "linguagem" : "Python" }
print("Olá, meu chamo {nome}. Eu tenho {idade} anos de idade," 
      " trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(**pessoa))


#f-string
print(f"Olá, meu chamo {nome}. Eu tenho {idade} anos de idade, " 
      f"trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

#s-string formatando com duas casas decimais
print(f"Valor de PI: {PI:.2f}")

#tamanho total de 10 com duas casas decimais
print(f"Valor de PI: {PI:10.2f}")




nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
INSS = salario * 0.08
salarioLiquido: salario - INSS
print (f"\nnome: {nome}")
print (f"Salário Bruto: R$ {salario:.2f}")
print (f"INSS: R$ {INSS:.2f}")
print (f"Salário Líquido: R$ {salarioLiquido:.2f}")
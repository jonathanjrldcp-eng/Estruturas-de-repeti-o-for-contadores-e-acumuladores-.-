import os
# ACUMULADOR
soma = 0
for i in range(1, 5):
    soma += i
    print(f"Valor de i: {i} | Soma acumulada: {soma}")

input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

aprovados = 0
for nota in range(4):
    if nota >= 2:
        aprovados += 1
print(f"Número de aprovados: {aprovados}")

input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

contador = 0
for i in range(1, 11):
    if i % 2 == 0:
        contador += 1
print(f"Número pares entre 1 e 10: {contador}")

input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

# CONTADOR
soma = 0
for i in range(1, 4):
    soma += i
print(f"Soma acumulada: {soma}")

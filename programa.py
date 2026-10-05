from funcao import media
print("um programa que calcula notas")
print()

nota1 = float(input("insira a primeira nota com peso 2: "))
nota2 = float(input("insira a segunda nota com peso 3: "))
nota3 = float(input("insira o valor da terceira nota com peso 5: "))

media = media(nota1, nota2, nota3)

print("")
print(f"a media das notas e igual a: {media:.2f} ")
ano = 2000

ano = int(input("Enter a year: "))

if (ano % 400 == 0) and (ano % 100 == 0):
    print("{0}é um ano bissexto.format(ano)")

elif(ano % 4 == 0) and (ano % 100 != 0):
    print("{0}é um ano bissexto.format(ano)")

else:

    print("{0}não é um ano bissexto.format(ano)")
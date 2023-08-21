saudacao =input("Indique a saudação: Oi, E aí, Olá:")

pessoa = input("Indique a pessoa cumprimentada: ")

if (pessoa == "Camila Spakauskas"):
  print(saudacao + "," + pessoa + "! Você é aluna da faculdade Descomplica!")
else:
    print(saudacao + "," + pessoa + "!Você é professor da faculdade Descomplica!");

    with open('nomes_saudados.txt', 'a') as f:
      f.write("\n" + pessoa)
    f.close()
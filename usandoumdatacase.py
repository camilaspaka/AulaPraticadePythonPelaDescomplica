
#falta o arquivo mas o professor não disponibilizou no material de apoio
#encontrei o arquivo mas esse exercicio é apenas para google colab, lame

lines = []
with open('Churn_Modelling.csv') as f:
  lines = f.readlines()

  count = 0
  for line in lines:
    count += 1
    print(f'{line}')

    #a forma que o professor ensinou a fazer não é gerada no Visual Studio mas assim funciona tranquilamente no google colab
dc = id.read_csv("Churn_Modelling.csv")
dc.head(5)

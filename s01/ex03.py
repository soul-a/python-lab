def main():
  n1 = float(input("Digite a sua nota do 1º bimestre: "))
  n2 = float(input("Digite a sua nota do 2º bimestre: "))
  n3 = float(input("Digite a sua nota do 3º bimestre: "))
  n4 = float(input("Digite a sua nota do 4º bimestre: "))

  media = (n1 + n2 + n3 + n4) / 4

  if media > 5:
    print("Ano passou com média de {}".format(media))
  else:
    print("Aluno não passou com média de {}".format(media))

main()
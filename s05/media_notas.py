def main():
  n1 = float(input("Digite a primeira nota:").replace(",", "."))
  n2 = float(input("Digite a segunda nota:").replace(",", "."))
  media = (0.4 * n1) + (0.6 * n2)

  if(media >= 5.0):
    print(f"Você foi aprovado com {round(media, 2)} de média, parabéns!!!")
  else:
    print("Infelizmente você foi reprovado!! :(")

main()
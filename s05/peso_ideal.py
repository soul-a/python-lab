def calcula_imc(altura: float, sexo: str) -> float:
  result = 0.0;
  if (sexo.upper() == "M"):
    result = (72.7 * altura) - 58
  else:
    result = (62.1 * altura) - 44.7
  return float (result)

def main():
  altura = float(input("Digite a sua altura: ").replace(',', '.'))
  sexo = str(input("Digite o seu sexo (M ou F): "))
  while (sexo.upper() not in ("M", "F")):
    sexo = str(input("Digite o seu sexo (M ou F): "))
  imc = calcula_imc(altura, sexo)
  print(f"Seu peso ideal é de {round(imc, 2)} Kg")

main()

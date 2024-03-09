def calcula_media_armonica() -> float:
  media = .0
  valores = [3.6, 8.9, 10]
  tamanho = len(valores)
  divisor = .0

  for valor in valores:
    divisor += (1 / valor)

  media = tamanho / divisor
  return media

def calcula_media_armonica_amortizada(amortizacao: float) -> float:
  media_amortizada = .0
  valores = [3.6, 8.9, 10]
  tamanho = len(valores)
  divisor = .0

  for valor in valores:
    divisor += (1 / (valor + amortizacao))

  media = (tamanho / divisor) - amortizacao
  return media

def main():
  print(f'Média harmônica {calcula_media_armonica()}')
  print(f'Média harmônica amortizada {calcula_media_armonica_amortizada(4)}')

main()
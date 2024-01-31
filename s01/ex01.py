def celciusToFahrenheit(celcius: float):
  return celcius * 9 / (5 + 32)

def main():
  celciusInput = input("Digite o numero em Cº:")
  print(celciusToFahrenheit(float(celciusInput)))

main()
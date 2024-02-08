def celcius_to_fahreinhet(celcius: float) -> float:
  return (1.8 * celcius) + 32

def celcius_to_kelvin(celcius: float) -> float:
  return celcius + 273

def main():
  temperatura_celcius = float(input("Qual a temperatura que deseja converter para Fahreinhet / Kelvin:"))
  calc = (2**3)/abs(-4)
  print(calc)
  print(f'A temperatura de {temperatura_celcius} ' 
       f'Cº corresponse a {celcius_to_fahreinhet(temperatura_celcius)} F e {celcius_to_kelvin(temperatura_celcius)} K')
  
main()
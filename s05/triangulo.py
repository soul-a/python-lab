def existe_desigualdade_triangular(a: float, b: float, c: float) -> bool:
  maior_lado = max(a, b, c)
  return maior_lado < (a + b + c - maior_lado)

def main():
  a = float(input("Digite o lado A do triângulo: "))
  b = float(input("Digite o lado B do triângulo: "))
  c = float(input("Digite o lado C do triângulo: "))

  if not existe_desigualdade_triangular(a, b, c):
    print("Seu triângulo é inválido!")
    exit()

  print("Seu triângulo é valido!")

  if(a == b and a == c):
    print("Seu triângulo é equilatero")
  elif(a == b or a == c or b == c):
    print("Seu triângulo é isósceles")
  else:
    print("Seu triângulo é escaleno")

main()
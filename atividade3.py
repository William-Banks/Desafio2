metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = centimetros * 100
quilometros = metros / 1000

print("==================")
print(f"O valor em metros é: {metros}m")
print(f"O valor em centímetros é: {centimetros}cm")
print(f"O valor em milímetros é: {milimetros}mm")
print(f"O valor em quilômetros é: {quilometros}km")
print("==================")
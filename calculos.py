import math

print("--- Calculadora de Engenharia Elétrica ---")

# Entradas
frequencia = float(input("Digite a frequência (Hz): "))
indutancia = float(input("Digite a indutância (H): "))
capacitancia = float(input("Digite a capacitância (F): "))

# Cálculos
xl = 2 * math.pi * frequencia * indutancia
xc = 1 / (2 * math.pi * frequencia * capacitancia)

# Resultados
print("-" * 30)
print(f"Reatância Indutiva (XL): {xl:.2f} Ohms")
print(f"Reatância Capacitiva (XC): {xc:.2f} Ohms")
print("-" * 30)
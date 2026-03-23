# Calculadora de Consumo de Energia

print("=== Calculadora de Consumo Elétrico ===")

# entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts (W)): "))
horas_dia = float(input("Digite a média de horas de uso por dia: "))

# processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000
valor_kwh = 0.90
custo = consumo_mensal * valor_kwh

# saída
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.1f} kWh/mês")
print(f"Custo estimado: R$ {custo:.1f}")

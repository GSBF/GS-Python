# Programa que vai fazer uma simulação do nível do mar 

def simular_nivel_do_mar(ano_inicial, ano_final, taxa_aumento):
    
    # Simula o aumento do nível do mar em um intervalo de anos e informa o impacto em áreas costeiras.

    # Inicialização
    nivel_do_mar = 0.0

    # Simulação ano a ano
    for ano in range(ano_inicial, ano_final + 1):
        nivel_do_mar += taxa_aumento
        print(f"Ano {ano}: Aumento do nível do mar: {nivel_do_mar:.2f} cm")

    # Resumo da simulação
    print("\nResumo:")
    print(f"Período: {ano_inicial} a {ano_final}")
    print(f"Taxa de aumento: {taxa_aumento:.2f} cm/ano")
    print(f"Aumento total: {nivel_do_mar:.2f} cm")

    # Impacto em áreas costeiras (opcional)
    if input("\nDeseja avaliar o impacto em áreas costeiras? (S/N): ").upper() == "S":
        areas_costeiras = [
            {"nome": "Área A", "altitude": 50},
            {"nome": "Área B", "altitude": 150},
            {"nome": "Área C", "altitude": 100},
        ]

        for area in areas_costeiras:
            impacto = "Inundada" if nivel_do_mar >= area["altitude"] else "Não inundada"
            print(f"{area['nome']}: {impacto}")


# Solicitação de dados ao usuário
ano_inicial = int(input("Digite o ano inicial: "))
ano_final = int(input("Digite o ano final: "))
taxa_aumento = float(input("Digite a taxa de aumento do nível do mar (cm/ano): "))

# Execução da simulação
simular_nivel_do_mar(ano_inicial, ano_final, taxa_aumento)
